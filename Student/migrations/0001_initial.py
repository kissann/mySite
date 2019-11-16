# Generated by Django 2.2.6 on 2019-11-08 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('increment', models.AutoField(db_index=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('dateB', models.DateField()),
                ('desc', models.TextField()),
                ('zarplata', models.SmallIntegerField()),
                ('slug', models.SlugField(default='', max_length=200, unique=True)),
            ],
        ),
    ]
