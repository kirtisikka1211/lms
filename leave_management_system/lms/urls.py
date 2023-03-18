from django.urls import path
from . import views
urlpatterns = [
    path('', views.members_list, name='members'),
    path('leave', views.leave_request, name='requests'),
    path('user/<int:member_id>/', views.user, name='member_detail'),
    
]