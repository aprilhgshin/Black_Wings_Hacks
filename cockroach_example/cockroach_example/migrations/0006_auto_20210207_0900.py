# Generated by Django 3.1.6 on 2021-02-07 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cockroach_example', '0005_auto_20210207_0858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='baseSalary',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='bonuses',
            field=models.IntegerField(default=0),
        ),
    ]