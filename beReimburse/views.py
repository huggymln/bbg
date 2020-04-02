from django.shortcuts import render
from django.http import JsonResponse
from beReimburse import models
from django.contrib.auth.models import User

def index(request):
    pisang ={
        "description": "ngentod",
    }
    user = User(
        username = "bambang123",
        #password = "bbg21",
    )
    user.set_password("bbg21")
    user.save()
    emp = models.Employee(
        name = "bambang",
        nrek = "14045",
        user = user,
    )
    emp.save()
# Create your views here.
    return JsonResponse(emp)
