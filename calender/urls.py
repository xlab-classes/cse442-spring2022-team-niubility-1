from django.conf.urls import url
from django.urls import path, re_path
from .views import *

urlpatterns = [

    url(r"^$", index, name="index"),
    url(r"^add_task$", add_task, name="add_task"),
]
