# Generated by Django 3.1.6 on 2021-02-06 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100)),
                ('company', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('education', models.CharField(max_length=100)),
                ('yearsExp', models.IntegerField(default=0)),
                ('baseSalary', models.IntegerField(default=0)),
                ('bonuses', models.IntegerField(default=0)),
                ('gender', models.CharField(choices=[('female', 'Female'), ('male', 'Male'), ('nonbinary', 'Nonbinary'), ('trans', 'Transgender'), ('other', 'Other')], max_length=9)),
                ('race', models.CharField(choices=[('white', 'White'), ('black/afr', 'Black or African American'), ('amerInd/alaskaNat', 'American Indian or Alaska Native'), ('asian', 'Asian'), ('natHawaii/pacIsland', 'Native Hawaiian or Other Pacific Islander')], max_length=50)),
            ],
        ),
    ]