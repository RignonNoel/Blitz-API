# Generated by Django 2.2.13 on 2020-11-25 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blitz_api', '0023_auto_20200527_2204'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicaluser',
            name='membership_end_notification',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Membership end notification date'),
        ),
        migrations.AddField(
            model_name='user',
            name='membership_end_notification',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Membership end notification date'),
        ),
    ]