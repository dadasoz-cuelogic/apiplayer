from __future__ import unicode_literals

from django.db import models

from product.models import Product

class Service(models.Model):
    # Service name
    name = models.CharField(max_length=200)

    # Service Descritpion
    description = models.TextField()

    # Product
    product = models.ForeignKey(Product, on_delete=models.CASCADE)



class Apis(models.Model):

    # Service as a parent
    # i.e AUTH -->Login,SignUp,ForgotPassword Api's
    service = models.ForeignKey(Service)

    # Api URl
    url = models.CharField(max_length=200)

    # Json data for table
    data = JSONField(null=True)

    # API request for method
    method = models.CharField(max_length=50)
