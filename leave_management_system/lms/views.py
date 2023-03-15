from django.http import HttpResponse
from .models import Members
from django.shortcuts import render

# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")
def members_list(request):
    members = Members.objects.all()
    return render(request, 'dashboard/members_list.html', {'members': members})
# views.py

