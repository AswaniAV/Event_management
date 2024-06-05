from django.db import models

# Create your models here.
class Event(models.Model):
    img = models.ImageField(upload_to="pics")
    name = models.CharField(max_length=100)
    des = models.TextField()


    def __str__(self):
        return self.name

class Booking(models.Model):
    customer_name = models.CharField(max_length=100)
    customer_phone = models.CharField(max_length=100)
    name = models.ForeignKey(Event, on_delete= models.CASCADE)
    book_date = models.DateField()
    book_on = models.DateField(auto_now_add=True)     

class feedback(models.Model):
    customer_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)  
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return f"{self.customer_name} - {self.subject}"




