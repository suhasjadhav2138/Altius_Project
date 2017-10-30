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


class Search_details(models.Model):
    user = models.ForeignKey(User, null=True, blank=True)
    run_id = models.CharField(max_length=3)
    date_pulled = models.CharField(max_length=15)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    email_original = models.EmailField(max_length=30)
    company_url = models.CharField(max_length=30)
    email_guess = models.CharField(max_length=30)
    email_score = models.CharField(max_length=3)


