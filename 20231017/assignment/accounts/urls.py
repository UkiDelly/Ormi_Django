from django.urls import path

from .views import Login, Register, Logout, profile

urlpatterns = [
    path("signup/", Register.as_view(), name="signup"),
    path("login/", Login.as_view(), name="login"),
    path("logout/", Logout.as_view(), name="logout"),
    path("profile/", profile, name="profile"),
]
