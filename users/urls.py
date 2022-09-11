from django.urls import path
from django.contrib.auth import views as auth_views
from .views import user_login, home
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", home, name="home"),
    path("login/",user_login,name="user_login"),
    path('logouts/', LogoutView.as_view(),name="user_logout"),
]
