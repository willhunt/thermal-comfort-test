# Generated by Django 3.1.3 on 2020-11-15 18:54

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BodyZoneModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body_zones', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='TestModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True)),
                ('project', models.CharField(max_length=10)),
                ('rig', models.CharField(max_length=30)),
                ('condition', models.CharField(max_length=20)),
                ('start', models.DateTimeField(null=True)),
                ('end', models.DateTimeField(null=True)),
                ('notes', models.TextField()),
                ('duration', models.DurationField(default=datetime.timedelta(seconds=3600))),
                ('frequency', models.DurationField(default=datetime.timedelta(seconds=600))),
                ('sensation_scale', models.CharField(choices=[('ASHRAE', 'ASHRAE scale'), ('Berkley', 'Berkley advanced scale')], default='Berkley', max_length=15)),
                ('body_zones', models.ManyToManyField(to='subjectivetest.BodyZoneModel')),
            ],
        ),
        migrations.CreateModel(
            name='ProfileModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField(blank=True, null=True)),
                ('mass', models.FloatField(blank=True, null=True)),
                ('height', models.FloatField(blank=True, null=True)),
                ('sex', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('N', 'Prefer not to say')], default='F', max_length=1)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PresetZonesModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('zone', models.ManyToManyField(to='subjectivetest.BodyZoneModel')),
            ],
        ),
        migrations.CreateModel(
            name='OccupantModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=30)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LocalResponseModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now=True)),
                ('comfort', models.IntegerField(default=0)),
                ('sensation', models.IntegerField(default=0)),
                ('stickiness', models.IntegerField(default=0)),
                ('body_zone', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='subjectivetest.bodyzonemodel')),
                ('occupant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subjectivetest.occupantmodel')),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subjectivetest.testmodel')),
            ],
        ),
        migrations.CreateModel(
            name='GlobalResponseModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now=True)),
                ('sensation_change', models.IntegerField(default=0)),
                ('acceptable', models.BooleanField(default=True)),
                ('satisfied', models.BooleanField(default=True)),
                ('notes', models.TextField()),
                ('occupant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='subjectivetest.occupantmodel')),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subjectivetest.testmodel')),
            ],
        ),
    ]
