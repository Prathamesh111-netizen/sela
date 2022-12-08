# from django.conf.urls import url, include
from django.urls import re_path as url
from django.contrib import admin
from django.contrib import admin
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [	
    url('getJobs', views.JobRecommendation.as_view()),
]