from django.conf.urls import patterns, url, include
from django.core.urlresolvers import reverse_lazy
from django.views.generic import UpdateView, CreateView, ListView
from production import views
from .models import ItemRecipe, RetailSize, PanelDepth, CradleDepth, CradleWidth, Coating, SprayColor, Item
from .views import RecipeFilterListView, DeleteRecipeView, RetailSizeListView, DeleteByInactiveView, ItemFilterListView, \
    ItemInlinePacksCreateView, ItemInlinePacksUpdateView

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^recipe/$', RecipeFilterListView.as_view(), name='recipe_list'),
    url(r'^recipe/(?P<pk>\d+)/edit/$', UpdateView.as_view(model=ItemRecipe, success_url=reverse_lazy('recipe_list')), name='recipe_edit'),
    url(r'^recipe/add/$', CreateView.as_view(model=ItemRecipe, success_url=reverse_lazy('recipe_list')), name='recipe_add'),
    url(r'^recipe/(?P<pk>\d+)/delete/$', DeleteRecipeView.as_view(), name='recipe_delete'),

    # Item CRUD
    url(r'item/$', ItemFilterListView.as_view(), name='item_list'),
    url(r'item/add/$', ItemInlinePacksCreateView.as_view(), name='item_add'),
    url(r'item/(?P<pk>\d+)/edit/$', ItemInlinePacksUpdateView.as_view(), name='item_edit'),
    url(r'^item/(?P<pk>\d+)/delete/$', DeleteByInactiveView.as_view(
        model=Item,
        success_url=reverse_lazy('item_list'),
        template_name='production/component_confirm_delete.html'
    ), name='item_delete'),

    # Retail Size CRUD
    url(r'^component/(retail/)?$', RetailSizeListView.as_view(), name='retail_size_list'),
    url(r'^component/retail/add/$',
        CreateView.as_view(model=RetailSize, success_url=reverse_lazy('retail_size_list')), name='retail_size_add'),
    url(r'^component/retail/(?P<pk>\d+)/edit/$',
        UpdateView.as_view(model=RetailSize, success_url=reverse_lazy('retail_size_list')), name='retail_size_edit'),
    url(r'^component/retail/(?P<pk>\d+)/delete/$', DeleteByInactiveView.as_view(
        model=RetailSize,
        success_url=reverse_lazy('retail_size_list'),
        template_name='production/component_confirm_delete.html'
    ), name='retail_size_delete'),

    # Panel Depths CRUD
    url(r'^component/panel-depth/$', ListView.as_view(model=PanelDepth, paginate_by=15), name='panel_depth_list'),
    url(r'^component/panel-depth/add/$',
        CreateView.as_view(model=PanelDepth, success_url=reverse_lazy('panel_depth_list')), name='panel_depth_add'),
    url(r'^component/panel-depth/(?P<pk>\d+)/edit/$',
        UpdateView.as_view(model=PanelDepth, success_url=reverse_lazy('panel_depth_list')), name='panel_depth_edit'),
    url(r'^component/panel-depth/(?P<pk>\d+)/delete/$', DeleteByInactiveView.as_view(
        model=PanelDepth,
        success_url=reverse_lazy('panel_depth_list'),
        template_name='production/component_confirm_delete.html'
    ), name='panel_depth_delete'),

    # Cradle Depth CRUD
    url(r'^component/cradle-depth/$', ListView.as_view(model=CradleDepth, paginate_by=15), name='cradle_depth_list'),
    url(r'^component/cradle-depth/add/$',
        CreateView.as_view(model=CradleDepth, success_url=reverse_lazy('cradle_depth_list')), name='cradle_depth_add'),
    url(r'^component/cradle-depth/(?P<pk>\d+)/edit/$',
        UpdateView.as_view(model=CradleDepth, success_url=reverse_lazy('cradle_depth_list')), name='cradle_depth_edit'),
    url(r'^component/cradle-depth/(?P<pk>\d+)/delete/$', DeleteByInactiveView.as_view(
        model=CradleDepth,
        success_url=reverse_lazy('cradle_depth_list'),
        template_name='production/component_confirm_delete.html'
    ), name='cradle_depth_delete'),

    # Cradle Width CRUD
    url(r'^component/cradle-width/$', ListView.as_view(model=CradleWidth, paginate_by=15), name='cradle_width_list'),
    url(r'^component/cradle-width/add/$',
        CreateView.as_view(model=CradleWidth, success_url=reverse_lazy('cradle_width_list')), name='cradle_width_add'),
    url(r'^component/cradle-width/(?P<pk>\d+)/edit/$',
        UpdateView.as_view(model=CradleWidth, success_url=reverse_lazy('cradle_width_list')), name='cradle_width_edit'),
    url(r'^component/cradle-width/(?P<pk>\d+)/delete/$', DeleteByInactiveView.as_view(
        model=CradleWidth,
        success_url=reverse_lazy('cradle_width_list'),
        template_name='production/component_confirm_delete.html'
    ), name='cradle_width_delete'),

    # Coatings CRUD
    url(r'^component/coating/$', ListView.as_view(model=Coating, paginate_by=15), name='coating_list'),
    url(r'^component/coating/add/$',
        CreateView.as_view(model=Coating, success_url=reverse_lazy('coating_list')), name='coating_add'),
    url(r'^component/coating/(?P<pk>\d+)/edit/$',
        UpdateView.as_view(model=Coating, success_url=reverse_lazy('coating_list')), name='coating_edit'),
    url(r'^component/coating/(?P<pk>\d+)/delete/$', DeleteByInactiveView.as_view(
        model=Coating,
        success_url=reverse_lazy('coating_list'),
        template_name='production/component_confirm_delete.html'
    ), name='coating_delete'),

    # Spray CRUD
    url(r'^component/spray-color/$', ListView.as_view(model=SprayColor, paginate_by=15), name='spray_color_list'),
    url(r'^component/spray-color/add/$',
        CreateView.as_view(model=SprayColor, success_url=reverse_lazy('spray_color_list')), name='spray_color_add'),
    url(r'^component/spray-color/(?P<pk>\d+)/edit/$',
        UpdateView.as_view(model=SprayColor, success_url=reverse_lazy('spray_color_list')), name='spray_color_edit'),
    url(r'^component/spray-color/(?P<pk>\d+)/delete/$', DeleteByInactiveView.as_view(
        model=SprayColor,
        success_url=reverse_lazy('spray_color_list'),
        template_name='production/component_confirm_delete.html'
    ), name='spray_color_delete'),
)
