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
class ContactApiView(APIView):
    permission_classes=([AllowAny])
    def post(self,request,format=None): 
        data=request.data
        name=data['name']
        email=data['email']
        subject=data['subject']
        phone=data['phone']
        details=data['details']
        
        contact=Contact(name=name,email=email,subject=subject,phone=phone,details=details)
        contact.save()
        return Response({'success':'Successfully saved contact'})
    def get(self,request,format=None):
        return Response({'success':'Successfully from get'})