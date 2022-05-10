from django.contrib import admin
from .models import Member


class MemberAdmin(admin.ModelAdmin):
    list_display = ('id','region', 'district', 'society', 'title','first_name','last_name', 'middle_name','preferred_name', 'gender','date_of_birth','address','telephone','educational_level','hometown','id_type','marriage_status', 'author')
    ordering = ('id',)
    search_fields = ("member_gfx__startswith", "first_name__startswith", )


# Register your models here.
admin.site.register(Member, MemberAdmin)
