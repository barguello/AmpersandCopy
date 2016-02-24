from django.conf.urls import patterns, url, include
import views

urlpatterns = patterns('',
    url(r'^$', views.OrderFilterListView.as_view(), name="order_list"),
    url(r'^import/$', views.order_import.as_view(), name="temp")
)
