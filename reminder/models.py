from django.db import models

class Position(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title



class Employee(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    picture = models.ImageField(null=True)
    date_of_birth = models.DateField()
    position = models.ForeignKey(Position, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} {self.surname}"