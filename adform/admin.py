from django.contrib import admin
from .models import Adsform


@admin.register(Adsform)
class AdsformAdmin(admin.ModelAdmin):
    list_display = (
        "full_name",
        "email",
        "whatsapp_country_code",
        "whatsapp_number",
        "country",
        "amazon_seller",
        "ad_manager",
        "brand_owner",
        "created_at",
    )

    list_filter = (
        "country",
        "amazon_seller",
        "ad_manager",
        "brand_owner",
        "created_at",
    )

    search_fields = (
        "full_name",
        "email",
        "whatsapp_number",
        "brand",
        "asin",
    )

    ordering = ("-created_at",)
