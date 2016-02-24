from django.conf.urls import patterns, url, include

import views

urlpatterns = patterns('',
        url(r'^login', views.login_view.as_view(), name="temp"),
)
