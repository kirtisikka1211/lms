from django.http import HttpResponseRedirect
from .models import Members
from django.shortcuts import render
from django.db.models import Q
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import EmailMultiAlternatives
from leave_management_system.settings import EMAIL_HOST_USER
from django.contrib import messages
# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")
def members_list(request):
    members = Members.objects.all()
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
        mem = Members.objects.all()
        
        print(request.user.username)
        for member in mem:
            username = member.username 
            print(username)
            if username == request.user.username:
                # mentor = member.mentor
                email = member.mentoremail
                print(email)
        maillist= email.split(", ")
        print(maillist)
        msg = EmailMultiAlternatives('Leave request', f'Start Date: {start_date}\nEnd Date: {end_date}\nReason: {reason}', EMAIL_HOST_USER, maillist)
                
            
        if msg.send():
            messages.success(request, 'Leave request submitted successfully.')      
        else:
            messages.error(request, 'Leave request unsuccessful.')

    memb=Members.objects.all() 
    value= False
    val= False

    for det in memb:
        uname= det.username
        if uname==request.user.username:
            if det.year==2020 or det.year==2021:
                print(det.year)
                value= True
                
    dict= {"value": value, "val": val}

    return render(request, 'dashboard/leave_request.html', dict)   
def user(request, id):
    user = get_object_or_404(Members, id=id) 
    members = Members.objects.all()
    context = {'members': members, 'id': id}
    return render(request, 'dashboard/user.html', context)

   
