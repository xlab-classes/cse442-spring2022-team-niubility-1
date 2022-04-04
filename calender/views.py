from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Task
# Create your views here.
import time
from datetime import date, timedelta
@login_required
def index(request):
    user = request.user
    date_list = []
    result = []
    for i in range(8):
        date_list.append((date.today() + timedelta(days=i)).strftime("%Y-%m-%d"))
    for i in range(len(date_list)-1):
        # tasks = Task.objects.filter(begin__range=(date_list[i], date_list[i+1]))
        tasks = Task.objects.filter(user=user, begin__gte=date_list[i], begin__lt=date_list[i+1])
        tmp = [date_list[i]]
        for i in range(0,24):
            tmp.append("")
        for task in tasks:
            index = int(task.begin_time.split(":")[0])
            tmp[index+1] = tmp[index+1] + "\n" + task.name
        result.append(tmp)

    ar2 = list(map(list,zip(*result)))
    heads = [""]
    heads.extend(ar2[0])
    for i in range(0,24):
        print("=====")
        print(i)
        print(ar2[i+1])
        print(str(i) + ":00~" + str(i+1) + ":00")
        tmp_list = ar2[i+1].copy()
        new_list = [str(i) + ":00~" + str(i+1) + ":00"]
        new_list.extend(tmp_list)
        print(new_list)
        ar2[i+1] = new_list
        print(ar2[i+1])
    result = ar2
    del result[0]
    print(result)
    return render(request, "index.html", locals())


@login_required
def add_task(request):
    user = request.user
    if request.method == "GET":
        return render(request, "add_task.html", locals())
    else:

        name = request.POST.get("name")
        begin = request.POST.get("begin")
        # end = request.POST.get("end")
        priority = request.POST.get("priority")
        print(name)
        print(begin)
        # print(end)
        print(priority)
        task = Task()
        try:
            db_begin = str(begin).strip().split(" ")
            begin_date = db_begin[0].split("-")
            print(begin_date)
            begin_date.reverse()
            print(begin_date)
            begin_date = "-".join(begin_date)
            print(begin_date)
            begin_time = db_begin[-1]
            begin_time.split(":")[1]
            task.begin = begin_date
            task.begin_time = begin_time
        except Exception as e:
            print(e)
            msg = "begin params error!"
            return render(request, "add_task.html", locals())

        # try:
        #     db_begin = str(end).strip().split(" ")
        #     begin_date = db_begin[0].split("-")
        #     begin_date.reverse()
        #     begin_date = "-".join(begin_date)
        #     begin_time = db_begin[-1]
        #     begin_time.split(":")[1]
        #     task.end = begin_date
        #     task.end_time = begin_time
        # except Exception as e:
        #     print(e)
        #     msg = "end params error!"
        #     return render(request, "add_task.html", locals())
        try:
            priority = int(priority)
            task.priority = priority
        except Exception as e:
            print(e)
            msg = "priority params error!"
            return render(request, "add_task.html", locals())
        if name == "":
            msg = "name params error!"
            return render(request, "add_task.html", locals())
        task.name = name
        task.user = user
        task.save()
        return redirect("/")

def history(request):
    user = request.user
    all_task = Task.objects.filter(user=user)
    for task in all_task:
        print(task)
    return render(request, "history.html", locals())