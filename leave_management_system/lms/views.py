from django.http import HttpResponseRedirect
from .models import Members
from django.shortcuts import render
from django.db.models import Q
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import EmailMultiAlternatives
from leave_management_system.settings import EMAIL_HOST_USER
from django.contrib import messages

def members_list(request):
    members = Members.objects.all()
    # memb=Members.objects.all() 
    value= False
    val= False

    for det in members:
        uname= det.username
        if uname==request.user.username:
            if det.year==2020 or det.year==2021:
                print(det.year)
                value= True
    return render(request, 'dashboard/members_list.html', {'members': members,"value": value, "val": val })
def my_view(request):
    user = request.user
    context = {'user': user}
    return render(request, 'my_template.html', context)

def leave_request(request):
    if request.method == 'POST':
            start_date = request.POST.get('start-date')
            end_date = request.POST.get('end-date')
            reason = request.POST.get('reason')
            mem = Members.objects.all()
            for member in mem:
                    username = member.username 
                    if username == request.user.username:
                        email = member.mentoremail
            maillist= email.split(", ")
            msg = EmailMultiAlternatives('Leave request', f'Start Date: {start_date}\nEnd Date: {end_date}\nReason: {reason}', EMAIL_HOST_USER, maillist)      
                  
            try:
                start_year, start_month, start_day = start_date.split('-')
                end_year, end_month, end_day = end_date.split('-')
                valid =False
                if end_year > start_year or (end_year == start_year and end_month > start_month):
                    valid = True
                elif end_year == start_year and end_month == start_month and end_day >= start_day:
                    valid = True
                else:
                    valid = False      
                if valid:
                    
                    if msg.send():
                        messages.success(request, 'Leave request submitted successfully.')      
                    else:
                        messages.error(request, 'Leave request unsuccessful.')
                else:
                    messages.error(request, "Please mention valid time period")
            except:
                messages.error(request, "Leave request unsuccessful, please give valid details.")



   

    return render(request, 'dashboard/leave_request.html')   
def user(request, id):
    user = get_object_or_404(Members, id=id) 
    members = Members.objects.all()
    context = {'members': members, 'id': id}
    
    return render(request, 'dashboard/user.html', context)
def approve(request):
    return render(request, 'dashboard/approve.html')


   
