import email
from importlib.resources import contents
from multiprocessing import context
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated,AllowAny

from ApiApp.models import Contact
#from ApiProject.ApiApp.models import BlogPost

# Create your views here.
''' class HomeView(TemplateView):
    template_name = "template.html"
    def get(self, request):
        context={
            'name':'Md Hafizur Rahman',
            'University':'Daffodil International University'
        }
        return render(request, self.template_name,context)
from rest_framework.response import Response
from rest_framework.views import APIView

class HomeApiView(APIView):
    def get(self,request,format=None):
        if request.method=='POST':
            data1=request.data['data1']
            data2=request.data['data2']
        
        context={
            'name':'Md Hafizur Rahman',
            'University':'Daffodil International University'
        }
        return Response(context) '''
def homeView(request):
    return render(request,'index.html') 
@api_view(['GET','POST'])
#@permission_classes([IsAuthenticated,])
def firstApi(request):
    if request.method=='POST':
        name=request.data['name']
        age=request.data['age']
        print(name,age)
        return Response({'name':name,'age':age})
    context={
        'name':"hafizur",
        'University':"Diu"
    }
    return Response(context)
from django.contrib.auth.models import User
@api_view(['POST',])
@permission_classes([IsAuthenticated])
def registrationApi(request):
    if request.method=='POST':
        username=request.data['username']
        email=request.data['email']
        first_name=request.data['first_name']
        last_name=request.data['last_name']
        password=request.data['password']
        password2=request.data['password2']
        if User.objects.filter(username=username).exists():
            return Response({'error':'an user with that username already exists!'}) 
        if password!=password2:
            return Response({'error':'Two password didnt matched!'})
        user=User()
        user.username=username
        user.email=email
        user.first_name=first_name
        user.last_name=last_name
        user.is_active=True
        
        user.set_password(raw_password=password)
        user.save()     
        return Response({"success":"User registration successfull."})
from .serializers import *
class ContactApiView(APIView):
    permission_classes=([AllowAny])
    def post(self,request,format=None): 
        # this code work for django.
        ''' data=request.data
        form=ContactForm(request.POST)
        if form.is_valid():
            form.save() '''
            
        serializer=ContactSerializerOne(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    def put(self,request,format=None): 
        contact=Contact.objects.get(id=6)
        serializer=ContactSerializerOne(data=request.data, instance=contact)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
        #return Response({'success':'Successfully saved contact'})
    def get(self,request,format=None):
        queryset=Contact.objects.get(id=6)
        serializer=ContactSerializerOne(queryset,many=False)
        return Response(serializer.data)

from rest_framework.generics import CreateAPIView
from .models import BlogPost 
from rest_framework import status

class PostCreateView(CreateAPIView):
    permission_classes=[IsAuthenticated,]
    queryset=BlogPost.objects.all()
    serializer_class=BlogPostSerializer
    
    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
        
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance= self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        
        serializer=PostDetailsSerializer(instance=instance, many=False)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)