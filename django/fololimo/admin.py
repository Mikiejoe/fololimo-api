from django.contrib import admin
from .models import Client, Tip, Region, City, SubCounty, Weather, Message


class ClientAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "location", "type")
    search_fields = ("name", "phone", "location", "type")
    list_filter = ("type",)


class WeatherAdmin(admin.ModelAdmin):
    list_display = (
        "city",
        "temperature",
        "description",
        "humidity",
        "min_temp",
        "max_temp",
        "pressure",
    )
    search_fields = (
        "city",
        "temperature",
        "description",
        "humidity",
        "min_temp",
        "max_temp",
        "pressure",
    )
    list_filter = ("city",)


admin.site.register(Tip)
admin.site.register(Client, ClientAdmin)
admin.site.register(Region)
admin.site.register(City)
admin.site.register(Message)
admin.site.register(SubCounty)
admin.site.register(Weather, WeatherAdmin)
