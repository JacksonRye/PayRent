# Generated by Django 2.2.5 on 2019-10-01 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_profile_account_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='account_type',
            field=models.CharField(choices=[('landlord', 'Landlord'), ('tenant', 'Tenant')], default='tenant', max_length=15),
        ),
    ]
