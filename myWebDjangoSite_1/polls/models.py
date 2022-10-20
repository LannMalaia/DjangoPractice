from django.db import models


# Create your models here.
class LoginTBL(models.Model):
    user_id = models.CharField(max_length=255)
    password = models.CharField(max_length=255)