
from django.urls import URLPattern, path
from . import views

# app_name = 'coach'
urlpatterns = [

    path("", views.index, name = "index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("team/<str:team>", views.team, name="team"),
    path("send/report", views.send_report, name="send-report"),
    path("add/player", views.add_player, name="add-player"),
    path("add/team", views.add_team, name="add-team"),

]