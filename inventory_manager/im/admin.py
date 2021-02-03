from django.contrib import admin
from .models import LdapDonation, LdapInventory

admin.site.register(LdapDonation)
admin.site.register(LdapInventory)
