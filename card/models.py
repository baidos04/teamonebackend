from django.db import models


class Card(models.Model):
    company_name = models.CharField(max_length=155)
    contact_number = models.CharField(max_length=100, blank=False, null=False)
    mc_dot_number = models.CharField(max_length=155, blank=False, null=False)
    number_or_trucks = models.CharField(max_length=100, blank=False, null=False)
    fuel_cards_register = models.CharField(max_length=100, blank=False, null=False)
    mailing_address = models.CharField(max_length=100, blank=False, null=False)
    address_line_2 = models.CharField(max_length=100, blank=False, null=False)
    city = models.CharField(max_length=100, blank=False, null=False)
    state = models.CharField(max_length=100, blank=False, null=False)
    zip_code = models.CharField(max_length=100, blank=False, null=False)
    primary_contact_info = models.CharField(max_length=100, blank=False, null=False)
    title = models.CharField(max_length=100, blank=False, null=False)
    phone_number = models.CharField(max_length=100, blank=False, null=False)
    email_address = models.EmailField(max_length=170, blank=False, null=False)
    file = models.FileField(upload_to='files/')
    signature = models.ImageField(upload_to='signature/')

    def __str__(self):
        return self.company_name
