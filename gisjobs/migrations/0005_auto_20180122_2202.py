# Generated by Django 2.0.1 on 2018-01-23 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gisjobs', '0004_gisjob_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gisjob',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]