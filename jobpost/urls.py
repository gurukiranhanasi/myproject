from django.urls import path
from jobpost import views



urlpatterns=[
    path('',views.job,name='jobpost'),
    path('<int:pk>/',views.Jobdetails.as_view(),name='details'),
    path('submit/',views.submits,name="submit"),
    path('appjobs/',views.appjobs,name="appjobs"),
    path('addpost/',views.addpost,name="addpost"),
]