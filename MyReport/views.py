
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Players, Report, User, Positions, IMG_Teams
from django.views.decorators.csrf import csrf_exempt


# Index View that will return all the teams storage in the DB


def index(request):
    if request.user.is_authenticated:
        teams = IMG_Teams.objects.all()
        is_user = True
        return render(request, 'MyReport/index.html', {
            "is_user": is_user,
            "teams": teams
        })
    else:
        return HttpResponseRedirect(reverse("login"))


# Log In User into Website
def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "MyReport/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "MyReport/login.html")


# Log Out user from Website
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        first = request.POST["first"]
        last = request.POST["last"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password, first_name=first, last_name=last)
            user.save()
        except IntegrityError:
            return render(request, "MyReport/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "MyReport/register.html")


# Here we can send and save the new reports on each players
@login_required
def send_report(request):

    if request.method != "POST":
        return JsonResponse({"error": "POST request required."}, status=400)

    defense = request.POST['defense']
    hitting = request.POST['hitting']
    pitching = request.POST['pitching']
    character_work_ethic = request.POST['character-work-ethic']
    first = request.POST['first']
    last = request.POST['last']
    x = request.POST['team']

    player = Players.objects.get(first=first, last=last)

    report = Report(CoachName=str(request.user), Player=player, Defense=defense, Hitting=hitting, Pitching=pitching, Character_Work_Ethic=character_work_ethic)
    report.save()

    return team(request, f"{x}")


# This function look up for the players into specific team and render a new html with the results if any
@login_required
def team(request, team):
    players = Players.objects.filter(team=team)
    is_user = True
    return render(request, 'MyReport/team.html', {
        "team": team,
        "players": players,
        "is_user": is_user
    })


# This Function will allow Coaches to add new player to a Team.
@login_required
def add_player(request):
    if request.method == "POST":

        team = request.POST['exampleDataList']
        first_name = request.POST['create-first']
        last_name = request.POST['create-last']
        position = request.POST['create-position']

        player = Players(team=team, first=first_name, last=last_name, player_positions=position)
        player.save()

        teams = IMG_Teams.objects.all()
        is_user = True
        
        return render(request, 'MyReport/index.html', {
            "is_user": is_user,
            "teams": teams,
            "message": "message",
        })


# This Function will allow coaches to create new teams. 
@login_required
def add_team(request):

    if request.method == "POST":

        team = request.POST['new-team']

        new_team = IMG_Teams(team = team)
        new_team.save()

        teams = IMG_Teams.objects.all()
        is_user = True

        return render(request, 'MyReport/index.html', {
            "is_user": is_user,
            "teams": teams,
            "message1": "message",
        })