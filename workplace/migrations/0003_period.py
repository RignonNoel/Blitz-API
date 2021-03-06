# Generated by Django 2.0.2 on 2018-05-26 19:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workplace', '0002_picture'),
    ]

    operations = [
        migrations.CreateModel(
            name='Period',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=253, verbose_name='Name')),
                ('price', models.PositiveIntegerField(verbose_name='Price')),
                ('start_date', models.DateTimeField(blank=True, verbose_name='Start Date')),
                ('end_date', models.DateTimeField(blank=True, verbose_name='End Date')),
                ('is_active', models.BooleanField(default=False, verbose_name='Activation')),
                ('workplace', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='periods', to='workplace.Workplace', verbose_name='Workplace')),
            ],
            options={
                'verbose_name': 'Period',
                'verbose_name_plural': 'Periods',
            },
        ),
    ]
