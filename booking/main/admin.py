from django.contrib import admin
from .models import Room, Booking

# Register your models here.
class RoomAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'seat', 'deskription')
    list_display_links = ('title', 'price')
    search_fields = ('title','seat','price')

admin.site.register(Room, RoomAdmin)

class BookingAdmin(admin.ModelAdmin):
    list_display = ('room', 'start_date', 'end_date', 'user_name')
    search_fields = ('room', 'start_date', 'user_name')

admin.site.register(Booking, BookingAdmin)