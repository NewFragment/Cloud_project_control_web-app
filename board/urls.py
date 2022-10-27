from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.board_task_list, name='board'),
    path('add-task', views.add_task, name='add-task'),
    path('sort_for_first', views.sort_first, name='sort_for_first'),
    path('sort_for_second', views.sort_second, name='sort_for_second'),
    path('sort_for_third', views.sort_third, name='sort_for_third'),
    path('delete-task/<int:pk>', views.delete_task, name='delete-task'),
    path('change-task', views.change_task, name='change-task'),
    path('add-file', views.add_file, name='add-file'),
    path('delete-file/<int:pk>', views.delete_file, name='delete-file'),
]
