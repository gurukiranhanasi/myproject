from django.urls import path
from projectapp import views

urlpatterns = [
    path('',views.index1,name='register'),
    path('login/',views.index2,name='login'),
    path('home/',views.index3,name='home'),
    path('user_logout/',views.user_logout,name="user_logout"),
    path('dashboard/',views.dashboard,name='dashboard'), 
    path('blog/',views.blog,name='blog'), 
    path('jobdetails/<int:pk>/',views.jobdetails,name='jobdetails'), 
    path('search/',views.search,name='search'), 
    path('likepost/<int:pk>/',views.like_post,name='likepost'),
    path('bookmarks/<int:pk>/',views.bookmark,name='bookmarks'),
    path('bookmark',views.bookmarks,name='bookmark'),
    path('likes',views.liked,name='likes'),
]