from django.shortcuts import render

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Review

def review_form(request):
    if request.method == "POST":
        # Get form data
        full_name = request.POST.get("fullName")
        email = request.POST.get("email")
        whatsapp_country_code = request.POST.get("countryCode")
        whatsapp_number = request.POST.get("whatsappNumber")
        country = request.POST.get("country")
        state = request.POST.get("state")
        amazon_seller = request.POST.get("amazonSeller")
        brand_owner = request.POST.get("brandOwner")
        brand = request.POST.get("brand")
        asin = request.POST.get("asin")

        # Save to database
        review = Review.objects.create(
            full_name=full_name,
            email=email,
            whatsapp_country_code=whatsapp_country_code,
            whatsapp_number=whatsapp_number,
            country=country,
            state=state,
            amazon_seller=amazon_seller,
            brand_owner=brand_owner,
            brand=brand,
            asin=asin
        )

        # Redirect to success page with WhatsApp info
        return render(request, "reviewform/revsuccess.html", {
            "full_name": full_name,
            "whatsapp_number": whatsapp_number,
            "country_code": whatsapp_country_code
        })

    return render(request, "reviewform/reviewform.html")

def submitted(request):
    return render(request, "reviewform/revsuccess.html")
# Create your views here.
