# Generated by Django 2.1.1 on 2018-10-10 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_webguiderequests'),
    ]

    operations = [
        migrations.AddField(
            model_name='webguiderequests',
            name='request_content',
            field=models.TextField(blank=True),
        ),
    ]
