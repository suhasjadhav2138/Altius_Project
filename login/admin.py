# -*- coding: utf-8 -*-
from .models import UserProfilename, Document, Search_details
from django.contrib import admin

admin.site.register(UserProfilename)
admin.site.register(Document)
admin.site.register(Search_details)