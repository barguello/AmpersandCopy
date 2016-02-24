from django import forms
from django.forms.models import inlineformset_factory, ModelForm
from django.forms.widgets import SelectMultiple, NullBooleanSelect
from .models import Item, Pack, Coating, CradleDepth, CradleWidth, PanelDepth, RetailSize, SprayColor


class RecipeFilterForm(forms.Form):
    retail_size = forms.ModelMultipleChoiceField(queryset=RetailSize.objects.all(), required=False, widget=SelectMultiple(attrs={'class': 'form-control'}))
    coating = forms.ModelMultipleChoiceField(queryset=Coating.objects.all(), required=False, widget=SelectMultiple(attrs={'class': 'form-control'}))
    panel_depth = forms.ModelMultipleChoiceField(queryset=PanelDepth.objects.all(), required=False, widget=SelectMultiple(attrs={'class': 'form-control'}))
    cradle_depth = forms.ModelMultipleChoiceField(queryset=CradleDepth.objects.all(), required=False, widget=SelectMultiple(attrs={'class': 'form-control'}))
    cradle_width = forms.ModelMultipleChoiceField(queryset=CradleWidth.objects.all(), required=False, widget=SelectMultiple(attrs={'class': 'form-control'}))
    spray_color = forms.ModelMultipleChoiceField(queryset=SprayColor.objects.all(), required=False, widget=SelectMultiple(attrs={'class': 'form-control'}))
    is_active = forms.NullBooleanField(required=False, initial=True, widget=NullBooleanSelect(attrs={'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        super(RecipeFilterForm, self).__init__(*args, **kwargs)
        self.fields['is_active'].widget.choices = (
            ('1', "Both"),
            ('2', "Yes"),
            ('3', "No")
        )


class PackModelForm(ModelForm):
    class Meta:
        model = Pack
        widgets = {
            'item_recipe': forms.widgets.HiddenInput()
        }

    class Media:
        js = (
            'bower_components/jquery-ui/jquery-ui.min.js',  # jquery-ui is required for django-bootstrap-dynamic-formset
            'production/js/select_recipe.js',  # Used for select recipe widget
        )

    def __init__(self, *args, **kwargs):
        super(PackModelForm, self).__init__(*args, **kwargs)
        self.fields['item_recipe'].widget.recipe_text = str(self.instance.item_recipe or "")

ItemPacksFormSet = inlineformset_factory(Item, Pack, form=PackModelForm, extra=1)
