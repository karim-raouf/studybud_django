from django.urls import path
from . import views



urlpatterns = [
     
    path('login/', views.loginpage , name = 'login'),
    path('logout/', views.logoutuser , name = 'logout'),
    path('register/', views.registerpage, name='register'),


    
    path('', views.home , name = 'home'),
    path('room/<int:id>', views.room , name = 'room'),
    path('profile/<int:id>', views.userprofile , name = 'user-profile'),
    
    
    path('create-room', views.createroom , name = 'create-room'),
    path('update-room/<int:id>', views.updateroom , name = 'update-room'),
    path('delete-room/<int:id>', views.deleteroom , name = 'delete-room'),
    path('delete-message/<int:id>', views.deletemessage , name = 'delete-message'),
]   