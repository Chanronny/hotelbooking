from django.contrib import admin

# Register your models here.
from .models import Payment

class PaymentAdmin(admin.ModelAdmin):
    list_display=('roomType','numberOfRooms','fullName','email','checkInDate','checkOutDate')
    list_display_links = ('roomType','fullName','email',)
    search_fields = ('fullName',)
    list_per_page = 25

admin.site.register(Payment,PaymentAdmin)