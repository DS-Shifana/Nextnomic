from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = [
            'full_name',
            'email',
            'whatsapp_country_code',
            'whatsapp_number',
            'country',
            'state',
            'amazon_seller',
            'brand_owner',
            'brand',
            'asin'
        ]
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name', 'required': True}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address', 'required': True}),
            'whatsapp_country_code': forms.Select(attrs={'class': 'form-control', 'required': True}),
            'whatsapp_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'WhatsApp Number', 'required': True}),
            'country': forms.Select(attrs={'class': 'form-control', 'required': True}),
            'state': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'State/Region', 'required': True}),
            'amazon_seller': forms.RadioSelect(choices=[('Yes','Yes'),('No','No')]),
            'brand_owner': forms.RadioSelect(choices=[('Yes','Yes'),('No','No')]),
            'brand': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Brand Name'}),
            'asin': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ASIN (Optional)'}),
        }

    def clean_whatsapp_number(self):
        number = self.cleaned_data.get('whatsapp_number')
        if not number.isdigit():
            raise forms.ValidationError("WhatsApp number should contain digits only.")
        if len(number) < 6 or len(number) > 15:
            raise forms.ValidationError("Enter a valid WhatsApp number length.")
        return number

    def clean_brand(self):
        brand_owner = self.cleaned_data.get('brand_owner')
        brand = self.cleaned_data.get('brand')
        if brand_owner == 'Yes' and not brand:
            raise forms.ValidationError("Brand name is required if you are a Brand Owner.")
        return brand
