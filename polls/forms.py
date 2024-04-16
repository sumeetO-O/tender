from dataclasses import fields
from django.forms import ModelForm
from .models import Tender

class TenderForm(ModelForm):
    class Meta:
        model = Tender
        fields = '__all__'  