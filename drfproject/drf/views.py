# from django.shortcuts import render
# from .serializer import ContactSerializer
# from .models import Contact
# from django.http import JsonResponse
# from rest_framework.response import Response
# from django.http import HttpResponse
# from rest_framework.decorators import api_view
# from rest_framework import status 
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.views import APIView


# class ContactAPI(APIView):
#     def get(self, request, contact_id = None, format = None):
#         if contact_id:
#             contact = Contact.objects.get(pk = contact_id)
#             serialized_contact = ContactSerializer(contact)
#             data = serialized_contact.data
#             return Response(data)
#         all_contacts = Contact.objects.all()
#         serialized_contacts = ContactSerializer(all_contacts, many = True)
#         data = serialized_contacts.data
#         return Response(data)
    
#     def post(self, request, format = None):
#         serialized_data = ContactSerializer(data = request.data)
#         if serialized_data.is_valid():
#             serialized_data.save()
#             return Response("Successfully Added", status=status.HTTP_201_CREATED)
#         else:
#             return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def put(self, request, contact_id, format = None):
#         contact = Contact.objects.get(pk = contact_id)
#         serialized_contact = ContactSerializer(contact, data = request.data, partial = True)
#         if serialized_contact.is_valid():
#             serialized_contact.save()
#             Response("Successfully updated", status = status.HTTP_201_CREATED)
#         Response(serialized_contact.errors, status = status.HTTP_400_BAD_REQUEST)
    
#     def patch(self, request, contact_id, format = None):
#         contact = Contact.objects.get(pk = contact_id)
#         serialized_contact = ContactSerializer(contact, data = request.data, partial = True)
#         if serialized_contact.is_valid():
#             serialized_contact.save()
#             Response("Partial data updated", status = status.HTTP_201_CREATED)
#         Response(serialized_contact.errors, status = status.HTTP_400_BAD_REQUEST)
    
#     def delete(self, request, contact_id, format = None):
#         try: 
#             contact = Contact.objects.get(pk = contact_id)
#             contact.delete()
#             return Response({'message': 'Contact deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
#         except Contact.DoesNotExist:
#             return Response({"Error":"Contact not found"})


# @api_view(["GET"])
# def get_contacts(request, contact_id = None):
#     if contact_id:
#         contact = Contact.objects.get(pk = contact_id)
#         serialized_contact = ContactSerializer(contact)
#         data = serialized_contact.data
#         return Response(data)
#     all_contacts = Contact.objects.all()
#     serialized_contacts = ContactSerializer(all_contacts, many = True)
#     data = serialized_contacts.data
#     return Response(data)

# @api_view(["POST"])
# def add_contact(request):
#     if request.method == 'POST':
#         serialized_data = ContactSerializer(data = request.data)
#         if serialized_data.is_valid():
#             serialized_data.save()
#             return Response("Successfully Added", status=status.HTTP_201_CREATED)
#         else:
#             return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(["POST"])
# @csrf_exempt
# def update_contact(request, contact_id):
#     try:
#         contact = Contact.objects.get(pk=contact_id)
#     except Contact.DoesNotExist:
#         return Response({"Error": "Contact not found"}, status=404)

#     if request.method == 'POST':
#         serialized_data = ContactSerializer(contact, data=request.data)

#         if serialized_data.is_valid():
#             serialized_data.save()
#             return Response(serialized_data.data, status=200)
#         return Response(serialized_data.errors, status=400)

# @api_view(['GET'])
# def delete_contact(request,contact_id):
#     try: 
#         contact = Contact.objects.get(pk = contact_id)
#         contact.delete()
#         return Response({'message': 'Contact deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
#     except Contact.DoesNotExist:
#         return Response({"Error":"Contact not found"})
    
from .models import Contact
from .serializer import ContactSerializer
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView


class ContactAPI(ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ContactCreateAPI(CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class RetrieveContactAPI(RetrieveAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class UpdateContactAPI(UpdateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class DestroyContactAPI(DestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
