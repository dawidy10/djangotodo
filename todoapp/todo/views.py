from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.urls import reverse
from .models import Task
from django.core import serializers
import json
from .serializers import ToDoSerializer
# Create your views here.

def todos(request):
    return render(request, "todos.html")

def tasks(request):
    # Tasks = serializers.serialize("Tasks" , Task.objects.all())
    # return JsonResponse(Tasks)
    todos = Task.objects.all()
    Tasks = ToDoSerializer(todos).data
    return JsonResponse(Tasks)