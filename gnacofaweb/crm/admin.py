from django.contrib import admin
from .models import Members, Profile, Due, Loan

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    search_fields = ("staff_id",)
    
class MembersAdmin(admin.ModelAdmin):
    search_fields = ("gfxnumber",)


admin.site.register(Members, MembersAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Loan)
admin.site.register(Due)