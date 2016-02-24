import datetime
from braces.views import CsrfExemptMixin, JSONResponseMixin, AjaxResponseMixin
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views.generic import TemplateView, ListView, DeleteView, CreateView, UpdateView, FormView
from django.views.generic.edit import FormMixin, ModelFormMixin, ProcessFormView
from .forms import RecipeFilterForm, ItemPacksFormSet
from .models import ItemRecipe, RetailSize, Item
from production.utils import display


class index(TemplateView):
    template_name = 'base_site.html'


class SessionFilterListView(FormView, ListView):
    """
    Base class to implement a list view with a form associate to filter objects.

    Subclasses should specify the attribute `filter`, which is a dictionary to map form fields with lookup filters

    Filters are saved in a session, if you want a custom session name add a property named `session_filter_name` with
    the wanted string name, by default it will take the name of the class.
    """
    filters = {}

    def get_initial(self):
        return self.session_filters

    def get_queryset(self):
        queryset = super(SessionFilterListView, self).get_queryset()
        return queryset.filter(**self.get_filters(self.session_filters)).distinct()

    def get_context_data(self, **kwargs):
        context = super(SessionFilterListView, self).get_context_data(**kwargs)
        form_class = self.get_form_class()
        context['form'] = self.get_form(form_class)
        return context

    def form_valid(self, form):
        self.session_filters = form.cleaned_data
        return self.get(self.request, self.args, self.kwargs)

    def form_invalid(self, form):
        return self.get(self.request, self.args, self.kwargs)

    @property
    def session_filter_name(self):
        return self.__class__.__name__

    @property
    def session_filters(self):
        return self.request.session.get(self.session_filter_name, {})

    @session_filters.setter
    def session_filters(self, filters):
        filters_copy = filters.copy()
        for key, value in filters_copy.items():
            try:  # Remove empty queryset
                if len(value) == 0:
                    del filters_copy[key]
                else:
                    try:  # Make queryset serializable
                        filters_copy[key] = list(value.values_list('pk', flat=True))
                    except AttributeError:
                        pass
            except TypeError:
                # If is date object convert it to string to avoid serializable json errors
                if isinstance(value, datetime.date) or isinstance(value, datetime.datetime):
                    filters_copy[key] = value.isoformat()
        self.request.session[self.session_filter_name] = filters_copy

    def update_session_filters(self, filters):
        tmp_filters = self.session_filters
        tmp_filters.update(filters)
        self.session_filters = tmp_filters

    def get_filters(self, data):
        filters = {}
        for key, value in data.items():
            key_filter = self.filters.get(key)
            if key_filter and value is not None:
                try:
                    if len(value) == 0:
                        continue
                except TypeError:
                    pass
                filters[key_filter] = value
        return filters


class RecipeFilterListView(CsrfExemptMixin, AjaxResponseMixin, JSONResponseMixin, SessionFilterListView):
    model = ItemRecipe
    form_class = RecipeFilterForm
    paginate_by = 15
    filters = {
        'is_active': 'is_active',
        'coating': 'coating__in',
        'retail_size': 'retail_size__in',
        'panel_depth': 'panel_depth__in',
        'cradle_depth': 'cradle_depth__in',
        'cradle_width': 'cradle_width__in',
        'spray_color': 'spray_color__in',
    }

    def get_paginate_by(self, queryset):
        result = super(RecipeFilterListView, self).get_paginate_by(queryset)
        if self.request.is_ajax():
            return None
        return result

    def post_ajax(self, request, *args, **kwargs):
        # Get unfiltered object_list
        self.object_list = super(RecipeFilterListView, self).get_queryset()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            # Apply filters
            filters = self.get_filters(form.cleaned_data)
            self.object_list = self.object_list.filter(**filters)
        result = {
            'recipe_list': []
        }
        for recipe in self.object_list:
            result['recipe_list'].append({
                'id': recipe.id,
                'retail_size': str(recipe.retail_size),
                'coating': str(recipe.coating),
                'panel_depth': str(recipe.panel_depth),
                'cradle_depth': str(recipe.cradle_depth),
                'cradle_width': str(recipe.cradle_width),
                'spray_color': str(recipe.spray_color),
                'is_active': recipe.is_active,
            })
        return self.render_json_response(result)

    def get_queryset(self):
        # TODO: Allow to specify initial filters in SessionFilterListView to avoid methods like this
        if 'is_active' not in self.session_filters:
            self.update_session_filters({'is_active': True})
        return super(RecipeFilterListView, self).get_queryset()


class DeleteByInactiveView(DeleteView):
    def delete(self, request, *args, **kwargs):
        """Do not delete object but inactive it"""
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(success_url)

    def get_context_data(self, **kwargs):
        context = super(DeleteByInactiveView, self).get_context_data(**kwargs)
        context['verbose_name'] = self.object._meta.verbose_name
        object_list_url = '{}_list'.format(self.object._meta.db_table)
        context['cancel_url'] = reverse_lazy(object_list_url)
        return context


class DeleteRecipeView(DeleteByInactiveView):
    model = ItemRecipe
    success_url = reverse_lazy('recipe_list')


class RetailSizeListView(ListView):
    model = RetailSize
    paginate_by = 15


class ItemFilterListView(SessionFilterListView):
    model = Item
    paginate_by = 12
    form_class = RecipeFilterForm
    filters = {
        'retail_size': 'pack__item_recipe__retail_size__in',
        'cradle_depth': 'pack__item_recipe__cradle_depth__in',
        'cradle_width': 'pack__item_recipe__cradle_width__in',
        'panel_depth': 'pack__item_recipe__panel_depth__in',
        'coating': 'pack__item_recipe__coating__in',
        'spray_color': 'pack__item_recipe__spray_color__in',
        'is_active': 'is_active'
    }


class ItemInlinePacksFormView(ModelFormMixin, ProcessFormView):
    model = Item
    success_url = reverse_lazy('item_list')

    def form_valid(self, form):
        result = super(ItemInlinePacksFormView, self).form_valid(form)
        formset_packs = ItemPacksFormSet(instance=self.object, data=self.request.POST, prefix='pack')
        if formset_packs.is_valid():
            formset_packs.save()
        else:
            return self.form_invalid(form)
        return result

    def get_context_data(self, **kwargs):
        context = super(ItemInlinePacksFormView, self).get_context_data(**kwargs)
        context['formset_packs'] = ItemPacksFormSet(instance=self.object, data=self.request.POST or None, prefix='pack')
        context['recipe_filter_form'] = RecipeFilterForm()
        return context


class ItemInlinePacksCreateView(ItemInlinePacksFormView, CreateView):
    pass


class ItemInlinePacksUpdateView(ItemInlinePacksFormView, UpdateView):
    pass
