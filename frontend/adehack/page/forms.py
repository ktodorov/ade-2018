from django import forms
from .models import Supplier
from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin

class addSupplierForm(PopRequestMixin, CreateUpdateAjaxMixin, forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ['supplier', 'address']