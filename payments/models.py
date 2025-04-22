from django.db import models

# Create your models here.
class Payment(models.Model):
    roomType  = models.CharField(max_length=20) 
    numberOfRooms = models.IntegerField()
    fullName = models.CharField(max_length=200)
    phoneNo  = models.CharField(max_length=20) 
    email  = models.CharField(max_length=100,default='',blank=True)
    creditCardType = models.CharField(max_length=20) 
    creditCard = models.CharField(max_length=20) 
    validThru = models.CharField(max_length=20) 
    CVC = models.CharField(max_length=20) 
    checkInDate = models.DateField()
    checkOutDate = models.DateField()
    totalPrice = models.IntegerField()
        
    def __str__(self):
        return self.fullName