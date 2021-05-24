# Generated by Django 3.2 on 2021-05-24 12:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vaccineinfo', '0005_vaccines_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='RolloutGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('from_age', models.CharField(max_length=3)),
                ('to_age', models.CharField(max_length=3)),
                ('starting_date', models.CharField(max_length=50)),
                ('vaccine_to_give', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='vaccineinfo.vaccines')),
            ],
        ),
    ]
