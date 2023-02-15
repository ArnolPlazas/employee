from django.contrib import admin
from .models import Employee, Skill


admin.site.register(Skill)

class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'department',
        'job',
        'full_name',
    )

    def full_name(self, obj):
        return obj.first_name + ' ' + obj.last_name

    search_fields = ('first_name',)
    list_filter = ('job', 'skills')
    filter_horizontal = ('skills', )  # solo para campos muchos a muchos
admin.site.register(Employee, EmployeeAdmin)