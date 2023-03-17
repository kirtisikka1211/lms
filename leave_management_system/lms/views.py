from django.http import HttpResponse
from .models import Members
from django.shortcuts import render
# from .filters import OrderFilter
from django.db.models import Q
# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")
def members_list(request):
    members = Members.objects.all()
    # members = Members.objects.get(id=pk)
    # name=members.first_name.all()
    # mail= members.email.all()
    # gen=members.gender.all()
    # stat= members.status.all()
    # years=members.year.all()
    # myFilter= OrderFilter(request.GET, queryset= name)
    # name= myFilter.qs
    return render(request, 'dashboard/members_list.html', {'members': members})

def my_view(request):
    user = request.user
    context = {'user': user}
    return render(request, 'my_template.html', context)
def leave_request(request):
    return render(request, 'dashboard/leave_request.html')
