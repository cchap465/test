"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.views.generic import ListView
from polls.models import *
from django.views.generic.edit import CreateView

class NewList(ListView):
    template_name= 'index.html'
    model = Question

class CreateItem(CreateView):
    template_name = 'index.html'
    model = Question
    fields = ['question_text']
    success_url = '/'

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('', NewList.as_view()),
    path('admin/', admin.site.urls)
]
