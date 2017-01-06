from django.conf.urls import url
from django.contrib import admin
from rip_app import views
from  rip_app.views import Offices, OfficeDetail, sub


urlpatterns = (
    url(r'^admin/', admin.site.urls, name='admin'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^Offices/$', Offices.as_view(), name='Offices'),
    url(r'^office/(?P<pk>[0-9]+)/members/$', OfficeDetail.as_view(), name='office-detail'),
    url(r'^$', Offices.as_view(), name='Offices'),
    url(r'^office/new/$', views.office_new, name='office_new'),
    url(r'^listing/$', views.listing, name='listing'),
    url(r'^members/new/$', views.member_new, name='member_new'),
    url(r'^sub/$', sub),


)
