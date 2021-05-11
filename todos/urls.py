from django.urls import path
from todos import views


urlpatterns = [
    path('', views.todo_list, name='todo-list'),
]
