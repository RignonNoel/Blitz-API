# Generated by Django 2.2.10 on 2020-04-03 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('retirement', '0025_auto_20200312_1205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalreservation',
            name='cancelation_reason',
            field=models.CharField(blank=True, choices=[('U', 'User canceled'), ('RD', 'Retreat deleted'), ('RM', 'Retreat modified'), ('A', 'Admin canceled')], max_length=100, null=True, verbose_name='Cancelation reason'),
        ),
        migrations.AlterField(
            model_name='historicalretreat',
            name='seats',
            field=models.PositiveIntegerField(verbose_name='Seats'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='cancelation_reason',
            field=models.CharField(blank=True, choices=[('U', 'User canceled'), ('RD', 'Retreat deleted'), ('RM', 'Retreat modified'), ('A', 'Admin canceled')], max_length=100, null=True, verbose_name='Cancelation reason'),
        ),
        migrations.AlterField(
            model_name='retreat',
            name='seats',
            field=models.PositiveIntegerField(verbose_name='Seats'),
        ),
    ]