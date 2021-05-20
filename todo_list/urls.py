from django.contrib import admin
from django.urls import path, include
# from django.urls.conf import include
from todos import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', views.index, name='index'),
    path('', views.todo_list, name='index'),
    path('delete_item/<int:pk>/', views.delete_item, name='delete_item'),
    path('update_item/<int:pk>/', views.update_item, name='update_item'),
    # path('todo-list/', include('todos.urls')),
]
