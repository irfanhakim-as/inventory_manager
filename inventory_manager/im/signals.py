from django.db.models.signals import post_save
from .models import LdapDonation, LdapInventory
from django.dispatch import receiver

@receiver(post_save, sender=LdapDonation)
def update_inventory(sender, instance, created, **kwargs):
    donated_item = instance.item
    donated_quantity = instance.quantity
    item_in_inventory = LdapInventory.objects.filter(item=donated_item)

    if item_in_inventory.exists():
        inventory_item_object = LdapInventory.objects.get(item=donated_item)
        print('IF STATEMENT')
        print('DONATED QUANTITY', donated_quantity)
        print('inventory_item_object.quantity BEFORE',inventory_item_object.quantity)
        inventory_item_object.quantity += donated_quantity
        inventory_item_object.save()
        print('inventory_item_object.quantity AFTER',inventory_item_object.quantity)
    else:
        print('ELSE STATEMENT')
        new_object = LdapInventory.objects.create(item=donated_item, quantity=donated_quantity)
        new_object.save()
