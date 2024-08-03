from django.urls import path
from . import views

urlpatterns = [

    path('Upload-File', views.Index, name='Index'),
    path('Result', views.Result, name='Result'),
]
