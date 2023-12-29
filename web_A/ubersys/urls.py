
from django.urls import path
from ubersys import views as v
urlpatterns = [
    path('map/m', v.mapy),
    path('map/m/dot', v.dot,name="dot"),
]
