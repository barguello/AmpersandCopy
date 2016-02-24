from bootstrap3_datetime.widgets import DateTimePicker
from django import forms
from django.core.exceptions import ValidationError
from django.forms.models import modelformset_factory

from production.models import Customer, Order


class OrderFilterForm(forms.Form):
    production_date_start = forms.DateField(
        label="Production date start", required=False,
        widget=DateTimePicker(options={"format": "YYYY-MM-DD", "pickTime": False})
    )
    production_date_end = forms.DateField(
        label='End', required=False,
        widget=DateTimePicker(options={"format": "YYYY-MM-DD", "pickTime": False})
    )
    customers = forms.ModelMultipleChoiceField(queryset=Customer.objects.all(), required=False)

    def clean(self):
        if self.cleaned_data.get('production_date_start', 0) > self.cleaned_data.get('production_date_end', 1):
            raise ValidationError("Start date should earlier than end date!")
        return super(OrderFilterForm, self).clean()

OrderFormset = modelformset_factory(Order, fields=('production_date',), extra=0, widgets={
    'production_date': DateTimePicker(options={"format": "YYYY-MM-DD", "pickTime": False})
})
