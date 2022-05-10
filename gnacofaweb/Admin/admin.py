from django.contrib import admin
from .models import Staff

# Register your models here.
class StaffAdmin(admin.ModelAdmin):
    search_fields = ("staff_id",)


admin.site.register(Staff, StaffAdmin)