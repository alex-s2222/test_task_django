from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView


app_name = "main"   


urlpatterns = [
    path("register/", views.register_request, name="register"),
    path("login/", views.login_request, name="login"),
    path('', views.main, name="main"),
    path('<int:room_pk>/', views.select_room, name='select_room'),
    path('my_booking/', views.my_booking, name='my_booking'),
    path('my_booking/<int:booking_pk>/', views.delete_room, name='delete_room')
]
