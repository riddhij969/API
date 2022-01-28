from django.db import models

# Create your models here.

class users(models.Model):
    # user_ID = models.IntegerField()
    first_name= models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    age = models.IntegerField()
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip = models.IntegerField()
    email = models.CharField(max_length=255)
    web = models.CharField(max_length=255)

    def __str__(self):
        return self.first_name
