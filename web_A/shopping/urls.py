
from django.urls import path,include
from shopping import views as v
urlpatterns = [
    path('admin/', v.home),
]