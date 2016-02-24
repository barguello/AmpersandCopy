from django import forms
from django.core.urlresolvers import reverse
from django.forms import MultiValueField, MultiWidget, TextInput, modelformset_factory
from django.forms.models import inlineformset_factory
from django.forms.widgets import Select, CheckboxInput
from production.models import RetailCuttingPattern, RetailCuttingPatternOutput
from production.utils.get.recipe_component import grades


class CuttingInstructionsSplitWidget(MultiWidget):
    def __init__(self, *args, **kwargs):
        widgets = (TextInput, TextInput, TextInput, TextInput, TextInput, TextInput)
        super(CuttingInstructionsSplitWidget, self).__init__(widgets, *args, **kwargs)

    def decompress(self, value):
        return value.split('___')

    def format_output(self, rendered_widgets):
        output = super(CuttingInstructionsSplitWidget, self).format_output(rendered_widgets)
        template = '''
            <script>var cutting_instruction_format_url = '{}';</script>
            <div class="cutting-patterns-preview pull-right" style="height:{}px"></div>
            {}
        '''
        cutting_instruction_format_url = reverse('cutting_instruction_format')
        preview_height = len(rendered_widgets) * 34  # 34 is the height of each input field
        return template.format(cutting_instruction_format_url, preview_height, output)


class CuttingInstructionsSplitField(MultiValueField):
    widget = CuttingInstructionsSplitWidget

    def __init__(self, *args, **kwargs):
        fields = (
            forms.CharField(),
            forms.CharField(),
            forms.CharField(),
            forms.CharField(),
            forms.CharField(),
            forms.CharField()
        )
        super(CuttingInstructionsSplitField, self).__init__(fields, *args, **kwargs)

    def compress(self, data_list):
        return "___".join(data_list)


class RetailCuttingPatternForm(forms.ModelForm):
    grade = forms.ChoiceField(choices=grades())
    cutting_instructions = CuttingInstructionsSplitField(label="Instructions", required=False)

    class Meta:
        model = RetailCuttingPattern
        fields = ('coating_size', 'grade', 'cutting_instructions', 'is_active')

    class Media:
        js = (
            'production/js/preview_splitted_instructions.js',  # required by CuttingInstructionsSplitWidget
        )


class RetailCuttingPatternOutputForm(forms.ModelForm):
    # Use of check_test in widget because that fields are integer in model
    is_for_cradle = forms.BooleanField(label="Cradle?", required=False, widget=CheckboxInput(check_test=lambda x: (x or 0) % 2 == 1))
    is_primary = forms.BooleanField(label="Primary?", required=False, widget=CheckboxInput(check_test=lambda x: (x or 0) % 2 == 1))

    class Meta:
        model = RetailCuttingPatternOutput

    class Media:
        css = {
            'all': ('django_bootstrap_dynamic_formsets/extra.css',)
        }
        # jquery-ui is required for django-bootstrap-dynamic-formset
        js = ('bower_components/jquery-ui/jquery-ui.min.js',)

OutputFormSet = inlineformset_factory(
    RetailCuttingPattern, RetailCuttingPatternOutput, form=RetailCuttingPatternOutputForm, extra=1
)


AdditionalGradesFormSet = modelformset_factory(
    RetailCuttingPattern, extra=1, can_delete=True, fields=('grade',), widgets={
        'grade': Select(choices=grades(), attrs={'class': 'form-control'})
    }
)
