from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def index(request):
    return render(request, "index.html", locals())


@login_required
def add_task(request):
    if request.method == "GET":
        return render(request, "add_task.html", locals())
    else:
        return render(request, "add_task.html", locals())
