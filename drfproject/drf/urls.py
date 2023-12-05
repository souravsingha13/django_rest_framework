from django.urls import path
from drf import views



urlpatterns = [
    # path('all-contacts', views.get_contacts, name = 'all-contacts'),
    # path('all-contacts/<int:contact_id>', views.get_contacts, name = 'all-contacts'),
    # path('add-contact', views.add_contact, name = 'add-contact'),
    # path('update-contact/<int:contact_id>/', views.update_contact, name = 'update-contact'),
    # path('delete-contact/<int:contact_id>/', views.delete_contact, name = 'delete-contact'),
    path('all-contacts/', views.ContactAPI.as_view(), name='all-contacts'),
    path('create-contacts/', views.ContactCreateAPI.as_view(), name='all-contacts'),
    path('all-contacts/<int:pk>', views.RetrieveContactAPI.as_view(), name = 'all-contacts'),
    path('update-contacts/<int:pk>', views.UpdateContactAPI.as_view(), name = 'update-contacts'),
    path('delete-contact/<int:pk>',views.DestroyAPIView.as_view(), name = 'delete-contact')
]