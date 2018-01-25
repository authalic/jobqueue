from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime
from django.urls import reverse

# Create your models here.


class Project(models.Model):
    project_code = models.CharField(max_length=12, blank=True)
    project_name = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Internal Project"

    def __str__(self):
        return self.project_name


class GISjob(models.Model):
    jobname = models.CharField(max_length=80)
    project_id = models.ForeignKey(Project, on_delete=models.PROTECT, blank=True)
    submitted_by = models.ForeignKey(User, related_name='submitted', limit_choices_to={'groups__name': 'Agents'}, on_delete=models.PROTECT, null=True, blank=True)
    assigned_to = models.ForeignKey(User, related_name='claimed', limit_choices_to={'groups__name': 'GIS'}, on_delete=models.PROTECT, null=True, blank=True)
    date_submitted = models.DateTimeField('Submitted', auto_now_add=True)
    date_modified = models.DateTimeField('Modified', default=timezone.now)
    date_assigned = models.DateTimeField('Assigned', null=True)
    date_due = models.DateTimeField('Due')
    date_completed = models.DateTimeField('Completed', null=True)
    description = models.TextField(blank=True, null=True)

    JOB_STATUS_CHOICES = (
        ('N', 'New'),
        ('P', 'Previously Completed'),
        ('U', 'Unassigned'),
        ('A', 'Assigned'),
        ('D', 'Done')
    )

    job_status = models.CharField(
        max_length=2,
        choices=JOB_STATUS_CHOICES,
        default='N'
        )

    class Meta:
        verbose_name = "GIS Job"

    def get_absolute_url(self):
        return reverse('job-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.jobname
