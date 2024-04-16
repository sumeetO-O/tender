from django.contrib import admin

# Register your models here.
from .models import Tender, OEM, TENDERER, BIDDER

admin.site.register(Tender)
admin.site.register(OEM)
admin.site.register(TENDERER)
admin.site.register(BIDDER)