from django.contrib import admin

from . import models


@admin.register(models.Attachment)
class AttachmentAdmin(admin.ModelAdmin):
    pass
