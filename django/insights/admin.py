from django.contrib import admin

from .models import Farm, Activity


class FarmAdmin(admin.ModelAdmin):
    list_display = ["name", "location", "size"]


class ActivityAdmin(admin.ModelAdmin):
    list_display = ["activity", "date", "cost", "duration", "farm", "status"]


admin.site.register(Farm, FarmAdmin)
admin.site.register(Activity, ActivityAdmin)
