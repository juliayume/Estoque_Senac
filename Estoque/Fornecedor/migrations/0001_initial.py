# Generated by Django 4.1.2 on 2022-11-11 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fornecedor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('nome', models.CharField(max_length=100)),
                ('cnpj', models.CharField(max_length=100)),
                ('endereco', models.CharField(max_length=225)),
                ('telefone', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=100)),
            ],
        ),
    ]
