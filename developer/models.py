from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

def generate_filename(filename):
    url = "media/%s" % (filename)
    return url


class Developer(models.Model):

    dev_org_name = models.CharField(max_length=200)

    # creationDateTime is the time that the object was created
    creation_date_time = models.DateTimeField(
        auto_now=False, auto_now_add=True)

    # modifiedDateTime is the time the object was last edited
    modified_date_time = models.DateTimeField(
        auto_now=True, auto_now_add=False)

    # Prfile pic
    profile_pic = models.FileField(upload_to=generate_filename, null=True)

    user = models.ForeignKey(User, related_name='dev_user')
