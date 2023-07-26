from django.urls import path
from . import views



urlpatterns  = [
    path('login/', views.loginPage, name='login'),
     path('register/', views.registerPage, name='register'),
     path('logout/', views.logoutUser, name='logout'),
    path('', views.home, name='home'),
    path('profile/<str:pk>/', views.user_profile, name='user-profile'),
    path('room/<str:pk>/', views.room, name = 'room'),
    path('createroom/', views.create_room, name='create-room'),
    path('updateroom/<str:pk>/', views.update_room, name='update-room'),
    path('deleteroom/<str:pk>/', views.delete_room, name='delete-room'),
    path('deletemessage/<str:pk>/', views.delete_message, name='delete-message'),
    path('updateuser/', views.update_user, name='update-user'),
    path('topics/', views.topics_page, name='topics'),
    path('activity/', views.activity_page, name='activity'),
]