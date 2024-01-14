from django.urls import re_path

from ubersys import consumers

websocket_urlpatterns = [
    re_path(r"service/map/m", consumers.ChatConsumer.as_asgi()),
]