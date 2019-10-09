# Generated by Django 2.2.6 on 2019-10-04 15:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0004_auto_20191004_1648'),
        ('houses', '0006_auto_20191001_1839'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookedHouses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booked_by', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='booked', to='accounts.Profile')),
                ('house', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='houses.House')),
            ],
        ),
    ]
