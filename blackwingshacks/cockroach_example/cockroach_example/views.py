from django.shortcuts import render
from .models import User

# Create your views here.
def user_page(request):
    #return render(request, 'user_info/page1.html')
    users = User.objects.all().order_by('baseSalary') #Grabs all records from Employee database table
    return render(request, 'cockroach_example/user_page.html', {'users' : users})
