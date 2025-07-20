from django.contrib import admin
from urbanstay.models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'flat', 'boarder', 'booked_on')
    list_filter = ('booked_on', 'flat__city', 'flat__state')
    search_fields = ('flat__title', 'boarder__email')
    ordering = ('-booked_on',)

