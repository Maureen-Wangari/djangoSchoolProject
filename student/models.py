from django.db import models

class Student (models.Model):
    first_name = models.CharField(max_length =20)
    last_name = models.CharField(max_length =20)
    email = models.EmailField()
    date_of_birth = models.DateField()
    code = models.PositiveSmallIntegerField()
    id_number = models.IntegerField()
    gender = models.CharField(max_length=15)
    country = models.CharField(max_length=28)

    class Teacher (models.Model):
     first_name = models.CharField(max_length =20)
     last_name = models.CharField(max_length =20)
     email = models.EmailField()
     date_of_birth = models.DateField()
     subject = models.CharField(max_length = 25)
     id_number = models.IntegerField()
     gender = models.CharField(max_length=15)
     country = models.CharField(max_length=28) 

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# Create your models here.
