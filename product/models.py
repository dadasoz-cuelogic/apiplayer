from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User
from organization.models import Organization

PRODUCT_TYPE = ((1, 'Private'), (2, 'Public'))

class Catagory(models.Model):
    # Catagory name
    name = models.CharField(max_length=200)

    # To set catagory active
    is_active = models.BooleanField(default=True)

    # To marked as deleted
    is_deleted = models.BooleanField(default=False)

    # creationDateTime is the time that the object was created
    creation_date_time = models.DateTimeField(
        auto_now=False, auto_now_add=True)

    # modifiedDateTime is the time the object was last edited
    modified_date_time = models.DateTimeField(
        auto_now=True, auto_now_add=False)


class Product(models.Model):
    # Catagory name
    name = models.CharField(max_length=200)

    # product URl
    url = models.CharField(max_length=200, null=False, blank=True)

    # To set catagory active
    is_active = models.BooleanField(default=True)

    # To marked as deleted
    is_deleted = models.BooleanField(default=False)

    # creationDateTime is the time that the object was created
    creation_date_time = models.DateTimeField(
        auto_now=False, auto_now_add=True)

    # modifiedDateTime is the time the object was last edited
    modified_date_time = models.DateTimeField(
        auto_now=True, auto_now_add=False)

    # Product Descritpion
    description = models.TextField()

    # Product Type
    product_type = models.IntegerField(choices=PRODUCT_TYPE, default=1)

    # Product Catagory
    catagory = models.ForeignKey(Catagory, on_delete=models.CASCADE, related_name='catagory')

    # Product Owner
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='organization')

    # Product_key
    product_key = models.CharField(null=True, max_length=32, unique=True, db_index=True)
