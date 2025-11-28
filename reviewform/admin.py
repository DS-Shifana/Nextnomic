from django.contrib import admin
from .models import Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'full_name', 
        'email', 
        'whatsapp_country_code', 
        'whatsapp_number', 
        'country', 
        'state', 
        'amazon_seller', 
        'brand_owner', 
        'brand', 
        'asin', 
        'created_at'
    )
    list_filter = ('country', 'state', 'amazon_seller', 'brand_owner', 'created_at')
    search_fields = ('full_name', 'email', 'whatsapp_number', 'brand', 'asin')
    ordering = ('-created_at',)

# Register your models here.
