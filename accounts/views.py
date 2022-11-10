from datetime import datetime

from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .forms import RegisterForm, LoginForm
from .models import Attendance



def login_page(request):
    form = LoginForm(request.POST or None)

    if request.POST and form.is_valid():
        user = form.login(request)
        print(user)
        if user:
            login(request, user)
            return redirect('home_page')
    context = {
        "form": form
    }
    return render(request, 'auth/login.html', context)


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'auth/register.html'
    success_url = '../home'


def attendance(request):
    currentUser = request.user
    query = Attendance.objects.filter(user=currentUser, currentDate=datetime.today()).first()
    qs = Attendance.objects.filter(user=request.user)
    print(qs.count()) #gamitin nyo to pang count ng attendance nya
    # print(query.values('currentDate'))
    if query:
        return render(request, 'attendance/attendance.html', {'query': query, 'qs': qs})
    else:
        #dto ung part na mag ccreate ng attendance for today
        qs = Attendance.objects.create(user=currentUser, currentDate=datetime.today())
        qs.save()
        return render(request, 'attendance/attendance.html')


def clockIn(request):
    currentUser = request.user
    dateToday = datetime.today()
    query = Attendance.objects.filter(user=currentUser, currentDate=dateToday, timeIn=None, timeOut=None)
    if query.exists():
        query.update(timeIn=dateToday)
        return redirect('home_page')
    else:
        return redirect('home_page')

def clockOut(request):
    currentUser = request.user
    dateToday = datetime.today()
    query = Attendance.objects.filter(user=currentUser, currentDate=dateToday, timeOut=None)
    if query.exists():
        query.update(timeOut=dateToday)
        return redirect('home_page')
    else:
        return redirect('home_page')
