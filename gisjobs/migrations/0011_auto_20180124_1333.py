# Generated by Django 2.0.1 on 2018-01-24 20:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gisjobs', '0010_auto_20180124_1319'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gisjob',
            old_name='date_submited',
            new_name='date_submitted',
        ),
    ]
