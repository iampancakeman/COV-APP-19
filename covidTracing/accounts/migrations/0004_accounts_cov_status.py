# Generated by Django 3.2 on 2021-05-20 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_accounts_user_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='accounts',
            name='cov_status',
            field=models.CharField(choices=[('NEGATIVE', 'Negative'), ('POSITIVE', 'Positive'), ('PENDING', 'Pending')], default='NEGATIVE', max_length=8),
        ),
    ]