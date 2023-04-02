from django.http import HttpResponseRedirect
from .models import Members, Leave
from django.shortcuts import render
from django.db.models import Q
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import EmailMultiAlternatives
from leave_management_system.settings import EMAIL_HOST_USER
from django.contrib import messages


def members_list(request):
    members = Members.objects.all()
    value = False
    val = False
    # print(request.user.id)

    for det in members:
        uname = det.username
        if uname == request.user.username:
            if det.year == 2020 or det.year == 2021:
                print(det.year)
                value = True
    return render(request, 'dashboard/members_list.html', {'members': members, "value": value, "val": val})


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
        maillist = email.split(", ")
        msg = EmailMultiAlternatives(
            'Leave request', f'Start Date: {start_date}\nEnd Date: {end_date}\nReason: {reason}', EMAIL_HOST_USER, maillist)

        try:
            start_year, start_month, start_day = start_date.split('-')
            end_year, end_month, end_day = end_date.split('-')
            valid = False
            if end_year > start_year or (end_year == start_year and end_month > start_month):
                valid = True
            elif end_year == start_year and end_month == start_month and end_day >= start_day:
                valid = True
            else:
                valid = False
            if valid:

                if msg.send():

                    messages.success(
                        request, 'Leave request submitted successfully.')
                    for members in mem:
                        username = members.username
                        if username == request.user.username:
                            members.req_sent = True
                            members.save(update_fields=['req_sent'])
                            leave_req = Leave(
                                start_date=start_date, end_date=end_date, reason=reason, user_id=members.user_id)
                            leave_req.save()

                else:
                    messages.error(request, 'Leave request unsuccessful.')
            else:
                messages.error(request, "Please mention valid time period")
        except:
            messages.error(
                request, "Leave request unsuccessful, please give valid details.")

    return render(request, 'dashboard/leave_request.html')


def user(request, id):
    user = get_object_or_404(Members, id=id)
    members = Members.objects.all()
    context = {'members': members, 'id': id}

    return render(request, 'dashboard/user.html', context)


def approve(request):
    requests= Leave.objects.all()
    members= Members.objects.all()
    for member in members:
        if request.user.username== member.username:
            mentees= member.mentee
    mentee_list = mentees.split(", ")
    print(mentee_list)
    dict={}
    for mem in members:
        for mentee_name in mentee_list:
            if mem.first_name == mentee_name:
                for req in requests:
                    if mem.user_id == req.user_id:
                        dict[mentee_name]=req.user_id
    print(dict)
                        # print(mem.username)
                        # print(mem.user_id)
                        # print(req.user_id)
                        # print(req.start_date)
                        # print(req.end_date)
                        # print(req.reason)
                        # print(req.status)
                        # if request.method == 'POST':
                        #     if 'approve' in request.POST:
                        #         req.status = True
                        #         req.save(update_fields=['status'])
                        #         messages.success(request, 'Leave request approved.')
                        #         return HttpResponseRedirect(request.path_info)
                        #     elif 'reject' in request.POST:
                        #         req.status = False
                        #         req.save(update_fields=['status'])
                        #         messages.success(request, 'Leave request rejected.')
                        #         return HttpResponseRedirect(request.path_info)

    return render(request, 'dashboard/approve.html', {'members': members, 'requests': requests, 'dict': dict})
