from django.shortcuts import render

# Create your views here.


def H_taxi(request):
    return render(request,'taxi/H_taxi.html')