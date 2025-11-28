from django.db import models


class Review(models.Model):

    COUNTRY_CODE_CHOICES = [
        ('+91', '+91'),
        ('+1', '+1'),
        ('+971', '+971'),
        ('+44', '+44'),
        ('+61', '+61'),
        ('+92', '+92'),
    ]

    COUNTRY_CHOICES = [
        ('India', 'India'),
        ('USA', 'USA'),
        ('UAE', 'UAE'),
        ('Canada', 'Canada'),
        ('UK', 'UK'),
        ('Australia', 'Australia'),
    ]


    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    whatsapp_country_code = models.CharField(max_length=5,choices=COUNTRY_CODE_CHOICES,
 default='+91')
    whatsapp_number = models.CharField(max_length=16)
    country = models.CharField(max_length=100, choices=COUNTRY_CHOICES, default='India')
    state = models.CharField(max_length=100)
    amazon_seller = models.CharField(max_length=3, choices=[('Yes','Yes'),('No','No')])
    brand_owner = models.CharField(max_length=3, choices=[('Yes','Yes'),('No','No')])
    brand = models.CharField(max_length=200, blank=True, null=True)
    asin = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.whatsapp_number}"


# Create your models here.
