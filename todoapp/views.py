
from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView
from todoapp.models import ToDoEntry, ToDoList


# Create your views here.

class AllListView(ListView):
  model = ToDoList
  template_name = "todoapp/index.html"
  context_object_name = 'list'


class DetailListView(ListView):
  model = ToDoEntry
  template_name = "todoapp/todo.html"
  context_object_name = 'list_todo'

  def get_queryset(self):
    x =  ToDoEntry.objects.filter(todo_list_id=self.kwargs["pk"])
    print(x)
    return x

  def get_context_data(self):
        context = super().get_context_data()
        context["todo_list"] = ToDoList.objects.get(id=self.kwargs["pk"])
        return context

class TodoUpdateView(UpdateView):
  model = ToDoEntry
  context_object_name = 'todo'
  template_name = "todoapp/update_form.html"
  fields = [
    "todo_titel",
  ]
