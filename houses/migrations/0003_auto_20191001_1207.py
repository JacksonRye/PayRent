# Generated by Django 2.2.5 on 2019-10-01 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0002_auto_20191001_1058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='houseimage',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
