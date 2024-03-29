# Generated by Django 2.2.6 on 2019-11-09 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0002_auto_20191108_1735'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('increment', models.AutoField(db_index=True, primary_key=True, serialize=False)),
                ('number', models.SmallIntegerField()),
                ('desc', models.TextField(max_length=5000)),
                ('slug', models.SlugField(default='', max_length=200, unique=True)),
            ],
        ),
    ]
