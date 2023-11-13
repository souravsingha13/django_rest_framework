from django.shortcuts import render
from .serializer import ContactSerializer
from .models import Contact
from django.http import JsonResponse
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework import status 


@api_view(["GET"])
def get_contacts(request):
    all_contacts = Contact.objects.all()
    serialized_contacts = ContactSerializer(all_contacts, many = True)
    data = serialized_contacts.data
    return Response(data)

@api_view(["POST"])
def add_contact(request):
    if request.method == 'POST':
        serialized_data = ContactSerializer(data = request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response("Successfully Added", status=status.HTTP_201_CREATED)
        else:
            return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)
