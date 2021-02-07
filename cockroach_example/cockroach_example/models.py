from django.db import models

'''
The User class is a Model containing instances for each user input as well unique identification:

id          - unique integer primary key assigned to each user
email       - string value
company     - string value of current company of user
title       - string value of job title
education   - string value of degree of education i.e. bachelors, masters, etc.
yearsExp    - int value of number of years of work experience
baseSalary  - int value of base salary of current job
bonuses     - int value of bonuses from current company
gender      - string value selected from one of five provided choices
race        - string value selected from one of five provided choices
'''

class User(models.Model):

    id = models.IntegerField(default=0)
    email = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    education = models.CharField(max_length=100)
    yearsExp = models.IntegerField(default=0)
    baseSalary = models.IntegerField(default=0)
    bonuses = models.IntegerField(default=0)

    gender_categories = (
        ('female', 'Female'),
        ('male', 'Male'),
        ('nonbinary', 'Nonbinary'),
        ('trans', 'Transgender'),
        ('other', 'Other'),
    )

    gender = models.CharField(max_length=9, choices=gender_categories)

    race_categories = (
        ('white', 'White'),
        ('black/afr', 'Black or African American'),
        ('amerInd/alaskaNat', 'American Indian or Alaska Native'),
        ('asian', 'Asian'),
        ('natHawaii/pacIsland', 'Native Hawaiian or Other Pacific Islander'),
    )
    race = models.CharField(max_length=50, choices=race_categories)

    def __str__(self):  #How it's going to look in admin and shell when retrieving Employee objects
        return self.email
