from django.contrib import admin

from .models import Contact
# Register your models here.

admin.site.site_title = "CEDROUSEROLL"
admin.site.site_header = "Cedrouseroll's Profile"
admin.site.register(Contact)
