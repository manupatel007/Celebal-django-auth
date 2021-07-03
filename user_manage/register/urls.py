from django.urls import path, include
from . import views
urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),
    path("", views.home, name="home"),
    path("register/",views.register, name="register"),
]