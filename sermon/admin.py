# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from sermon.models import SermonType, Content
import os

# Register your models here.
class ContentInline(admin.StackedInline):
    model = Content
    extra = 2

class SermonTypeAdmin(admin.ModelAdmin):
    inlines = [ContentInline]
    list_display = ('name', 'description')

class ContentAdmin(admin.ModelAdmin):
    # add 'audio_file_player' tag to your admin view
    list_display = ('title', 'upload_date')
    actions = ['custom_delete_selected']

    def custom_delete_selected(self, request, queryset):
        # custom delete code
        n = queryset.count()
        for i in queryset:
            if i.audio_file:
                if os.path.exists(i.audio_file.path):
                    os.remove(i.audio_file.path)
            i.delete()
        self.message_user(request, ("Successfully deleted %d audio files.") % n)

    custom_delete_selected.short_description = "Delete selected items"

    def get_actions(self, request):
        actions = super(ContentAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions


admin.site.register(SermonType, SermonTypeAdmin)
admin.site.register(Content, ContentAdmin)




