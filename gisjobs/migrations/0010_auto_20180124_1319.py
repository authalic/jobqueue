# Generated by Django 2.0.1 on 2018-01-24 20:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gisjobs', '0009_auto_20180124_1244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gisjob',
            name='assigned_to',
            field=models.ForeignKey(blank=True, limit_choices_to={'groups__name': 'GIS'}, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='claimed', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='gisjob',
            name='submitted_by',
            field=models.ForeignKey(blank=True, limit_choices_to={'groups__name': 'Agents'}, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='requested', to=settings.AUTH_USER_MODEL),
        ),
    ]
