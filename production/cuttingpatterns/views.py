from braces.views import JSONResponseMixin, AjaxResponseMixin
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.views.generic import UpdateView
from django.views.generic.base import TemplateView, View
from django import forms
from .forms import RetailCuttingPatternForm, OutputFormSet, AdditionalGradesFormSet
from production.models import RetailCuttingPattern
from production.utils.get import recipe_component
from production.utils.get import shortage
from datetime import datetime
import get

class QueryForm(forms.Form):
    coatingChoices = forms.ChoiceField(label="Coating")
    panelDepths = forms.ChoiceField(label="Panel Depth")
    primarySizeChoices = forms.ChoiceField(label="Primary Size Desired")
    primarySizeQuantity = forms.IntegerField(label="Primary Quantity Desired", required=False, initial=0)
    isCradle = forms.BooleanField(label="Is Primary Cradled?", required=False)
    secondarySizeChoices = forms.ChoiceField(label="Secondary Size Desired", required=False)
    primarySizeChoices.choices = recipe_component.retail_sizes()
    #TODO: make this function and primary choice dropdown more useful
    secondarySizeChoices.choices = recipe_component.retail_sizes()
    secondarySizeChoices.choices.insert(0, ('', '----'))
    coatingChoices.choices = recipe_component.coatings()
    panelDepths.choices = recipe_component.panel_depths()


class CuttingPatternDetailsForm(forms.Form):
    tercero_panel_sizes = forms.ChoiceField(label="Panel Size", required=False)
    tercero_panel_sizes.choices = recipe_component.coating_cut_sizes()
    #panelDepths = forms.ChoiceField(label="Panel Depth")
    #panelDepths.choices = recipe_component.panel_depths()
    original_instructions = forms.CharField(required=False)
    grade_choice_1 = forms.ChoiceField(label="Grade 1", required=False)
    grade_choice_1.choices = recipe_component.grades()
    grade_choice_2 = forms.ChoiceField(label="Grade 2", required=False)
    grade_choice_2.choices = recipe_component.grades()
    grade_choice_3 = forms.ChoiceField(label="Grade 3", required=False)
    grade_choice_3.choices = recipe_component.grades()
    grade_choice_4 = forms.ChoiceField(label="Grade 4", required=False)
    grade_choice_4.choices = recipe_component.grades()
    grade_choice_5 = forms.ChoiceField(label="Grade 5", required=False)
    grade_choice_5.choices = recipe_component.grades()
    grade_choice_6 = forms.ChoiceField(label="Grade 6", required=False)
    grade_choice_6.choices = recipe_component.grades()
    instr1 = forms.CharField(label="Instructions")
    instr2 = forms.CharField(label='')
    instr3 = forms.CharField(label='')
    instr4 = forms.CharField(label='')
    instr5 = forms.CharField(label='')
    instr6 = forms.CharField(label='')
    output_quantity1 = forms.IntegerField()
    output_size1 = forms.ChoiceField()
    output_size1.choices = recipe_component.retail_sizes()
    isCradle1 = forms.BooleanField()
    isPrimary1 = forms.BooleanField()
    output_quantity2 = forms.IntegerField()
    output_size2 = forms.ChoiceField()
    output_size2.choices = recipe_component.retail_sizes()
    isCradle2 = forms.BooleanField()
    isPrimary2 = forms.BooleanField()
    output_quantity3 = forms.IntegerField()
    output_size3 = forms.ChoiceField()
    output_size3.choices = recipe_component.retail_sizes()
    isCradle3 = forms.BooleanField()
    isPrimary3 = forms.BooleanField()
    output_quantity4 = forms.IntegerField()
    output_size4 = forms.ChoiceField()
    output_size4.choices = recipe_component.retail_sizes()
    isCradle4 = forms.BooleanField()
    isPrimary4 = forms.BooleanField()
    output_quantity5 = forms.IntegerField()
    output_size5  = forms.ChoiceField()
    output_size5.choices = recipe_component.retail_sizes()
    isCradle5 = forms.BooleanField()
    isPrimary5 = forms.BooleanField()


class Instruction:
    def __init__(self, output, quantity, retail_cutting_pattern_id):
        self.output = output
        self.quantity = quantity
        self.retail_cutting_pattern_id = retail_cutting_pattern_id

class retail_cuts(TemplateView):
    template_name = 'cutting_patterns_index.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return super(retail_cuts, self).dispatch(request, *args, **kwargs)
        else:
            return redirect('/production/auth/login')


    def post(self, request, *args, **kwargs):
        if self.request.POST:
            context = self.get_context_data()
            queryForm = QueryForm(self.request.POST)
            context['currentSheetSummary'] = get.get_current_sheet_summary(queryForm["coatingChoices"].value(), queryForm["panelDepths"].value())
            context['currentSheet'] = get.cutting_sheet(queryForm["coatingChoices"].value(), queryForm["panelDepths"].value())
            context['coating'] = queryForm["coatingChoices"].value()
            context['depth'] = queryForm["panelDepths"].value()

            if 'submitQueryForm' in self.request.POST:
                context['testvarb'] = queryForm['primarySizeChoices'].value()
                context['status'] = 'submitted query form'
                searchedPatterns = get.cutting_patterns(queryForm['primarySizeChoices'].value(),\
                        queryForm['isCradle'].value(), queryForm['secondarySizeChoices'].value(),
                        get.net_retail_panels_needed(queryForm['primarySizeChoices'].value(),\
                                queryForm['primarySizeQuantity'].value(), context['currentSheetSummary'],\
                                queryForm['coatingChoices'].value(), queryForm['isCradle'].value()))
                print 'searchedPatterns: ' + str(len(searchedPatterns))
                context['cuttingPatterns'] = searchedPatterns

            if 'submitCuttingSheetSelection' in self.request.POST:
                context['status'] = 'submitted cutting sheet selection'
                instructions = []
                numberOfInstructions = 0
                for name, value in self.request.POST.items():
                    if name.startswith('quantityInputFor_'):
                        if (value):
                            numberOfInstructions = numberOfInstructions + 1
                            context['status'] = context['status'] + ', ' + name + ', ' + value
                            cuttingPatternId = name[len('quantityInputFor_'):]
                            instructions.append(Instruction('', value, cuttingPatternId))

                if (numberOfInstructions > 0):
                    get.add_to_sheet(self.request.POST["currentCuttingSheetId"], queryForm["coatingChoices"].value(),\
                                queryForm["panelDepths"].value(), queryForm["isCradle"].value(), instructions)
                context['currentSheetSummary'] = get.get_current_sheet_summary(queryForm["coatingChoices"].value(), queryForm["panelDepths"].value())

                context['status'] = context['status'] + '____submitting patterns for ' + str(numberOfInstructions) + ' numberOfInstructions'


            if 'submitNewCuttingSheet' in self.request.POST:
                #get.create_sheet(form['cutting_sheet_id'])
                get.new_sheet(queryForm["coatingChoices"].value(), queryForm["panelDepths"].value())
                context['currentSheetSummary'] = get.get_current_sheet_summary(queryForm["coatingChoices"].value(), queryForm["panelDepths"].value())
                context['currentSheet'] = get.cutting_sheet(queryForm["coatingChoices"].value(), queryForm["panelDepths"].value())
                context['status'] = 'do create new cutting sheet'

            if "finalizeCuttingSheet" in self.request.POST:
                self.template_name = 'cutting_patterns_cutting_sheet_print.html'
                context['finalSheet'] = get.final_cutting_sheet_instructions(queryForm["coatingChoices"].value(), queryForm["panelDepths"].value())
                context['finalSheetCoating'] = context['finalSheet'][0].coating
                context['finalSheetPanelDepth'] = context['finalSheet'][0].panel

            if context["form"].is_valid():
                print 'yes done'
                #save your model
                #redirect

            postData = self.request.POST

        return super(TemplateView, self).render_to_response(context)

    def get_context_data(self, **kwargs):
        if self.request.POST:
            form = QueryForm(self.request.POST)
            if form.is_valid():
                instance = form
        else :
            form = QueryForm()
        return {'form':form, 'testvar':["a","b","c"], 'testvarb':'b', 'cuttingPatterns':'', 'status':'unsubmitted', 'coating':'13', 'depth':'3'}

    def get_shortage(self, queryForm):
        #if queryForm[''] NEED LOGIC TO ENABLE retail/sprayed/glued/framed shortage calls
        # assume only retail cut shortages are being sought after right now
        return shortage.retail_cuts(datetime.now(), queryForm["isCradle"].value(), queryForm["coatingChoices"].value(),\
            queryForm['primarySizeChoices'].value(), queryForm["panelDepths"].value())


class retail_cuts_cutting_sheet_print(TemplateView):
    template_name = 'cutting_patterns_cutting_sheet_print.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return super(retail_cuts_cutting_sheet_print, self).dispatch(request, *args, **kwargs)
        else:
            return redirect('/production/auth/login')


    def post(self, request, *args, **kwargs):
        context = self.get_context_data()

        if self.request.POST:
            if 'submitReviewSelection' in self.request.POST:
                print 'in post'
                updates = []
                numberOfInstructions = 0
                for name, value in self.request.POST.items():
                    if name.startswith('quantityInputFor_'):
                        if (value):
                            numberOfInstructions = numberOfInstructions + 1
                            context['status'] = context['status'] + ', ' + name + ', ' + value
                            cuttingPatternEntryId = name[len('quantityInputFor_'):]
                            originalQuantity = '33' # self.request.POST[cuttingPatternEntryId] # TODO: Once we have real id's
                            if (originalQuantity == value):
                                print 'would not update'
                            else:
                                # TODO: Bryan, add to updates correctly - this would be enought; id + quantity, but may want to use a class other than Instruction...
                                updates.append(Instruction('', value, cuttingPatternEntryId))
                                print 'would update'

                # TODO: Bryan, call to update records that changed - either loop or feed list to get.py
                get.UpdateCuttingSheetEntries(updates)

                #reload all relevant data
                context = self.get_context_data()

        return super(TemplateView, self).render_to_response(context)

    def get_context_data(self, **kwargs):
        finalSheet = get.final_cutting_sheet_instructions(self.request.GET.get('coating', ''), self.request.GET.get('depth', ''))
        sheetForReview = get.review_instructions(self.request.GET.get('coating', ''), self.request.GET.get('depth', ''))
        sheetSummary = get.get_current_sheet_summary(self.request.GET.get('coating', ''), self.request.GET.get('depth', ''))
        coatingText = finalSheet[0].coating
        panelDepthText = finalSheet[0].panel
        return {'form':'', 'testvar':["a","b","c"], 'testvarb':'b', 'cuttingPatterns':'', \
                'status':'unsubmitted', \
                'finalSheet':finalSheet, \
                'currentSheetSummary': sheetSummary, \
                'finalSheetCoating': coatingText , \
                'finalSheetPanelDepth': panelDepthText, \
                'sheetForReview': sheetForReview}


class RetailCuttingPatternUpdateView(UpdateView):
    model = RetailCuttingPattern
    form_class = RetailCuttingPatternForm
    formset_output = OutputFormSet
    prefix_output = 'output'
    formset_grades = AdditionalGradesFormSet
    prefix_grades = 'grades'
    success_url = reverse_lazy('retailcut_search')

    def form_valid(self, form):
        formset_output = self.formset_output(
            instance=self.object, data=self.request.POST or None, prefix=self.prefix_output
        )
        if formset_output.is_valid():
            # Find other objects with same instructions (before changed) to display its grades
            sibling_grades = form.instance.get_siblings(form.initial['cutting_instructions'])
            formset_grades = self.formset_grades(
                queryset=sibling_grades, data=self.request.POST, prefix=self.prefix_grades
            )
            result = super(RetailCuttingPatternUpdateView, self).form_valid(form)
            formset_output.save()
            if formset_grades.is_valid():
                # Since should create new objects with the same data for `self.object` but `grade` is the only
                # field will be easier to set `self.object.pk` as None to clone objects
                new_cutting_patterns = formset_grades.save(commit=False)
                new_siblings_ids = []  # Save ids of new grades created to update his outputs latter
                for new_cutting_pattern in new_cutting_patterns:
                    if not new_cutting_pattern.pk:  # New objects created
                        self.object.pk = None
                        self.object.grade = new_cutting_pattern.grade
                        self.object.save()
                        new_siblings_ids.append(self.object.pk)
                    else:  # Be sure to save edited objects
                        new_cutting_pattern.save()

                # Then delete deleted objects (this is necessary because used commit=False on save formset)
                for obj in formset_grades.deleted_objects:
                    obj.delete()

                # Restore original object references
                self.object = self.get_object()
                form.instance = self.object

                # Update other fields in siblings
                # Create new dictionary based on form.cleaned_data by excluding the grade and unchanged data
                changed_data = {k: v for k, v in form.cleaned_data.items() if k not in ('grade',) and k in form.changed_data}
                if changed_data:
                    sibling_grades.update(**changed_data)

                # Update outputs in siblings
                if formset_output.has_changed():  # Outputs where modified
                    siblings_to_update_outputs = self.object.get_siblings()
                else:  # Add outputs in new siblings
                    siblings_to_update_outputs = RetailCuttingPattern.objects.filter(pk__in=new_siblings_ids)
                for sibling in siblings_to_update_outputs:
                    # Remove all outputs
                    sibling.retailcuttingpatternoutput_set.all().delete()
                    # Add outputs
                    for output in self.object.retailcuttingpatternoutput_set.all():
                        output.pk = None
                        output.retail_cutting_pattern = sibling
                        output.save()

            return result
        return self.form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super(RetailCuttingPatternUpdateView, self).get_context_data(**kwargs)
        context['formset_output'] = self.formset_output(
            instance=self.object, data=self.request.POST or None, prefix=self.prefix_output
        )
        sibling_grades = self.object.get_siblings()
        context['formset_grades'] = self.formset_grades(
            queryset=sibling_grades, data=self.request.POST or None, prefix=self.prefix_grades
        )
        return context


class retail_cut_edit(TemplateView):
    template_name = 'cutting_patterns_create_edit.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return super(retail_cut_edit, self).dispatch(request, *args, **kwargs)
        else:
            return redirect('/production/auth/login')


    def post(self, request, *args, **kwargs):
        context = self.get_context_data()

        if self.request.POST:
            if 'submitPatternForm' in self.request.POST:
                print 'in post'
                form = CuttingPatternDetailsForm(self.request.POST)
                # construct update call
                grades = []
                for i in range(1,6):
                    if self.request.POST['grade_choice_' + str(i)] != '':
                        grades.append(self.request.POST['grade_choice_' + str(i)])
                outputs = []
                for i in range(1,6):
                    if self.request.POST['output_quantity' + str(i)] != '':
                        outputs.append(self.getOutput(self.request.POST, i))
                instructions = []
                for i in range(1,7):
                    if self.request.POST['instr' + str(i)]:
                        instructions.append(self.request.POST['instr' + str(i)])

                print 'my instructions: ' + str.join('___', instructions)
                originalInstructions = self.request.POST.get('original_instructions', '')
                get.UpdateCuttingPattern(originalInstructions, self.request.POST['tercero_panel_sizes'], grades, outputs, str.join('___', instructions))

                #reload all relevant data
                context = self.get_context_data()
            if 'submitCopyPattern' in self.request.POST:
                originalInstructions = self.request.POST.get('original_instructions', '')
                newId = get.CopyCuttingPattern(originalInstructions)
                return redirect('/production/cuttingpatterns/retailcutedit?id=' + str(newId))

        return super(TemplateView, self).render_to_response(context)

    def getOutput(self, post, i):
        isPrimary = False if self.request.POST.get('isPrimary' + str(i), False) == False else True
        isCradle = False if self.request.POST.get('isCradle' + str(i), False) == False else True
        get.print_stuff(isCradle)
        return [self.request.POST['output_quantity' + str(i)], \
                self.request.POST['output_size' + str(i)], \
                isPrimary, \
                isCradle]


    def get_context_data(self, **kwargs):
        if self.request.GET:
            form = CuttingPatternDetailsForm()
            #load from DB based on incoming ID if avaialble
            incomingId = self.request.GET.get('id', '')
            if incomingId != '':
                cuttingPattern = get.ReadById(incomingId)
                cuttingPatternFull = get.ReadByInstruction(cuttingPattern.cuttingPatternInstructions)
                print 'loaded pattern for id: ' + incomingId + ', terceroid: ' + str(cuttingPatternFull.coatingSize.id) + ', grade: ' + cuttingPattern.grade + ', grades: ' + ', '.join(cuttingPatternFull.grade)
                # things to load: 1. Panel Size, 2. Panel Depth?, 3. Grades, 4. Instructions, 5. Outputs
                form.fields['tercero_panel_sizes'].initial = cuttingPatternFull.coatingSize.id
                currIndex = 1
                for grade in cuttingPatternFull.grade:
                    get.print_stuff(form.fields)
                    form.fields['grade_choice_' + str(currIndex)].initial = grade
                    currIndex += 1
                form.fields['original_instructions'].initial = cuttingPatternFull.cuttingPatternInstructions
                currIndex = 1
                for line in cuttingPatternFull.cuttingPatternInstructions.split('___'):
                    form.fields['instr' + str(currIndex)].initial = line
                    currIndex += 1
                currIndex = 1
                for output in cuttingPatternFull.outputs:
                    form.fields['output_size' + str(currIndex)].initial = output.retailSizeId
                    form.fields['output_quantity' + str(currIndex)].initial = output.quantity
                    isCradled = False
                    if output.isCradled:
                        isCradled = True
                    form.fields['isCradle' + str(currIndex)].initial = isCradled
                    form.fields['isPrimary' + str(currIndex)].initial = output.isPrimary
                    currIndex += 1

                print cuttingPattern

        return {
            'form': form, 'testvar': ["a", "b", "c"], 'testvarb': 'b', 'cuttingPatterns': '',
            'status': 'unsubmitted', 'patternId': incomingId,
            'formatted_instructions': get.format_cutting_pattern(form.fields['original_instructions'].initial, '')
        }


class InstructionFormatView(AjaxResponseMixin, JSONResponseMixin, View):
    """Get instructions formated in json format"""

    def get(self, request, *args, **kwargs):
        formatted_instructions = ''
        # example: "A:47.8  I:30.25->A:31 I:30.25(1)___I:16.25->A:31.8 I:20.2(1)"
        instructions_text = self.request.GET.get('instructions')
        if instructions_text:
            formatted_instructions = get.format_cutting_pattern(instructions_text, '')
        return self.render_json_response({'formatted_instructions': formatted_instructions})
