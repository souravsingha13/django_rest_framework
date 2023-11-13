from django.urls import path
from . import views


urlpatterns = [
    path('all-contacts', views.get_contacts, name = 'all-contacts'),
    path('add-contact', views.add_contact, name = 'add-contact')
]