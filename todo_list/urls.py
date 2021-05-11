from django.contrib import admin
from django.urls import path
# from django.urls.conf import include
from todos import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.todo_list, name='index'),
    # path('', views.index, name='index'),
    # path('todo-list/', include('todos.urls')),
]
