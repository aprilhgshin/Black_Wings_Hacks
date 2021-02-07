from django.db import models

# Create your models here.
class User(models.Model):

    # define different fields:
    email = models.CharField(max_length=100) # can have arg max_length = 100
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

    def __str__(self):  #how it's going to look in admin and shell when retrieving Employee objects
        return self.email
