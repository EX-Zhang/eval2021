from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(primary_key=True, max_length=255)
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    token = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'user'
