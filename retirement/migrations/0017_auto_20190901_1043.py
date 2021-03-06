# Generated by Django 2.2.2 on 2019-09-01 14:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0031_auto_20190901_1043'),
        ('retirement', '0016_auto_20190815_0328'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalretreat',
            name='hidden',
            field=models.BooleanField(default=False, verbose_name='Hidden'),
        ),
        migrations.AddField(
            model_name='retreat',
            name='hidden',
            field=models.BooleanField(default=False, verbose_name='Hidden'),
        ),
        migrations.CreateModel(
            name='RetreatInvitation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('url_token', models.CharField(max_length=40, unique=True, verbose_name='Key')),
                ('name', models.CharField(blank=True, max_length=253, null=True, verbose_name='Name')),
                ('nb_places', models.IntegerField(verbose_name='Number of places')),
                ('coupon', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='invitations', to='store.Coupon', verbose_name='Coupon')),
                ('retreat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invitations', to='retirement.Retreat', verbose_name='Retreat')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HistoricalRetreatInvitation',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('url_token', models.CharField(db_index=True, max_length=40, verbose_name='Key')),
                ('name', models.CharField(blank=True, max_length=253, null=True, verbose_name='Name')),
                ('nb_places', models.IntegerField(verbose_name='Number of places')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('coupon', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='store.Coupon', verbose_name='Coupon')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('retreat', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='retirement.Retreat', verbose_name='Retreat')),
            ],
            options={
                'verbose_name': 'historical retreat invitation',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.AddField(
            model_name='historicalreservation',
            name='invitation',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='retirement.RetreatInvitation', verbose_name='Invitation'),
        ),
        migrations.AddField(
            model_name='reservation',
            name='invitation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='retreat_reservations', to='retirement.RetreatInvitation', verbose_name='Invitation'),
        ),
    ]
