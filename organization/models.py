from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from api_user.models import API_USER

def generate_filename(filename):
    url = "media/%s" % (filename)
    return url


class Developer(models.Model):

    org_name = models.CharField(max_length=200)

    # organization URl
    org_url = models.CharField(max_length=200, null=False, blank=True)

    # creationDateTime is the time that the object was created
    creation_date_time = models.DateTimeField(
        auto_now=False, auto_now_add=True)

    # modifiedDateTime is the time the object was last edited
    modified_date_time = models.DateTimeField(
        auto_now=True, auto_now_add=False)

    # logo
    logo = models.FileField(upload_to=generate_filename)

    # Org details
    user = models.ForeignKey(API_USER)
