# Generated by Django 2.2.5 on 2019-10-01 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0005_auto_20191001_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='houseimage',
            name='image',
            field=models.ImageField(blank=True, upload_to='photo/%Y/%m/%d'),
        ),
    ]