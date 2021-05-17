from django.urls import path
from todos import views


urlpatterns = [
    path('', views.todo_list, name='todo-list'),
    path('delete_item/<int:pk>', views.deleteItem, name='deleteItem'),
    path('update_item/<int:pk>', views.updateItem, name='updateItem'),
]
