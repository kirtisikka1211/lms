from django.urls import path
from . import views
urlpatterns = [
    path('', views.members_list, name='members'),
    path('leave', views.leave_request, name='requests'),
]