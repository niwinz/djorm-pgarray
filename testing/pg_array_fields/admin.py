# -*- coding: utf-8 -*-

from django.contrib import admin

from . import models


class Admin(admin.ModelAdmin):
    pass

admin.site.register(models.IntModel, Admin)
admin.site.register(models.DoubleModel, Admin)
