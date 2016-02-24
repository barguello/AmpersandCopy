from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Ampersand.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^production/cuttingpatterns/', include('production.cuttingpatterns.urls')),
    url(r'^production/orders/', include('production.orders.urls')),
    url(r'^production/items/', include('production.items.urls')),
    url(r'^production/inventory/', include('production.inventory.urls')),
    url(r'^production/', include('production.urls')),
    url(r'^production/auth/', include('production.auth.urls')),
    )
