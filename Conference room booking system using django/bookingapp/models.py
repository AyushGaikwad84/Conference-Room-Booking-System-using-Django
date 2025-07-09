# from xml.parsers.expat import model
from django.db import models

# Create your models here.
class useraccount(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique = True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class contactmsg(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    contact_number = models.CharField(max_length=12)
    contact_msg = models.TextField(max_length=255)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.submitted_at.strftime('%Y-%m-%d %H:%M')}"       # this msg will execute on admin site in contactmsg to identify user.
    

class room_booking(models.Model):
    name = models.CharField(max_length=100)
    room_title = models.CharField(max_length=50)
    room_capacity = models.CharField(max_length=200)
    email = models.EmailField()
    mbno = models.CharField(max_length=15)
    booking_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    extras = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.booking_date} ({self.start_time} - {self.end_time})"

