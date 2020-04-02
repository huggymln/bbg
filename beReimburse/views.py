from django.shortcuts import render
from django.http import JsonResponse
from beReimburse import models
from django.contrib.auth.models import User
import json

def index(request):
    pisang ={
        "description": "ngentod",
    }

    # Create user
    user = User(
        username = "something2",
        #password = "bbg21",
    )
    user.set_password("bbg21")
    user.save()

    # Creat employee
    emp = models.Employee(
        name = "somethign 2",
        nrek = "14045",
        user = user,
    )
    emp.save()

    # Create your views here.
    return JsonResponse({
        "name": emp.name,
        "no-rek": emp.nrek,
        "userName": emp.user.username,
    })

def accept_reimburse(request, reimburse_id):
    reimburse = models.Reimburses.objects.get(id=reimburse_id)
    reimburse.stat = "Accepted"
    reimburse.save()

    return JsonResponse({
        "statusCode": 200,
    })

def reject_reimburse(request):
    return JsonResponse({
        "statusCode": 200,
    })

def on_progress_reimburse(request):
    return JsonResponse({
        "statusCode": 200,
    })

