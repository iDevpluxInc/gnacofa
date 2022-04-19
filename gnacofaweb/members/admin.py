from django.contrib import admin
from .models import Member


class MemberAdmin(admin.ModelAdmin):
    search_fields = ("member_gfx__startswith", "first_name__startswith", )


# Register your models here.
admin.site.register(Member, MemberAdmin)
