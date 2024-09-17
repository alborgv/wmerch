from django.db import models

class Merch(models.Model):

    id = models.AutoField(primary_key=True, blank=True)
    name = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=500, blank=True)
    price = models.CharField(max_length=255, blank=True)
    stock = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name

class MerchPhoto(models.Model):
    merch = models.ForeignKey(Merch, related_name='photos', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='merch_photos/') 
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.merch.name

class Contact(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True)
    email = models.CharField(max_length=500, blank=True)
    phone = models.CharField(max_length=255, blank=True)
    message = models.CharField(max_length=1000, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name
    

class Subscription(models.Model):

    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.email