from django.http import HttpResponse
from django.shortcuts import render
import pathlib



def home_page_view(request,*args,**kwargs):#args and kwargs are for any other types of arguments
    html_template='templates/base.html'
    page_title='basehtmlpage'
    context={
        'my_title':page_title
    }
    return render(request,html_template,context)