# Generated by Django 2.2.6 on 2019-10-02 19:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0006_auto_20191001_1839'),
        ('auction', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='auctionsession',
            name='house',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='houses.House'),
            preserve_default=False,
        ),
    ]
