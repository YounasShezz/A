from django.shortcuts import  render
from django.http import HttpResponse

def home_web_A(request):
    return render(request,'start_home.html')