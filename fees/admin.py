from django.contrib import admin
from fees.models import Fee

class FeeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'email',
        'password',
    )

admin.site.register(Fee,FeeAdmin)
