from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.workspace_main, name='workspaces'),
    path('/change-workspace', views.workspace_change, name='change'),
    path('/delete-workspace', views.workspace_delete, name='delete_w'),
    path('/delete-board', views.board_delete, name='delete_b'),
    path('/change-user', views.user_permission_change, name='permissions'),
    path('/<int:b_id>/', include('board.urls')),
]