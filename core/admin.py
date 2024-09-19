from django.contrib import admin
from .models import Create, Contact
# Register your models here.
admin.site.register(Create)
admin.site.register(Contact)
admin.site.site_header = "My Todo Site"
admin.site.site_title = "My todo" 
