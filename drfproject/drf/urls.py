from django.urls import path
from . import views


urlpatterns = [
    path('all-contacts', views.get_contacts, name = 'all-contacts'),
    path('all-contacts/<int:contact_id>', views.get_contacts, name = 'all-contacts'),
    path('add-contact', views.add_contact, name = 'add-contact'),
    path('update-contact/<int:contact_id>/', views.update_contact, name = 'update-contact')
]