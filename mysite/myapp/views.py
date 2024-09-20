from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime

# Create your views here.
def say_hello(request, name):

    return render(request, "hello.html", context={"name": name})


def give_time(request):
    t = datetime.now()

    return HttpResponse(t)


def show_tasks(request):
    # for creating empty list the first time
    if "tasks" not in request.session:
        request.session["tasks"] = []


    return render(request, "tasks.html", context={"tasks": request.session["tasks"]})


def add_task(request):
    if request.method == "GET":
        return render(request, "add.html")


    elif request.method == "POST":
        t = request.POST["task"]
        request.session["tasks"].append(t)
        request.session.modified = True

        return redirect('myapp:tasks')