from django.http import HttpResponse
from django.shortcuts import render

def homepage(request): #home page url
    #return HttpResponse("homepage")
    return render(request, 'homepage.html')


def about(request): #about url
    #return HttpResponse("about")
    return render(request, 'about.html')
