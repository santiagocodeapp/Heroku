from turtle import position
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.forms import CharField

# Create your models here.

class User(AbstractUser):
    pass


class Positions(models.Model):
    field_position = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.field_position}"

class Players(models.Model):
    team = models.CharField(max_length=64)
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    player_positions = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.first} {self.last} Position: {self.player_positions}"


class Report(models.Model):
    CoachName = models.CharField(max_length=64)
    Player = models.ForeignKey('Players', on_delete = models.CASCADE)
    Defense = models.CharField(max_length=1000)
    Hitting = models.CharField(max_length=1000)
    Pitching = models.CharField(max_length=1000)
    Character_Work_Ethic = models.CharField(max_length=1000)

    def __str__(self):
        return f"New Report"


class IMG_Teams(models.Model):
    team = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.team}"