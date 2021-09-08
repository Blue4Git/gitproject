from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50, null=True, blank=False)
    email = models.EmailField(max_length=50, null=True, blank=False)
    city = models.CharField(max_length=30, null=True, blank=False)

    def __str__(self):
        return self.name