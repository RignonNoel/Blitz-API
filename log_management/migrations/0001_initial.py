# Generated by Django 2.2.5 on 2019-10-03 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(max_length=100, verbose_name='Source')),
                ('level', models.CharField(max_length=100, verbose_name='Level')),
                ('message', models.TextField(verbose_name='Message')),
                ('error_code', models.CharField(blank=True, max_length=100, null=True, verbose_name='Error Code')),
                ('additional_data', models.TextField(blank=True, null=True, verbose_name='Additional data')),
                ('traceback_data', models.TextField(blank=True, null=True, verbose_name='TraceBack')),
            ],
            options={
                'verbose_name': 'Log',
                'verbose_name_plural': 'Logs',
            },
        ),
    ]
