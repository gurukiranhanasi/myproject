from django.urls import path
from projectapp import views

urlpatterns=[
    path('',views.index),
    path('index1/',views.index1),
]
