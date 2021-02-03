# Generated by Django 3.1.5 on 2021-02-03 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('im', '0004_ldapdonation_ldapinventory'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Donation',
        ),
        migrations.DeleteModel(
            name='Inventory',
        ),
        migrations.AlterField(
            model_name='ldapdonation',
            name='item',
            field=models.CharField(db_column='cn', max_length=50),
        ),
        migrations.AlterField(
            model_name='ldapinventory',
            name='item',
            field=models.CharField(db_column='cn', default='item', max_length=50),
        ),
    ]
