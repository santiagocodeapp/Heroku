from django.urls import URLPattern, path
from . import views

app_name = "student"

urlpatterns = [

    path("", views.student_index, name="index"),
    path("login", views.student_login_view, name="login"),
    path("logout", views.student_logout_view, name="logout"),
    path("register", views.student_register, name="register"),

]
