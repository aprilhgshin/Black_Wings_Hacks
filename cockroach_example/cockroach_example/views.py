from django.shortcuts import render
from django.http import HttpResponse
from .models import User

# Creating views here. Each view leads to a different web page.

def user_page(request): #user page url
    users = User.objects.all().order_by('baseSalary') #Grabs all records from Employee database table
    return render(request, 'cockroach_example/user_page.html', {'users' : users})


def homepage(request): #home page url
    return render(request, 'cockroach_example/homepage.html')


def about(request): #about url
    return render(request, 'cockroach_example/about.html')
