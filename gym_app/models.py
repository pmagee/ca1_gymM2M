from django.db import models
from django.urls import reverse

class Gym(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Member(models.Model):
    gym = models.ForeignKey(Gym, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    membership_start_date = models.DateField()

    def __str__(self):
        return self.name
    
    


class Equipment(models.Model):
    name = models.CharField(max_length=100)
    gyms = models.ManyToManyField(Gym)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('equip_detail', args=[str(self.id)])