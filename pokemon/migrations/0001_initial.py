# Generated by Django 4.1.6 on 2023-02-09 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('tipo', models.CharField(max_length=30)),
                ('generacion', models.CharField(default='Sin generacion', max_length=20)),
            ],
        ),
    ]
