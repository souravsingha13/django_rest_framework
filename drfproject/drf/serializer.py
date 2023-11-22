from rest_framework import serializers
from drf.models import Contact


#implement a regular serializer
# class ContactSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length = 100)
#     title = serializers.CharField(max_length = 100)
#     email = serializers.EmailField(max_length = 100)

#     def create(self, validated_data):
#         """
#         Create and return a new `Contact` instance, given the validated data.
#         """
#         return Contact.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `Contact` instance, given the validated data.
#         """
#         instance.name = validated_data.get('name', instance.name)
#         instance.title = validated_data.get('title', instance.title)
#         instance.email = validated_data.get('email', instance.email)
#         instance.save()
#         return instance

# Implement model serializer

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'
