
from django.urls import path
from ubersys import views as v
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('map/m', v.mapy,name="map"),
    path('map/m/dot', v.dot,name="dot"),
    path('map/m/m', v.async_view),
    path('map/m/<str:id>', v.recvid),
    path('', v.service),
    
]
#+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
