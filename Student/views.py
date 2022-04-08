from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import json
from MyReport.models import Players, Report, User, IMG_Teams




# Index View that will return all the teams storage in the DB
def student_index(request):
    if request.user.is_authenticated:

        is_user = True
        user = User.objects.get(username = str(request.user))

        try:
            player = Players.objects.get(first = str(user.first_name))
            reports = Report.objects.filter(Player_id = player.id).order_by("-pk")

            return render(request, 'Student/student-index.html',{
                "reports": reports,
                "is_user": is_user,
                "user": user
            })
        except:
             return render(request, 'Student/student-index.html',{
                "message": "Sorry, something is wrong with the report search.",
                "is_user": is_user,
            })
    else:
        return HttpResponseRedirect(reverse("student:login"))


# Log In User into Website
def student_login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("student:index"))
        else:
            return render(request, "Student/student-login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "Student/student-login.html")


# Log Out user from Website
def student_logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("student:index"))




def student_register(request):
    if request.method == "POST":
        username = request.POST["username"]
        first = request.POST["first"]
        last = request.POST["last"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "Student/student-register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password, first_name = first, last_name = last)
            user.save()
        except IntegrityError:
            return render(request, "Student/student-register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("student:index"))
    else:
        return render(request, "Student/student-register.html")

