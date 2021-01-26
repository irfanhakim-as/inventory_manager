from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import (
    ListView
 )
from .models import Donation, Inventory
from .forms import DonationCreateForm

class DonationListView(ListView):
    model = Donation
    template_name = 'im/donation_list.html'
    context_object_name = 'donations'
    ordering = ['-pk']
    paginate_by=5

class InventoryListView(ListView):
    model = Inventory
    template_name = 'im/inventory_list.html'
    context_object_name = 'inventories'
    ordering = ['-pk']
    paginate_by=5

def makeDonation(request):
    if request.method == 'POST':
        form = DonationCreateForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.item = obj.item.lower()
            obj.save()
            donated_item = form.cleaned_data['item']
            print(donated_item)
            item = form.cleaned_data.get('item')
            name = form.cleaned_data.get('donor')
            quantity = form.cleaned_data.get('quantity')
            # feedback and redirect user
            messages.success(request, f'{name} has donated {donated_item} by {quantity}!')
            return redirect('im-home')
    else:
        form = DonationCreateForm()
    return render(request, 'im/donation_form.html', {'form' : form})