from datetime import datetime

import pytz
import re

from django.apps import apps
from django.conf import settings
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.utils.translation import ugettext_lazy as _
from django.template.loader import render_to_string

from rest_framework.pagination import PageNumberPagination

from .exceptions import MailServiceError
from django.core.mail import send_mail as django_send_mail


LOCAL_TIMEZONE = pytz.timezone(settings.TIME_ZONE)


def send_mail(users, context, template):
    """
    Uses Anymail to send templated emails.
    Returns a list of email addresses to which emails failed to be delivered.
    """
    if settings.LOCAL_SETTINGS['EMAIL_SERVICE'] is False:
        raise MailServiceError(_(
            "Email service is disabled."
        ))
    MAIL_SERVICE = settings.ANYMAIL

    failed_emails = list()
    for user in users:
        message = EmailMessage(
            subject=None,  # required for SendinBlue templates
            body='',  # required for SendinBlue templates
            to=[user.email]
        )
        message.from_email = None  # required for SendinBlue templates
        # use this SendinBlue template
        message.template_id = MAIL_SERVICE["TEMPLATES"].get(template)
        message.merge_global_data = context
        response = message.send()  # return number of successfully sent emails

        if not response:
            failed_emails.append(user.email)

    return failed_emails


def remove_translation_fields(data_dict):
    """
    Used to removed translation fields.
    It matches ANYTHING followed by "_" and a 2 letter code.
    ie:
        name_fr (matches)
        reservation_date (doesn't match)
    """
    language_field = re.compile('[a-z0-9_]+_[a-z]{2}$')
    data = {
        k: v for k, v in data_dict.items() if not language_field.match(k)
    }
    return data


def check_if_translated_field(field_name, data_dict):
    """
    Used to check if a field or one of its translated version is present in a
    dictionnary.
    ie:
        name or name_fr or name_en
    Returns:
        True: one or more occurences
        False: no occurence
    """
    if field_name in data_dict:
        return True
    for lang in settings.LANGUAGES:
        if data_dict.get(''.join([field_name, "_", lang[0]])):
            return True
    return False


def get_model_from_name(model_name):
    """
    Used to get a model instance when you only have its name.
    """
    app_labels = [a.label for a in apps.app_configs.values()]
    app_number = len(app_labels)
    for idx, app in enumerate(app_labels):
        try:
            model = apps.get_model(app, model_name)
            return model
        except LookupError as err:
            if idx == (app_number - 1):
                raise err
            continue


def notify_user_of_new_account(email, password):
    if settings.LOCAL_SETTINGS['EMAIL_SERVICE'] is False:
        raise MailServiceError(_("Email service is disabled."))
    else:
        merge_data = {
            'EMAIL': email,
            'PASSWORD': password,
        }

        plain_msg = render_to_string(
            "notify_user_of_new_account.txt",
            merge_data
        )
        msg_html = render_to_string(
            "notify_user_of_new_account.html",
            merge_data
        )

        return django_send_mail(
            "Bienvenue à Thèsez-vous?",
            plain_msg,
            settings.DEFAULT_FROM_EMAIL,
            [email],
            html_message=msg_html,
        )


class ExportPagination(PageNumberPagination):
    """ Custom paginator for data exportation """
    page_size = 1000
    page_size_query_param = 'page_size'
    max_page_size = 1000

    def get_paginated_response(self, data):
        next_url = self.get_next_link()
        previous_url = self.get_previous_link()

        if next_url is not None and previous_url is not None:
            link = '<{next_url}; rel="next">, <{previous_url}; rel="prev">'
        elif next_url is not None:
            link = '<{next_url}; rel="next">'
        elif previous_url is not None:
            link = '<{previous_url}; rel="prev">'
        else:
            link = ''

        link = link.format(next_url=next_url, previous_url=previous_url)

        response = HttpResponse(
            data,
            content_type="application/vnd.ms-excel"
        )
        # Add pagination links to response
        response['Link'] = link if link else {}

        return response
