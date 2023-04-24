# Generated by Django 3.1 on 2023-04-24 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AirHumidity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current', models.FloatField()),
                ('high', models.FloatField()),
                ('medium', models.FloatField()),
                ('low', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('name', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('state', models.IntegerField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='HistoryAirHumidity',
            fields=[
                ('time', models.DateTimeField(primary_key=True, serialize=False)),
                ('value', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='HistoryLight',
            fields=[
                ('time', models.DateTimeField(primary_key=True, serialize=False)),
                ('value', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='HistorySoil',
            fields=[
                ('time', models.DateTimeField(primary_key=True, serialize=False)),
                ('value', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='HistoryTemprature',
            fields=[
                ('time', models.DateTimeField(primary_key=True, serialize=False)),
                ('value', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='LightIntensitive',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current', models.FloatField()),
                ('high', models.FloatField()),
                ('medium', models.FloatField()),
                ('low', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('time', models.DateTimeField(primary_key=True, serialize=False)),
                ('content', models.TextField()),
                ('state', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device', models.CharField(max_length=30)),
                ('start', models.TimeField()),
                ('end', models.TimeField()),
                ('date', models.DateField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='SoilMoisure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current', models.FloatField()),
                ('high', models.FloatField()),
                ('medium', models.FloatField()),
                ('low', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Temprature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current', models.FloatField()),
                ('high', models.FloatField()),
                ('medium', models.FloatField()),
                ('low', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Threshold',
            fields=[
                ('name', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('value', models.IntegerField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('username', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=30)),
                ('role', models.CharField(blank=True, max_length=30)),
            ],
        ),
    ]
