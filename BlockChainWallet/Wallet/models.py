# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Address(models.Model):
    username = models.CharField(primary_key=True, max_length=255)
    address = models.CharField(max_length=255)
    wallet = models.CharField(max_length=255)
    private = models.CharField(max_length=255)
    public = models.CharField(max_length=255)
    wif = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'address'
        unique_together = (('username', 'address', 'wallet'),)


class Wallet(models.Model):
    username = models.CharField(primary_key=True, max_length=255)
    wallet = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'wallet'
        unique_together = (('username', 'wallet'),)

