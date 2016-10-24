from django.conf.urls import url

from . import views

app_name = 'inventory'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # inventory/<folder_id>/
    url(r'^inventory/(?P<folder_id>[0-9]+)/$', views.detail, name='detail'),
    # inventory/add_folder
    url(r'^inventory/add_folder/$', views.add_folder, name='add_folder'),
    # inventory/<folder_id>/add_computer
    url(r'^inventory/(?P<folder_id>[0-9]+)/add_computer/$', views.add_computer, name='add_computer'),
    # inventory/<folder_id>/delete_folder
    url(r'^inventory/(?P<folder_id>[0-9]+)/delete_folder/$', views.delete_folder, name='delete_folder'),
    # inventory/<folder_id>/<computer_id>
    url(r'^inventory/(?P<folder_id>[0-9]+)/(?P<computer_id>[0-9]+)/$', views.computer, name='computer'),
    # inventory/<folder_id>/<computer_id>/update
    url(r'^inventory/(?P<folder_id>[0-9]+)/(?P<computer_id>[0-9]+)/edit/$', views.edit, name='edit'),
    # inventory/<folder_id>/<computer_id>/delete_computer
    url(r'^inventory/(?P<folder_id>[0-9]+)/(?P<computer_id>[0-9]+)/delete_computer/$', views.delete_computer, name='delete_computer'),

]
