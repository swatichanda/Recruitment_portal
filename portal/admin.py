# from django.contrib import admin
# from.models import Job,Profile
# # Register your models here.
# admin.site.register(Job,Profile)
from django.contrib import admin
from .models import Job, Profile

admin.site.register(Job)
admin.site.register(Profile)
