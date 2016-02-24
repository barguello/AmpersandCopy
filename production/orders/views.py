from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django import forms
import order_parser_and_saver
import os

from production.models import Order
from production.orders.forms import OrderFilterForm, OrderFormset
from production.views import SessionFilterListView


class FileForm(forms.Form):
    name = forms.FileField(label="Choose an Order Report File to Upload");

class order_import(TemplateView):
    template_name = 'orders_index.html'
    def post(self, request, *args, **kwargs):
        if self.request.POST:
            context = self.get_context_data()
            file_name = self.request.FILES['name']
            data_file_path = default_storage.save('data.csv',
                                                  ContentFile(file_name.read()))
            if context["form"].is_valid():
                status = order_parser_and_saver.save_orders(data_file_path)
                os.remove(data_file_path)

            postData = self.request.POST

        return super(TemplateView, self).render_to_response(context)

    def get_context_data(self, **kwargs):
        if self.request.POST:
            form = FileForm(self.request.POST, self.request.FILES)
        else :
            form = FileForm()
        return {'form':form}


class OrderFilterListView(SessionFilterListView):
    model = Order
    paginate_by = 12
    form_class = OrderFilterForm
    prefix = 'filters'  # Required because this view have the second form (production_date formset)
    success_url = reverse_lazy('order_list')
    filters = {
        'customers': 'customer__in',
        'production_date_start': 'production_date__gte',
        'production_date_end': 'production_date__lte',
    }

    def form_valid(self, form):
        """Process formset with production date field"""
        result = super(OrderFilterListView, self).form_valid(form)
        formset = OrderFormset(data=self.request.POST, queryset=self.object_list, prefix='formset')
        try:  # Catch exception when formset data is not sent
            if formset.is_valid():
                formset.save()
        except ValidationError:
            return result
        else:
            return HttpResponseRedirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        context = super(OrderFilterListView, self).get_context_data(**kwargs)
        context['formset'] = OrderFormset(queryset=self.object_list, prefix='formset')
        # Create a template context with both object_list and formset in one joined list for easy
        # manipulation/synchronization in template
        context['zipped_list'] = zip(self.object_list, context['formset'].forms)
        return context
