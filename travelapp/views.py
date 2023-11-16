from django.http import HttpResponse
from django.shortcuts import render
from .models import place
from .models import team

# Create your views here.
def demo(request):
    obj=place.objects.all()

    return render(request,"index.html",{'result':obj})

def demo(request):

    tem=team.objects.all()
    return render(request,"index.html",{'team':tem})