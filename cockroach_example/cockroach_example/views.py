from django.shortcuts import render
from django.http import HttpResponse
from .models import User

# Create your views here.
def user_page(request):
    #return render(request, 'user_info/page1.html')
    users = User.objects.all().order_by('baseSalary') #Grabs all records from Employee database table
    return render(request, 'cockroach_example/user_page.html', {'users' : users})


def homepage(request): #home page url
    #return HttpResponse("homepage")
    return render(request, 'cockroach_example/homepage.html')


def about(request): #about url
    #return HttpResponse("about")
    return render(request, 'cockroach_example/about.html')
