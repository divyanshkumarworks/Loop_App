# Generated by Django 4.2.4 on 2023-09-21 13:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_rename_update_last_week_storereport_uptime_last_week'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='storereport',
            name='report_id',
        ),
    ]
