# Generated by Django 4.1.2 on 2022-11-11 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Local',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('sala', models.CharField(max_length=100)),
                ('armario', models.CharField(max_length=100)),
                ('numero', models.CharField(max_length=10)),
            ],
        ),
    ]