# Generated by Django 2.0.1 on 2018-01-23 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gisjobs', '0002_auto_20180123_0435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gisjob',
            name='date_completed',
            field=models.DateTimeField(blank=True, verbose_name='Completed'),
        ),
    ]