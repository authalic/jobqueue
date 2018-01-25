from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Project, GISjob
from gisjobs.models import GISjob
from django.urls import reverse_lazy

# Create your views here.


class JobQueue(LoginRequiredMixin, generic.ListView):
    model = GISjob


class JobRequestDetail(LoginRequiredMixin, generic.DetailView):
    model = GISjob


class GISjobCreate(LoginRequiredMixin, CreateView):
    model = GISjob
    fields = ['jobname', 'project_id', 'submitted_by', 'date_due', 'description']
    success_url = reverse_lazy('job-queue')


class GISjobUpdate(LoginRequiredMixin, UpdateView):
    model = GISjob
    fields = ['jobname', 'project_id', 'submitted_by', 'date_due', 'description']
    success_url = reverse_lazy('job-queue')


class GISjobDelete(LoginRequiredMixin, DeleteView):
    model = GISjob
    success_url = reverse_lazy('job-queue')


class GISjobByUser(LoginRequiredMixin, generic.ListView):
    model = GISjob
    template_name = 'gisjobs/gisjob_list.html'

    def get_queryset(self):
        return GISjob.objects.filter(submitted_by=self.request.user).order_by('-date_submitted')
    

