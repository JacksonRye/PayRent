# Generated by Django 2.2.5 on 2019-10-01 09:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField()),
                ('number_of_rooms', models.PositiveSmallIntegerField(default=1)),
                ('number_of_toilets', models.PositiveSmallIntegerField(default=0)),
                ('description', models.TextField()),
                ('price', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='HouseImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('house', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='houses.House')),
            ],
        ),
        migrations.DeleteModel(
            name='Houses',
        ),
    ]
