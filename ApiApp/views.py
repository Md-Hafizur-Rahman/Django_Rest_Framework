from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from rest_framework.views import APIView

# Create your views here.
class HomeView(TemplateView):
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
        return Response(context)