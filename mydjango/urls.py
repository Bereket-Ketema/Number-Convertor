from django.urls import path

from . import views


urlpatterns=[
   path('',views.select,name='select'),
   path('numbers',views.numbers,name='numbers'),
    ]