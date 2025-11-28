from django.shortcuts import render, redirect
from django.conf import settings
from .models import Adsform
import os


def ad_form(request):
    if request.method == "POST":
        # Collect form data
        full_name = request.POST.get("fullName")
        email = request.POST.get("email")
        whatsapp_country_code = request.POST.get("countryCode")
        whatsapp_number = request.POST.get("whatsappNumber")
        country = request.POST.get("country")
        state = request.POST.get("state")
        amazon_seller = request.POST.get("amazonSeller")
        ad_manager = request.POST.get("adManager")   
        brand_owner = request.POST.get("brandOwner")
        brand = request.POST.get("brand")
        asin = request.POST.get("asin")

        # Save to DB
        Adsform.objects.create(
            full_name=full_name,
            email=email,
            whatsapp_country_code=whatsapp_country_code,
            whatsapp_number=whatsapp_number,
            country=country,
            state=state,
            amazon_seller=amazon_seller,
            ad_manager=ad_manager,   
            brand_owner=brand_owner,
            brand=brand,
            asin=asin
        )

        # Redirect to success page
        return redirect('success')

    return render(request, "adform/index.html")


def success(request):
    return render(request, "adform/success.html")