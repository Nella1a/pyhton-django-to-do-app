
from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from todoapp.models import ToDoEntry, ToDoList
from django.urls import reverse, reverse_lazy


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
    x =  ToDoEntry.objects.filter(todo_list_id=self.kwargs["list_id"])
   # print("get_query:", x)
    return x

  def get_context_data(self):
        context = super().get_context_data()
       # print("context 1: ",context)
        context["todo_list"] = ToDoList.objects.get(id=self.kwargs["list_id"])
       # print("context 2:", context)
        return context


class ToDoListCreate(CreateView):
  model = ToDoList
  template_name = "todoapp/add_todo.html"
  fields = [
    "title"
  ]

  def get_success_url(self):
      return reverse_lazy("index")


class ToDoTaskCreate(CreateView):
  model = ToDoEntry
  template_name = "todoapp/add_todo.html"
  fields = [
    "todo_title"
    "todo_list"
  ]

  def get_success_url(self):
      return reverse_lazy("index")




class TodoUpdateView(UpdateView):
  model = ToDoEntry
  context_object_name = 'todo'
  template_name = "todoapp/update_form.html"
  fields = [
    "todo_titel",
  ]

  def get_queryset(self):
    x =  ToDoEntry.objects.filter(todo_list_id=self.kwargs["list_id"])
   # print(x)
    return x

  def get_context_data(self):
        context = super().get_context_data()
       # print("context 1: ",context)
        context["todo_list"] = ToDoList.objects.get(id=self.kwargs["list_id"])
      #  print("context 2:", context)
        return context

  def get_success_url(self):
    context = super().get_context_data()
    context["todo_list"] = ToDoList.objects.get(id=self.kwargs["list_id"])
    x = ToDoList.objects.get(id=self.kwargs["list_id"])
    return reverse("todos",kwargs={"list_id":x.id})


class ToDoDeleteView(DeleteView):
  model = ToDoEntry

  def get_success_url(self):
    context = super().get_context_data()
    print("context1:", context)
    print
    context["todo_list"] = ToDoList.objects.get(id=self.kwargs["list_id"])

    print(context["todo_list"].id)
    return reverse("todos",kwargs={"list_id":context["todo_list"].id})
