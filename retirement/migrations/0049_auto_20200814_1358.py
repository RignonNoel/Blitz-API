# Generated by Django 2.2.12 on 2020-08-14 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('retirement', '0048_auto_20200814_1354'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalretreattype',
            name='index_ordering',
            field=models.PositiveIntegerField(default=1, verbose_name='Index for display'),
        ),
        migrations.AddField(
            model_name='retreattype',
            name='index_ordering',
            field=models.PositiveIntegerField(default=1, verbose_name='Index for display'),
        ),
    ]