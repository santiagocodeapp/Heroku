from re import U
from django.contrib import admin
from .models import User, Positions, Players, Report, IMG_Teams

# Register your models here.
admin.site.register(User)
admin.site.register(Positions)
admin.site.register(Players)
admin.site.register(Report)
admin.site.register(IMG_Teams)