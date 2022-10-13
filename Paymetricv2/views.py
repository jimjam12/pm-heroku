from urllib import request

from django.shortcuts import render, redirect
from .forms import ContactForm
from django.db.models.query_utils import Q
from django.contrib.auth import get_user_model

User = get_user_model()


def startup(request):
    return render(request, "startup.html")


def home_page(request):
    if request.user.is_authenticated:
        return render(request, "home/home_page.html")
    else:
        return redirect('login')


def contact(request):
    contact_form = ContactForm(request.POST or None)

    context = {
        'form': contact_form

    }

    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    return render(request, "contact/contact.html", context)


def list_user(request):
    if 'q' in request.GET:
        q = request.GET['q']
        multiple_q = Q(Q(email__icontains=q) | Q(first_name__icontains=q) | Q(last_name__icontains=q) | Q(
            middle_name__icontains=q))
        data = User.objects.filter(multiple_q)
        model = data.values()

    else:
        model = User.objects.all().values()
        q = ""
    context = {
        'model': model,
        'q': q
    }
    return render(request, 'admin/list_user.html', context)


def update(request, id):
    user = User.objects.get(id=id)
    context = {
        'user': user
    }
    return render(request, 'auth/update.html', context)


def delete(request, id):
    user = User.objects.get(id=id)
    user.delete()
    return redirect('list_user')


def updaterecord(request, id):
    newEmail = request.POST['email']
    newFirstName = request.POST['first_name']
    user = User.objects.get(id=id)
    user.email = newEmail
    user.first_name = newFirstName
    user.save()
    return redirect('list_user')

def attendance(request):
    return render(request, "attendance/attendance.html")

def detailed(request):
    return render(request, "detailed/detailed.html")