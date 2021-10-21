from usuarios.models import User
from django.db import models
from django.conf import settings
from ecomm.models import Product
from django.forms import ModelForm


class ServiceOrder(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='orderServices', on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    product = models.CharField(max_length=100)
    txService = models.CharField(max_length=3000)
    class Meta:
        ordering = ['-created_at',]

    def __str__(self):
        return '%s' % self.id


class Sugestion(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='orderSugestions', on_delete=models.CASCADE) 
    sugestao = models.CharField(max_length=2500, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-created_at',]
    def __str__(self): 
        return '%s' % self.id 
