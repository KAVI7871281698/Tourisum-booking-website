from django.contrib import admin
from .models import register_page,package,booking
# Register your models here.
admin.site.register(register_page)
admin.site.register(package)
admin.site.register(booking)
