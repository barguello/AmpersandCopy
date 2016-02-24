from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django import forms
import get
from production.utils.get import recipe_component
import pdb


class RecipeQueryForm(forms.Form):
    sizeChoices = forms.MultipleChoiceField(label="Size")
    coatingChoices = forms.MultipleChoiceField(label="Coating")
    panelDepthChoices = forms.MultipleChoiceField(label="Panel Depth")
    cradleDepthChoices = forms.MultipleChoiceField(label="Cradle Depth")
    cradleWidthChoices = forms.MultipleChoiceField(label="Cradle Width")
    sprayColorChoices = forms.MultipleChoiceField(label="Color")

    sizeChoices.choices = recipe_component.retail_sizes()
    coatingChoices.choices = recipe_component.coatings()
    panelDepthChoices.choices = recipe_component.panel_depths()
    cradleDepthChoices.choices = recipe_component.cradle_depths()
    cradleWidthChoices.choices = recipe_component.cradle_widths()
    sprayColorChoices.choices = recipe_component.spray_colors()

class QueryForm(forms.Form):
    txtSku = forms.CharField(label="SKU")

class items_view(TemplateView):
    template_name = 'items_index.html'
    def post(self, request, *args, **kwargs):
        if self.request.POST:
            context = self.get_context_data()
            form = QueryForm(self.request.POST)
            recipe_form = RecipeQueryForm(self.request.POST)

            if 'submitRecipeForm' in self.request.POST:
                context['retail_sizes'] = recipe_form['sizeChoices'].value()
                context['coatings'] = recipe_form['coatingChoices'].value()
                context['panel_depths'] = recipe_form['panelDepthChoices'].value()
                context['cradle_depths'] = recipe_form['cradleDepthChoices'].value()
                context['cradle_widths'] = recipe_form['cradleWidthChoices'].value()
                context['spray_colors'] = recipe_form['sprayColorChoices'].value()
                context['items'] = get.items(context)
                #pdb.set_trace()

            if 'submitSkuForm' in self.request.POST:
                context['testvar'] = form['txtSku'].value()
                context['arecipe'] = get.recipe(form['txtSku'].value())[0]

            if context["form"].is_valid():
                print 'Done!'
                #save your model
                #redirect

            postData = self.request.POST

        return super(TemplateView, self).render_to_response(context)

    def get_context_data(self, **kwargs):
        if self.request.POST:
            form = QueryForm(self.request.POST)
            recipe_form = RecipeQueryForm(self.request.POST)
            if form.is_valid():
                instance = form
        else :
            form = QueryForm()
            recipe_form = RecipeQueryForm()

        return {'form':form, 'recipe_form':recipe_form, 'testvar':'', 'testvarb':'b', 'testvarc':'c', 'arecipe':'', 'items':''}
