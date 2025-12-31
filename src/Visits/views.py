

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from.models import *
import pathlib



def home_page_view(request,*args,**kwargs):
    queryset=PageVisit.objects.all()
    html_template='base.html'
    page_title='basehtmlpage'
    context={
        'my_title':page_title,
        'page_visit_count':queryset.count(),
        'total_count':queryset.count()*100/queryset.count(),
    }
    PageVisit.objects.create()
    return render(request,html_template,context)

def index(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html') 
