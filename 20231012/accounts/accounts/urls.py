from django.urls import path
from . import views

urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("profile/", views.profile, name="profile"),
    path("logincheck/", views.login_check, name="profile"),
    path('loginfbv/', views.loginfbv, name='loginfbv'),
]
