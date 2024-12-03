from django.shortcuts import render

# Create your views here.
import datetime

def server(request):
    date=datetime.datetime.now()
    dic={'insert':date}
    return render(request,'date.html',context=dic)