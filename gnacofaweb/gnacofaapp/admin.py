from django.contrib import admin
from .models import Archieve, Event, Announcement, News

class EventAdmin(admin.ModelAdmin):
    search_fields = ("title",)


class AnnouncementAdmin(admin.ModelAdmin):
    search_fields = ("title",)


class NewsAdmin(admin.ModelAdmin):
    search_fields = ("title",)


class ArchieveAdmin(admin.ModelAdmin):
    search_fields = ("title",)


# Register your models here.
admin.site.register(Event, EventAdmin)
admin.site.register(Announcement, AnnouncementAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Archieve, ArchieveAdmin)
