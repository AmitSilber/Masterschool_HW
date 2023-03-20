from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_POST, require_GET
from django.views.decorators.csrf import csrf_exempt
import json
from Service.SystemWrapper import StudentsOrganizer


@require_GET
def get_task(request):
    print(request)
    return HttpResponse(request)


@csrf_exempt
@require_POST
def add_student(request):
    a = json.loads(request.body)
    message = StudentsOrganizer.add_student(a)
    return HttpResponse(message)


@csrf_exempt
@require_POST
def check_student(request):
    a = json.loads(request.body)
    print(StudentsOrganizer.check_status(a["user_id"]))
    return HttpResponse("check")


@csrf_exempt
@require_POST
def initialize(request):
    return HttpResponse("created system")
