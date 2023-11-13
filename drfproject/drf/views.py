from django.shortcuts import render
from .serializer import ContactSerializer
from .models import Contact
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(["GET"])
def get_contacts(request):
    all_contacts = Contact.objects.all()
    serialized_contacts = ContactSerializer(all_contacts, many = True)
    data = serialized_contacts.data
    return Response(data)

