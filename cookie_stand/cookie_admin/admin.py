from django.contrib import admin
from .models import Cookie

@admin.register(Cookie)
class CookieAdmin(admin.ModelAdmin) :
    list_displaty = ['location', 'minimum_customers_per_hour', 'maximum_customers_per_hour', 'average_cookies_per_sale']
