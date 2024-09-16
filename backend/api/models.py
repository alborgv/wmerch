from django.db import models

class Merch(models.Model):

    name = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    price = models.CharField(max_length=255)
    stock = models.CharField(max_length=255)

    #fotos


    def __str__(self):
        return True