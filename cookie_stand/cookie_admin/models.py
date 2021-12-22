from django.db import models
from django.contrib.auth import get_user_model

class Cookie(models.Model) :
    location = models.CharField(max_length = 20)
    minimum_customers_per_hour = models.IntegerField()
    maximum_customers_per_hour = models.IntegerField()
    average_cookies_per_sale = models.IntegerField()
    owner = models.ForeignKey(get_user_model(), default = None, on_delete = models.CASCADE)

    def __str__(self) :
        return self.location