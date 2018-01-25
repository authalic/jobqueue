from django.urls import path
from . import views


urlpatterns = [
    path('', views.JobQueue.as_view(), name='job-queue'),
    path('request/<int:pk>', views.JobRequestDetail.as_view(), name='job-detail'),
    path('request/add/', views.GISjobCreate.as_view(), name='request-add'),
    path('request/<int:pk>/update/', views.GISjobUpdate.as_view(), name='request-update'),
    path('request/<int:pk>/delete/', views.GISjobDelete.as_view(), name='request-delete'),
    path('queue/myjobs/', views.GISjobByUser.as_view(), name='queue-my-jobs')
]
