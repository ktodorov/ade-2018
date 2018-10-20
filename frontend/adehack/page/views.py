from django.shortcuts import render

from .forms import addSupplierForm

from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views import generic
from .forms import addSupplierForm
from .models import Supplier
from bootstrap_modal_forms.mixins import PassRequestMixin


class AddSupplierView(PassRequestMixin, SuccessMessageMixin,
                     generic.CreateView):
    template_name = 'addsupplier.html'
    form_class = addSupplierForm
    success_message = 'Success: Supplier was added.'
    success_url = reverse_lazy('map')

def map(request):
    # form = addSupplierForm(request.POST or None)
    # if form.is_valid():
    #     supplier = form.cleaned_data['supplier']
    #     address = form.cleaned_data['address']

    # context = {'add_supplier_form': form, }
		
    return render(request, 'map.html', {})