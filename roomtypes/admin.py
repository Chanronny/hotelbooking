from django.contrib import admin

# Register your models here.
from .models import Roomtype

class RoomtypeAdmin(admin.ModelAdmin):
    list_display=('id','room_type','room_type_desc','roomtype_photo_main')
    list_display_links = ('id','room_type')
    search_fields = ('room_type',)
    list_per_page = 25

admin.site.register(Roomtype,RoomtypeAdmin)