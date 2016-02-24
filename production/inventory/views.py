from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from production.inventory import retrieve_wip
from production.inventory import save_wip
from django import forms
from django.forms.extras.widgets import SelectDateWidget
from production.utils.get import recipe_component
from datetime import date
from production.datetimewidget.widgets import DateTimeWidget, DateWidget, TimeWidget


class QueryForRetailCutsForm(forms.Form):
    retail_wip_type = forms.ChoiceField(label="WIP Type", required=False)
    retail_wip_date = forms.DateField(widget=SelectDateWidget(), label="WIP Date",\
            initial=date.today(), required=False)
    retail_coating_choices = forms.ChoiceField(label="Coating", required=False)
    retail_panel_depths = forms.ChoiceField(label="Panel Depth", required=False)
    retail_is_cradled = forms.BooleanField(label="Cradled?", required=False)
    retail_coating_choices.choices = recipe_component.coatings()
    retail_panel_depths.choices = recipe_component.panel_depths()
    retail_wip_type.choices = [['daily', 'Daily'], ['adjustment', 'Adjustment'], ['loss', 'Loss'], ['beginningofperiodinventory', 'Beginning of Period Inventory']]


class QueryForTerceroForm(forms.Form):
    tercero_wip_type = forms.ChoiceField(label="WIP Type", required=False)
    tercero_wip_date = forms.DateField(widget=DateWidget(usel10n=True, bootstrap_version=3),\
            initial=date.today(), required=False)
    tercero_coating_choices = forms.ChoiceField(label="Coating", required=False)
    tercero_panel_depths = forms.ChoiceField(label="Panel Depth", required=False)
    tercero_panel_sizes = forms.ChoiceField(label="Panel Size", required=False)
    # form field values
    tercero_coating_choices.choices = recipe_component.coatings()
    tercero_panel_depths.choices = recipe_component.panel_depths()
    tercero_panel_sizes.choices = recipe_component.coating_cut_sizes()
    tercero_wip_type.choices = [['daily', 'Daily'], ['adjustment', 'Adjustment'], ['loss', 'Loss'], ['beginningofperiodinventory', 'Beginning of Period Inventory']]


class QueryForSprayedForm(forms.Form):
    sprayed_wip_type = forms.ChoiceField(label="WIP Type", required=False)
    sprayed_wip_date = forms.DateField(widget=SelectDateWidget(), label="WIP Date",\
            initial=date.today(), required=False)
    sprayed_spray_color_choices = forms.ChoiceField(label="Color", required=False)
    sprayed_panel_depths = forms.ChoiceField(label="Panel Depth", required=False)
    #form field values
    sprayed_spray_color_choices.choices = recipe_component.spray_colors()
    sprayed_panel_depths.choices = recipe_component.panel_depths()
    sprayed_wip_type.choices = [['daily', 'Daily'], ['adjustment', 'Adjustment'], ['loss', 'Loss'], ['beginningofperiodinventory', 'Beginning of Period Inventory']]


class QueryForFramedForm(forms.Form):
    framed_wip_type = forms.ChoiceField(label="WIP Type", required=False)
    framed_wip_date = forms.DateField(widget=SelectDateWidget(), label="WIP Date",\
            initial=date.today(), required=False)
    framed_cradle_depths = forms.ChoiceField(label="Cradle Depth", required=False)
    framed_cradle_depths.choices = recipe_component.cradle_depths()
    framed_wip_type.choices = [['daily', 'Daily'], ['adjustment', 'Adjustment'], ['loss', 'Loss'], ['beginningofperiodinventory', 'Beginning of Period Inventory']]


class QueryForGluedForm(forms.Form):
    glued_wip_type = forms.ChoiceField(label="WIP Type", required=False)
    glued_wip_date = forms.DateField(widget=SelectDateWidget(), label="WIP Date",\
            initial=date.today(), required=False)
    glued_coating_choices = forms.ChoiceField(label="Coating", required=False)
    glued_panel_depths = forms.ChoiceField(label="Panel Depth", required=False)
    glued_cradle_depths = forms.ChoiceField(label="Cradle Depth", required=False)
    glued_coating_choices.choices = recipe_component.coatings()
    glued_panel_depths.choices = recipe_component.panel_depths()
    glued_cradle_depths.choices = recipe_component.cradle_depths()
    glued_wip_type.choices = [['daily', 'Daily'], ['adjustment', 'Adjustment'], ['loss', 'Loss'], ['beginningofperiodinventory', 'Beginning of Period Inventory']]


class inventory(TemplateView):
    template_name = 'inventory_index.html'
    def post(self, request, *args, **kwargs):
        if self.request.POST:
            context = self.get_context_data()

            if 'submitQueryRetail' in self.request.POST:
                context['status'] = 'submit query retail'
                context['queryType'] = 'retail'
                queryForm = QueryForRetailCutsForm(self.request.POST)
                context['entrySizes'] = retrieve_wip.retail_cut_wip(queryForm['retail_wip_date'].value(), queryForm['retail_is_cradled'].value(),
                    queryForm['retail_coating_choices'].value(), queryForm['retail_panel_depths'].value(), queryForm['retail_wip_type'].value())

            if 'submitQuerySprayed' in self.request.POST:
                context['status'] = 'submit query sprayed'
                context['queryType'] = 'sprayed'
                queryForm = QueryForSprayedForm(self.request.POST)
                context['entrySizes'] = retrieve_wip.sprayed_wip(queryForm['sprayed_wip_date'].value(), queryForm['sprayed_panel_depths'].value(),
                    queryForm['sprayed_spray_color_choices'].value(), queryForm['sprayed_wip_type'].value())

            if 'submitQueryFramed' in self.request.POST:
                context['status'] = 'submit query framed'
                context['queryType'] = 'framed'
                queryForm = QueryForFramedForm(self.request.POST)
                context['entrySizes'] = retrieve_wip.framed_wip(queryForm['framed_wip_date'].value(), queryForm['framed_cradle_depths'].value(),
                    queryForm['framed_wip_type'].value())

            if 'submitQueryGlued' in self.request.POST:
                context['status'] = 'submit query glued'
                context['queryType'] = 'glued'
                queryForm = QueryForGluedForm(self.request.POST)
                context['entrySizes'] = retrieve_wip.glued_wip(queryForm['glued_wip_date'].value(), queryForm['glued_coating_choices'].value(),
                    queryForm['glued_panel_depths'].value(), queryForm['glued_cradle_depths'].value(), queryForm['glued_wip_type'].value() )

            if 'submitQueryTercero' in self.request.POST:
                context['status'] = 'submit query tercero'
                context['queryType'] = 'tercero'
                queryForm = QueryForTerceroForm(self.request.POST)
                context['entrySizes'] = retrieve_wip.graded_wip(queryForm['tercero_wip_date'].value(), queryForm['tercero_coating_choices'].value(),
                    queryForm['tercero_panel_depths'].value(), queryForm['tercero_panel_sizes'].value(), queryForm['tercero_wip_type'].value() )

            if 'submitQuantities' in self.request.POST:
                context['status'] = 'submit quantities'
                # no form in this case; parse values from post data...
                wipEntries = []
                isRetailWip = isGluedWip = isFramedWip = isSprayedWip = isTerceroWip = False
                for name, value in self.request.POST.items():
                    if name.startswith('quantityInputFor_retail____') and value and value != '0': # this will look like e.g. quantityInputFor_retail____12____123 (of form )quantityInputFor_queryType____retail_size_id____wip_entry_id)
                        context['status'] = context['status'] + ', ' + name + ', ' + value
                        valuesToParse = name[len('quantityInputFor_retail____'):]
                        values = valuesToParse.split('____')
                        wipEntry = retrieve_wip.DisplaySizeRow(values[1], values[0], '0x0 in', value)
                        wipEntries.append(wipEntry)
                        isRetailWip = True
                    elif name.startswith('quantityInputFor_sprayed') and value and value != '0':
                        context['status'] = context['status'] + ', ' + name + ', ' + value
                        valuesToParse = name[len('quantityInputFor_sprayed____'):]
                        values = valuesToParse.split('____')
                        wipEntry = retrieve_wip.DisplaySizeRow(values[1], values[0], '0x0 in', value)
                        wipEntries.append(wipEntry)
                        isSprayedWip = True
                    elif name.startswith('quantityInputFor_framed') and value and value != '0':
                        context['status'] = context['status'] + ', ' + name + ', ' + value
                        valuesToParse = name[len('quantityInputFor_framed____'):]
                        values = valuesToParse.split('____')
                        wipEntry = retrieve_wip.DisplaySizeRow(values[1], values[0], '0x0 in', value)
                        wipEntries.append(wipEntry)
                        isFramedWip = True
                    elif name.startswith('quantityInputFor_glued') and value and value != '0':
                        context['status'] = context['status'] + ', ' + name + ', ' + value
                        valuesToParse = name[len('quantityInputFor_glued____'):]
                        values = valuesToParse.split('____')
                        wipEntry = retrieve_wip.DisplaySizeRow(values[1], values[0], '0x0 in', value)
                        wipEntries.append(wipEntry)
                        isGluedWip = True
                    elif name.startswith('quantityInputFor_tercero') and value and value != '0':
                        context['status'] = context['status'] + ', ' + name + ', ' + value
                        valuesToParse = name[len('quantityInputFor_tercero____'):]
                        values = valuesToParse.split('____')
                        wipEntry = retrieve_wip.DisplayGradeRow(values[1], values[0], value)
                        wipEntries.append(wipEntry)
                        isTerceroWip = True

                if (isRetailWip):
                    queryForm = QueryForRetailCutsForm(self.request.POST)
                    save_wip.retail_cut_wip(wipEntries, queryForm['retail_wip_date'].value(), queryForm['retail_is_cradled'].value(),
                        queryForm['retail_coating_choices'].value(), queryForm['retail_panel_depths'].value(), queryForm['retail_wip_type'].value())
                    context['status'] = context['status'] + ', NUM_ENTRIES: ' + str(len(wipEntries)) + ', isRetailWip: ' + str(isRetailWip)
                elif (isGluedWip):
                    queryForm = QueryForGluedForm(self.request.POST)
                    save_wip.glued_wip(wipEntries, queryForm['glued_wip_date'].value(), queryForm['glued_coating_choices'].value(),
                        queryForm['glued_cradle_depths'].value(), queryForm['glued_panel_depths'].value(), queryForm['glued_wip_type'].value())
                    context['status'] = context['status'] + ', NUM_ENTRIES: ' + str(len(wipEntries)) + ', isRetailWip: ' + str(isGluedWip)
                elif (isFramedWip):
                    queryForm = QueryForFramedForm(self.request.POST)
                    save_wip.framed_wip(wipEntries, queryForm['framed_wip_date'].value(), queryForm['framed_cradle_depths'].value(),
                        queryForm['framed_wip_type'].value())
                    context['status'] = context['status'] + ', NUM_ENTRIES: ' + str(len(wipEntries)) + ', isRetailWip: ' + str(isFramedWip)
                elif (isSprayedWip):
                    queryForm = QueryForSprayedForm(self.request.POST)
                    save_wip.sprayed_wip(wipEntries, queryForm['sprayed_wip_date'].value(), queryForm['sprayed_spray_color_choices'].value(),
                        queryForm['sprayed_panel_depths'].value(), queryForm['sprayed_wip_type'].value())
                    context['status'] = context['status'] + ', NUM_ENTRIES: ' + str(len(wipEntries)) + ', isRetailWip: ' + str(isSprayedWip)
                elif (isTerceroWip):
                    queryForm = QueryForTerceroForm(self.request.POST)
                    save_wip.graded_wip(wipEntries, queryForm['tercero_wip_date'].value(), queryForm['tercero_coating_choices'].value(),
                        queryForm['tercero_panel_depths'].value(), queryForm['tercero_panel_sizes'].value(), queryForm['tercero_wip_type'].value())
                    context['status'] = context['status'] + ', NUM_ENTRIES: ' + str(len(wipEntries)) + ', isRetailWip: ' + str(isSprayedWip)

            if context["queryRetailForm"].is_valid():
                print 'yes done'
                #save your model
                #redirect

            postData = self.request.POST

        return super(TemplateView, self).render_to_response(context)


    def get_context_data(self, **kwargs):
        if self.request.GET:
            queryRetailForm = QueryForRetailCutsForm()
            querySprayedForm = QueryForSprayedForm()
            queryFramedForm = QueryForFramedForm()
            queryGluedForm = QueryForGluedForm()
            queryTerceroForm = QueryForTerceroForm()
        else:            
            queryRetailForm = QueryForRetailCutsForm(self.request.POST)
            querySprayedForm = QueryForSprayedForm(self.request.POST)
            queryFramedForm = QueryForFramedForm(self.request.POST)
            queryGluedForm = QueryForGluedForm(self.request.POST)
            queryTerceroForm = QueryForTerceroForm(self.request.POST)

        return {'queryRetailForm':queryRetailForm, 'querySprayedForm':querySprayedForm, 'queryFramedForm':queryFramedForm,
                'queryGluedForm':queryGluedForm, 'queryTerceroForm':queryTerceroForm,
                'testvar':["a","b","c"], 'testvarb':'b', 'entrySizes':'', 'queryType':'', 'status':'unsubmitted', }

