from django.db import models

# Create your models here.
class Roomtype(models.Model):
    room_type  = models.CharField(max_length=20) 
    room_type_desc = models.CharField(max_length=200)
    number_of_beds = models.IntegerField()
    roomtype_photo_main  = models.ImageField(upload_to='photos/')
    max_no_of_room_for_roomtype = models.IntegerField()
    standard_price = models.IntegerField()
    week_date_price = models.IntegerField()
    week_end_price = models.IntegerField()
    peak_season_price = models.IntegerField()
    special_price = models.IntegerField()
    with_breakfast_standard_price = models.IntegerField()
    with_breakfast_week_date_price = models.IntegerField()
    with_breakfast_week_end_price = models.IntegerField()
    with_breakfast_peak_season_price = models.IntegerField()
    with_breakfast_special_price = models.IntegerField()
    
    def __str__(self):
        return self.room_type