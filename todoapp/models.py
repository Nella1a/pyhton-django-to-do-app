from tkinter import CASCADE
from django.db import models

# Create your models here.


class ToDoList(models.Model):
    title = models.CharField(max_length=30, unique=True)

    def __str__(self):
      return self.name

    class Meta:
      ordering = ["date_created"]


class ToDoEntry(models.Model):
  todo_titel = models.CharField(max_length=100)
  description = models.TextField
  todo_list = models.ForeignKey(ToDoList, on_delete=models.CASCADE)


  def __str__(self):
    return self.todo_titel
