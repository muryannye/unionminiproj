from django.conf.urls import url

from . import views

app_name = 'inventory'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # inventory/<folder_id>/
    url(r'^inventory/(?P<folder_id>[0-9]+)/$', views.detail, name='detail'),
    # inventory/<folder_id>/delete
    # url(r'^inventory/(?P<folder_id>[0-9]+)/delete/$', views.delete_folder, name='delete_folder'),
    # inventory/<folder_id>/add
    url(r'^inventory/(?P<folder_id>[0-9]+)/add/$', views.add, name='add'),
    # inventory/<folder_id>/<computer_id>
    url(r'^inventory/(?P<folder_id>[0-9]+)/(?P<computer_id>[0-9]+)/$', views.computer, name='computer'),
    # inventory/<folder_id>/<computer_id>/update
    url(r'^inventory/(?P<folder_id>[0-9]+)/(?P<computer_id>[0-9]+)/update/$', views.update, name='update'),

]
