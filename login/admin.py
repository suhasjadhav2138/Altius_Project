# -*- coding: utf-8 -*-
from .models import UserProfilename, Document, Search_details
from django.contrib import admin


# class UserSessionAdmin(admin.ModelAdmin):
#     meta=UserSession
#     list_display = ("ip","location")

admin.site.register(UserProfilename)
admin.site.register(Document)
admin.site.register(Search_details)
# admin.site.register(UserSession, UserSessionAdmin)