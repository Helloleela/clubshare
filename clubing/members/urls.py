from django.urls import path
from . import views

urlpatterns = [ 
    path('login_user', views.login_user, name='login'),
    path("logout_user", views.user_logout, name='logout'),
    path("register_user", views.user_register, name="register"),
]