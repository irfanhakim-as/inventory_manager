from django.urls import path
from .views import (
    DonationListView,
    InventoryListView
 )
from . import views as im_views

urlpatterns = [
    path('', DonationListView.as_view(), name='im-home'),
    path('inventory/', InventoryListView.as_view(), name='inventory-home'),
    path('donate/', im_views.makeDonation, name='donate'),
]