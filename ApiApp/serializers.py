from dataclasses import fields
from pyexpat import model
from django import forms
from rest_framework import serializers
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields='__all__'
        
class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model=Contact
       # fields='__all__'
        fields=['id','name','email','phone','subject','details']