from django.http import HttpResponseRedirect
from .models import Members
from django.shortcuts import render
from django.db.models import Q
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings
from django.contrib import messages
# from leave_management_system.settings import EMAIL_HOST_USER
# import ezgmail
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
    if request.method == 'POST':
        start_date = request.POST.get('start-date')
        end_date = request.POST.get('end-date')
        reason = request.POST.get('reason')

        send_mail(
            'Leave Request',
            f'Start Date: {start_date}\nEnd Date: {end_date}\nReason: {reason}',
            settings.EMAIL_HOST_USER,
            # 'kirtisikka972@gmail.com',
            ['kirtisikka972@gmail.com'],
            fail_silently=False,
            # auth_user=settings.EMAIL_HOST_USER,
            # auth_password=settings.EMAIL_HOST_PASSWORD,
           )

        messages.success(request, 'Your leave request has been submitted successfully!')

    return render(request, 'dashboard/leave_request.html')

    
def user(request, id):
    user = get_object_or_404(Members, id=id) 
    members = Members.objects.all()
    context = {'members': members, 'id': id}
    return render(request, 'dashboard/user.html', context)

   
