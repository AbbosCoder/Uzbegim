from django.contrib import admin
from .models import Xabar

@admin.register(Xabar)
class XabarAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone_number', 'created_at']  # Columns to display in the admin panel
    list_filter = ['created_at']  # Filters to quickly find messages by date
