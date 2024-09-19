from django.contrib import admin
from .models import Create
# Register your models here.
admin.site.register(Create)
admin.site.site_header = "My Todo Site"
admin.site.site_title = "My todo" 
