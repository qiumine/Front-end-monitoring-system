# Generated by Django 4.1 on 2022-08-25 04:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("web", "0011_xhr_method"),
    ]

    operations = [
        migrations.RemoveField(model_name="xhr", name="method",),
    ]
