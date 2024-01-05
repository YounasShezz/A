
from django.urls import path
from ubersys import views as v
urlpatterns = [
    path('map/m', v.mapy),
    path('map/m/dot', v.dot,name="dot"),
    path('map/m/m', v.async_view),
    path('map/m/<str:id>', v.recvid),
    path('', v.service),
    
]
