from django.urls import path, include
from . import views

urlpatterns = [ 
    path('login', views.loginUser, name='login'),
    path('logout', views.logoutUser, name='logout'),
    path('register', views.registerUser, name='register'),

    path('create-mountain', views.createMountain, name='createMountain'),
    path('read-mountains', views.readMountains, name='readMountains'),
    path('read-one-mountain/<str:pk>', views.readOneMountain, name='readOneMountain'),
    path('update-one-mountain/<str:pk>', views.updateMountain, name='updateMountain'),
    path('delete-mountain/<str:pk>', views.deleteMountain, name='deleteMountain'),
  
]