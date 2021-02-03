from django.utils import timezone
import ldapdb.models
from ldapdb.models.fields import fields

#LDAP DONATION
class LdapDonation(ldapdb.models.Model):
    """
    Class for representing an LDAP user entry.
    """
    # LDAP meta-data
    base_dn = "ou=donation,dc=birunisoft,dc=com"
    object_classes = ['']
    last_modified = fields.DateTimeField(db_column='modifyTimestamp', editable=False)

    # donation
    item = fields.CharField(db_column='cn', max_length=50)
    quantity = fields.IntegerField(db_column='itemQuantity', default=0)
    description = fields.TextField(db_column='itemDescription')
    date_donated = fields.DateTimeField(db_column='dateDonation', default=timezone.now)
    donor = fields.CharField(db_column='donorName', max_length=50)

    #return readable object upon query
    def __str__(self):
        return f'{self.donor}-{self.item}'

#LDAP INVENTORY
class LdapInventory(ldapdb.models.Model):
    """
    Class for representing an LDAP user entry.
    """
    # LDAP meta-data
    base_dn = "ou=inventory,dc=birunisoft,dc=com"
    object_classes = ['']
    last_modified = fields.DateTimeField(db_column='modifyTimestamp', editable=False)

    # inventory
    item = fields.CharField(db_column='cn', max_length=50, default='item')
    quantity = fields.IntegerField(db_column='itemQuantity', default=0)

    #return readable object upon query
    def __str__(self):
        return f'{self.item}'

##############################################################################################################

'''
# inetOrgPerson
first_name = fields.CharField(db_column='givenName', verbose_name="Prime name")
last_name = fields.CharField("Final name", db_column='sn')
full_name = fields.CharField(db_column='cn')
email = fields.CharField(db_column='mail')
phone = fields.CharField(db_column='telephoneNumber', blank=True)
mobile_phone = fields.CharField(db_column='mobile', blank=True)
photo = fields.ImageField(db_column='jpegPhoto')

# posixAccount
uid = fields.IntegerField(db_column='uidNumber', unique=True)
group = fields.IntegerField(db_column='gidNumber')
gecos = fields.CharField(db_column='gecos')
home_directory = fields.CharField(db_column='homeDirectory')
login_shell = fields.CharField(db_column='loginShell', default='/bin/bash')
username = fields.CharField(db_column='uid', primary_key=True)
password = fields.CharField(db_column='userPassword')
'''