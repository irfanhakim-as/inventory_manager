from django import forms
from .models import Donation

class DonationCreateForm(forms.ModelForm):

    class Meta:
        model = Donation
        fields = ['item', 'quantity', 'description', 'donor']
