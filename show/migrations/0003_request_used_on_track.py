# Generated by Django 3.2.6 on 2021-10-16 02:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0003_auto_20211016_0230'),
        ('show', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='used_on_track',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainsite.song'),
        ),
    ]
