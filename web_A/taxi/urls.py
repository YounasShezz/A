
from django.urls import path
from taxi import views as v
urlpatterns = [
    path('taxi',v.H_taxi,name="taxi")
]
