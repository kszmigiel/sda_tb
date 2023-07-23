from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Car, Client, Rental


class RentalAdmin(ModelAdmin):
    ordering = ['-id']
    list_display = ['id', 'car', 'client', 'start_date', 'end_date']
    list_display_links = ['id']
    list_filter = ['car', 'client', 'start_date', 'end_date']
    search_fields = ['car']
    fieldsets = (
        (None, {
            'fields': ('car', 'client', 'price')
        }),
        ('Date', {
            'fields': ('start_date', 'end_date')
        }),

    )
    readonly_fields = ['price']




admin.site.register(Car)
admin.site.register(Client)
admin.site.register(Rental, RentalAdmin)
#admin.site.register(Rental)

