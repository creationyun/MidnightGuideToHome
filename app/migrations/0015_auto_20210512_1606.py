# Generated by Django 3.1.5 on 2021-05-12 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_webpubtransroutescomparisons'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webpubtransroutescomparisons',
            name='num',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
