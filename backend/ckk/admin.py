from django.contrib import admin

from . import models

admin.site.register(models.CKKItem)
admin.site.register(models.CKKImage)
admin.site.register(models.Upload)