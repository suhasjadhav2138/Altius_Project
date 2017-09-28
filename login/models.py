from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


class UserProfilename(models.Model):
    name = models.OneToOneField(User, primary_key=True)
    email = models.EmailField(max_length=50)
    contact = models.CharField(max_length=20)
    skill = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

class Document(models.Model):
    user = models.ForeignKey(User, null=True, blank=True)
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')
    def __unicode__(self):
        return unicode(self.docfile)
