from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import *

# Create your views here.


def sample(request):
    p1 = Dept.objects.create(dname="BusinessAnalyst", location='BANGALORE')
    p1.save()
    return HttpResponse("Value inserted")
