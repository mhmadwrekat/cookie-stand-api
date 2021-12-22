from rest_framework import serializers
from .models import Cookie

class CookieSerializer(serializers.ModelSerializer) :
    class Meta :
        fields = ['location', 'minimum_customers_per_hour', 'maximum_customers_per_hour', 'average_cookies_per_sale']
        model = Cookie
