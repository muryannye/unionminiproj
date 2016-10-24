from django.conf.urls import url

from . import views

app_name = 'inventory'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # inventory/<folder_id>/
    url(r'^inventory/(?P<folder_id>[0-9]+)/$', views.detail, name='detail'),
    # inventory/<folder_id>/add
    url(r'^inventory/(?P<folder_id>[0-9]+)/add/$', views.add, name='add'),
]
