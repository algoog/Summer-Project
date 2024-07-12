# myapp/models.py

from django.db import models

class House(models.Model):
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)

    def __str__(self):
        return self.address

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    number = models.CharField(max_length=15)
    woonplaats = models.CharField(max_length=50)
    age = models.IntegerField()
    school = models.CharField(max_length=100)
    school_year = models.CharField(max_length=20)
    house = models.ForeignKey(House, on_delete=models.CASCADE, related_name='residents', null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
