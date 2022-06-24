from importlib.resources import path
from django.urls import URLPattern, path
from todoapp.views import AllListView

urlpatterns = [
  path("", AllListView.as_view(), name="index")
]