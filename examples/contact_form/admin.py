from django.contrib import admin

from . import models


class AttachmentInline(admin.StackedInline):
    model = models.Attachment
    extra = 0

@admin.register(models.Message)
class MessageAdmin(admin.ModelAdmin):
    inlines = [AttachmentInline]
