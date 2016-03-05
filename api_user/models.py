from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


def generate_filename(filename):
    url = "media/%s" % (filename)
    return url

USER_TYPE = (
    (1, 'Admin'),
    (2, 'Organization'),
    (3, 'Developer'))


class API_USER(models.Model):

    user = models.OneToOneField(User)
    user_type = models.CharField(max_length=1, choices=USER_TYPE,default=3)
