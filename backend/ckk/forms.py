from django import forms

from .models import CKKItem, CKKImage

class CKKForm(forms.ModelForm):
    class Meta:
        model = CKKItem
        fields = ['sku','price','description','link']
