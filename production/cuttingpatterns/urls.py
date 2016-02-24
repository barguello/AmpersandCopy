from django.conf.urls import patterns, url, include

import views

urlpatterns = patterns('',
        url(r'^cuttingsheetprint', views.retail_cuts_cutting_sheet_print.as_view(), name="temp"),
        url(r'^retailcuts', views.retail_cuts.as_view(), name="retailcut_search"),
        url(r'^retailcutedit', views.retail_cut_edit.as_view(), name="temp"),

        url(r'^retailcut/(?P<pk>\d+)/edit/', views.RetailCuttingPatternUpdateView.as_view(), name="retailcut_edit"),

        url(r'instruction/format/', views.InstructionFormatView.as_view(), name="cutting_instruction_format")
)
