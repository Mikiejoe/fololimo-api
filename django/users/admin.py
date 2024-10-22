from django.contrib import admin
from .models import User

admin.site.site_header = "FOLOLIMO"
admin.site.site_title = "FOLOLIMO ADMINSTRATION"
admin.site.index_title = "WELCOME TO FOLOLIMO ADMINSTRATION"
# admin.site


class UserAdmin(admin.ModelAdmin):
    list_display = ["username", "email", "firstname", "lastname"]


admin.site.register(User, UserAdmin)
