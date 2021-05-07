# Generated by Django 3.2 on 2021-05-06 06:39

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('houseNumber', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Locations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('locationName', models.CharField(max_length=255)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='visitinfo.address')),
            ],
        ),
        migrations.CreateModel(
            name='PostCode',
            fields=[
                ('postcode', models.CharField(max_length=4, primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator(code='nomatch', message='Length has to be 4 integers', regex='^(\\d{4})$')])),
                ('state', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='visits',
            fields=[
                ('visitID', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True)),
                ('timeOfVisit', models.DateTimeField(default=datetime.datetime.now)),
                ('locationID', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='visitinfo.locations')),
                ('userID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Street',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('PostCode', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='visitinfo.postcode')),
            ],
        ),
        migrations.AddField(
            model_name='address',
            name='streetID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='visitinfo.street'),
        ),
    ]
