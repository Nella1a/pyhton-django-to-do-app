from importlib.resources import path
from django.urls import URLPattern, path
from .views import AllListView, DetailListView, TodoUpdateView, ToDoDeleteView

urlpatterns = [
  path("", AllListView.as_view(), name="index"),
  path("<int:list_id>/", DetailListView.as_view(), name="todos"),
  path("<int:list_id>/item/<int:pk>", TodoUpdateView.as_view(), name="update"),
  path("<int:list_id>/item/<int:pk>/delete", ToDoDeleteView.as_view(), name="delete"),
]