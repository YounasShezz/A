from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
import certbot_django.server.urls
from web_A import views as v
urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('a/b/c/', include("globalproject.urls")),
    path('service/', include("ubersys.urls")),
    path('/', include("shopping.urls")),
    path('', include('taxi.urls')),
    path('', v.home_web_A),
    path(r'^\.well-known/', include(certbot_django.server.urls)),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)