from dataclasses import fields
from pyexpat import model
from unicodedata import name
from django import forms
from rest_framework import serializers
from .models import Contact, BlogPost

class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields='__all__'
        
class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model=Contact
       # fields='__all__'
        fields=['id','name','email','phone','subject','details']
        
from rest_framework import serializers
class ContactSerializerOne(serializers.Serializer):
    name = serializers.CharField(max_length=20)
    email = serializers.EmailField()
    phone = serializers.CharField(max_length=17)
    subject= serializers.CharField(max_length=20)
    details= serializers.CharField(max_length=100)
    
    def create(self, validated_data):
        return Contact(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.subject = validated_data.get('subject', instance.subject)
        instance.details = validated_data.get('details', instance.details)
        instance.save()
        return instance
class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        # fields="__all__"
        exclude=['user','is_active']
class PostDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields="__all__"
