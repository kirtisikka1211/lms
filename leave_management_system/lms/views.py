from django.http import HttpResponseRedirect
from .models import Members
from django.shortcuts import render
from django.db.models import Q
from .forms import NameForm
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
def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'dashboard/leave_request.html', {'form': form})
