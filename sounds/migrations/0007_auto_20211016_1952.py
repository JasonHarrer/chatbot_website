# Generated by Django 3.2.6 on 2021-10-16 19:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sounds', '0006_auto_20211016_1946'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='instrument',
            name='played_by',
        ),
        migrations.RemoveField(
            model_name='instrument',
            name='requested_by',
        ),
    ]