from django.conf.urls import patterns, include, url
from django.contrib import admin
import billing.views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cep_final_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'bills/$', billing.views.BillsList.as_view()),
    url(r'bills/(?P<pk>[0-9]+)/$', billing.views.BillDetail.as_view()),
    url(r'items/$', billing.views.ItemsList.as_view()),
    url(r'items/(?P<pk>[0-9]+)/$', billing.views.ItemDetail.as_view()),
)
