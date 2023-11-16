from app.views import *
from django.urls import path
app_name='ok'
urlpatterns=[
    path('data_render/',data_render,name='data_render')
    
]