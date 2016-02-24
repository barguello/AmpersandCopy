from django.conf.urls import patterns, url, include

import views


urlpatterns = patterns('',
        url(r'^', views.items_view.as_view(), name="temp")
)
