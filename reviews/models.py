from __future__ import unicode_literals

from django.db import models

from developer.models import Developer

from product.models import Product
# Create your models here.


class reviews(models.Model):

    # review for product
    product = models.ForeignKey(Product, related_name='product')

    # Reviewer
    reviewer = models.ForeignKey(Developer, related_name='reviewer')

    # rating for product
    rating = models.IntegerField(default=0)

    # reviews for product
    reviews = models.TextField()

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
