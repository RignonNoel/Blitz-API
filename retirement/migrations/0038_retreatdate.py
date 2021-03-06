# Generated by Django 2.2.12 on 2020-07-23 18:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('retirement', '0037_automaticemaillog'),
    ]

    operations = [
        migrations.CreateModel(
            name='RetreatDate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(verbose_name='Start time')),
                ('end_time', models.DateTimeField(verbose_name='End time')),
                ('retreat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='retreat_dates', to='retirement.Retreat', verbose_name='Retreat')),
            ],
            options={
                'verbose_name': 'Retreat date',
                'verbose_name_plural': 'Retreat dates',
            },
        ),
    ]
