from msilib.schema import ListView
from django.shortcuts import render
from django.views.generic import ListView
from todoapp.models import ToDoEntry, ToDoList


# Create your views here.

class AllListView(ListView):
  model = ToDoList
  template_name: "todoapp/index.html"
  context_object_name: "all_lists"