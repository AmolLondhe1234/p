from django.urls import path
from . import views
urlpatterns = [
    path('',views.profile),
    path('ps',views.ps,name='profile'),
    path('skill',views.skill,name='skills'),
    path('cert',views.cert,name='cert'),
    path('project',views.project,name='project'),
    path('hireme',views.hireme,name='hireme'),
    # path('feedback',views.feedback,name='feedback')
]