from django.db import models

class Voter(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    birthdate = models.Field('birthdate')
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=7)
    email = models.EmailField()
    phone = models.IntegerField()
    #ip = models.GenericIPAddressField(_(""), protocol="both", unpack_ipv4=False)