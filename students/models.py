from django.db import models

class Student(models.Model):

    name = models.CharField(max_length=100)

    university_id = models.IntegerField(unique=True)

    id_number = models.IntegerField()

    mobile_number = models.CharField(max_length=10)

    address = models.CharField(max_length=150)

    date_of_birth = models.DateField()

    image = models.ImageField(upload_to='students/')

    def __str__(self):
        return self.name