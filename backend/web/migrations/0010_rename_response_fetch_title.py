# Generated by Django 4.1 on 2022-08-23 14:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("web", "0009_timing_dnstime_timing_domready"),
    ]

    operations = [
        migrations.RenameField(
            model_name="fetch", old_name="response", new_name="title",
        ),
    ]
