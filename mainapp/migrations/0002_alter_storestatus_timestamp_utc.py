# Generated by Django 4.2.4 on 2023-09-19 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storestatus',
            name='timestamp_utc',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
