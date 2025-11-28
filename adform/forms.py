from django import forms
from .models import Adsform


class AdsformForm(forms.ModelForm):
    class Meta:
        model = Adsform
        fields = [
            "full_name",
            "email",
            "whatsapp_country_code",
            "whatsapp_number",
            "country",
            "state",
            "amazon_seller",
            "ad_manager",
            "brand_owner",
            "brand",
            "asin",
        ]

        widgets = {
            "full_name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "whatsapp_country_code": forms.TextInput(attrs={"class": "form-control"}),
            "whatsapp_number": forms.TextInput(attrs={"class": "form-control"}),
            "country": forms.TextInput(attrs={"class": "form-control"}),
            "state": forms.TextInput(attrs={"class": "form-control"}),

            "amazon_seller": forms.Select(attrs={"class": "form-select"}),
            "ad_manager": forms.Select(attrs={"class": "form-select"}),
            "brand_owner": forms.Select(attrs={"class": "form-select"}),

            "brand": forms.TextInput(attrs={"class": "form-control"}),
            "asin": forms.TextInput(attrs={"class": "form-control"}),
        }

    def clean(self):
        cleaned_data = super().clean()
        brand_owner = cleaned_data.get("brand_owner")
        brand = cleaned_data.get("brand")

        # If brand_owner = "Yes", brand is required
        if brand_owner == "Yes" and not brand:
            self.add_error("brand", "Brand name is required when brand owner is Yes.")

        return cleaned_data
