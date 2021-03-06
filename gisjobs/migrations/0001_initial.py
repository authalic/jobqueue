# Generated by Django 2.0.1 on 2018-01-23 03:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GISjob',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jobname', models.CharField(max_length=80)),
                ('date_submited', models.DateTimeField(auto_now_add=True, verbose_name='Submitted')),
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name='Modified')),
                ('date_assigned', models.DateTimeField(verbose_name='Assigned')),
                ('date_due', models.DateTimeField(verbose_name='Due')),
                ('date_completed', models.DateTimeField(verbose_name='Completed')),
                ('job_status', models.CharField(choices=[('N', 'New'), ('P', 'Previously Completed'), ('U', 'Unassigned'), ('A', 'Assigned'), ('D', 'Done')], default='N', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='GISpro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='JobSubmitter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('office_code', models.CharField(max_length=3, verbose_name='Office Code')),
                ('office_name', models.CharField(max_length=80, verbose_name='Office Name')),
                ('office_add1', models.CharField(max_length=60, verbose_name='Address')),
                ('office_add2', models.CharField(max_length=24, verbose_name='Ste')),
                ('office_city', models.CharField(max_length=40, verbose_name='City')),
                ('office_state', models.CharField(max_length=2, verbose_name='State')),
                ('office_zip', models.CharField(max_length=10, verbose_name='ZIP')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_code', models.CharField(max_length=12)),
                ('project_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='jobsubmitter',
            name='employee_office',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gisjobs.Office'),
        ),
        migrations.AddField(
            model_name='gisjob',
            name='assigned_to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gisjobs.GISpro'),
        ),
        migrations.AddField(
            model_name='gisjob',
            name='project_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gisjobs.Project'),
        ),
        migrations.AddField(
            model_name='gisjob',
            name='submitted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gisjobs.JobSubmitter'),
        ),
    ]
