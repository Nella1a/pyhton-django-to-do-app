from django.contrib import admin
from todoapp.models import ToDoEntry, ToDoList

# Register your models here.

admin.site.register([ToDoList, ToDoEntry])