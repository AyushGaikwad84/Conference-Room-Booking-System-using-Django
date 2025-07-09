from django.contrib import admin
from .models import contactmsg, room_booking, useraccount

# Register your models here.

# admin.site.register(contactmsg)
@admin.register(contactmsg)
class ContactMsgAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'contact_number', 'submitted_at')

@admin.register(useraccount)
class useraccount_signup_admin(admin.ModelAdmin):
    list_display = ('name', 'email', 'password')

@admin.register(room_booking)
class room_booking_admin(admin.ModelAdmin):
    list_display = ('name','email','room_title','room_capacity','mbno','booking_date','start_time','end_time','extras','created_at')