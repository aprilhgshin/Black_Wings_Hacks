from django.shortcuts import render
from .models import Employee

# Create your views here.
def user_page(request):
    #return render(request, 'user_info/page1.html')
    employees = Employee.objects.all().order_by('baseSalary') #Grabs all records from Employee database table
    return render(request, 'user_data/user_page.html', {'employees' : employees})
