from django.contrib import admin
from card.models import Card


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ('company_name',)
    # fields = ('company_name', 'contact_name', 'mc_dot_number', 'number_or_trucks', 'fuel_cards_register',
    #           'mailing_address', 'address_line_2', 'city', 'state', 'zip_code', 'primary_contact_info',
    #           'title', 'phone_number', 'email_address', 'signage')
