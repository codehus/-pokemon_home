# Generated by Django 4.1.6 on 2023-02-09 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('edad', models.IntegerField()),
                ('pais', models.CharField(default='', max_length=30)),
                ('dni', models.CharField(default='00000000', max_length=8)),
                ('vigente', models.BooleanField(default=True)),
            ],
        ),
    ]
