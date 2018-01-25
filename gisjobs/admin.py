from django.contrib import admin

from gisjobs.models import Project, GISjob

# Register your models here.



class ProjectAdmin(admin.ModelAdmin):
    list_display = ( 'project_code', 'project_name')


class GISjobAdmin(admin.ModelAdmin):
    fields = [
        'jobname',
        'project_id',
        'submitted_by',
        'date_due',
        'description'
    ]
    list_display = ('jobname', 'project_id', 'submitted_by', 'date_due')

admin.site.register(Project, ProjectAdmin)
admin.site.register(GISjob, GISjobAdmin)