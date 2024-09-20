from django.urls import path
from . import views

app_name = 'myapp'

urlpatterns = [
    path('hello/<str:name>/', views.say_hello, name="hello"),
    path('time/', views.give_time, name="time"),
    path('tasks/', views.show_tasks, name="tasks"),
    path('add/', views.add_task, name="add"),
]