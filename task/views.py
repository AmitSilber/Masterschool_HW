from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_POST, require_GET
from django.views.decorators.csrf import csrf_exempt
import json
from Service.StudentsOrganizer import StudentsOrganizer


@require_GET
def get_flow(request):
    message = StudentsOrganizer.get_flow(request.GET["user_id"])

    return HttpResponse(message)


@require_GET
def get_state(request):
    message = StudentsOrganizer.get_state(request.GET["user_id"])
    return HttpResponse(message)


@require_GET
def get_status(request):
    message = StudentsOrganizer.get_status(request.GET["user_id"])
    return HttpResponse(message)


@csrf_exempt
@require_POST
def make_step(request):
    arguments = json.loads(request.body)
    message = StudentsOrganizer.make_step(arguments)

    return HttpResponse(message)
