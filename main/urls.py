from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('/profile', views.profile_settings, name='profile'),
    path('/<int:w_id>', include('workspace.urls')),
]
