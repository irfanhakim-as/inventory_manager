from django import forms
from .models import LdapDonation

class DonationCreateForm(forms.ModelForm):

    class Meta:
        model = LdapDonation
        fields = ['item', 'quantity', 'description', 'donor']
