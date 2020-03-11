# Generated by Django 2.2.11 on 2020-03-10 21:08

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AGEvent',
            fields=[
                ('event_uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('event_name', models.CharField(blank=True, max_length=40)),
                ('event_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('event_description', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='AGSensorType',
            fields=[
                ('sensorType_id', models.AutoField(primary_key=True, serialize=False)),
                ('sensorType_name', models.CharField(blank=True, max_length=1024)),
                ('sensorType_processingFormula', models.IntegerField(default=0)),
                ('sensorType_format', django.contrib.postgres.fields.jsonb.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='AGVenue',
            fields=[
                ('venue_uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('venue_name', models.CharField(blank=True, max_length=100)),
                ('venue_description', models.CharField(blank=True, max_length=100)),
                ('venue_latitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('venue_longitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AGSensor',
            fields=[
                ('sensor_id', models.AutoField(primary_key=True, serialize=False)),
                ('sensor_name', models.CharField(blank=True, max_length=1024)),
                ('sensor_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ag_data.AGSensorType')),
            ],
        ),
        migrations.CreateModel(
            name='AGMeasurement',
            fields=[
                ('measurement_uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('measurement_timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('measurement_value', django.contrib.postgres.fields.jsonb.JSONField()),
                ('measurement_event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ag_data.AGEvent')),
                ('measurement_sensor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ag_data.AGSensor')),
            ],
        ),
        migrations.AddField(
            model_name='agevent',
            name='event_venue',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ag_data.AGVenue'),
        ),
    ]
