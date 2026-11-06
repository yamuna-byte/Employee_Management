from django.contrib import admin
from .models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'position', 'department')
    search_fields = ('name', 'email')
    list_filter = ('department', 'position')

admin.site.register(Employee, EmployeeAdmin)