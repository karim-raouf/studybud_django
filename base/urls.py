from django.urls import path
from . import views


urlpatterns = [
    path('', views.home , name = 'home'),
    path('room/<int:id>', views.room , name = 'room'),
    path('create-room', views.createroom , name = 'create-room'),
    path('update-room/<int:id>', views.updateroom , name = 'update-room'),
    path('delete-room/<int:id>', views.deleteroom , name = 'delete-room'),
    path('login/', views.loginpage , name = 'login'),
]
