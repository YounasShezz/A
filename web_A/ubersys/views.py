from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.middleware.csrf import get_token
from folium import  ClickForMarker,ClickForLatLng,LatLngPopup
from folium.plugins import Geocoder,LocateControl,Search,Fullscreen
import asyncio
from time import sleep
import clipboard
import httpx
from html import escape
from branca.element import Figure,Element
import folium
from ubersys.MapConfigu import Map
from ubersys import funhtml as fun,send_client_data
from django.contrib.auth import (
    BACKEND_SESSION_KEY,)





async def http_call_async():
  for num in range(1,6):
    await asyncio.sleep(1)
    print(num)
  async with httpx.AsyncClient() as client:
    r = await client.get("https://httpbin.org")
    print(r)

async def async_view(request):
  loop = asyncio.get_event_loop()
  await loop.create_task(http_call_async())
  return HttpResponse('Non-blocking HTTP request')
# Create your views here.

def mapy(request):
    print(BACKEND_SESSION_KEY)
    #d = {"zoom_start":17,'location':[ -0.27462011299984185,33.55129184778379]}
    #fig = Figure(width=550,height=350)
    #fig._template = fun.HtmlH().page
    #########tiles='https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',attr='Tiles &copy; Esri &mdash; Source: Esri, i-cubed, USDA, USGS, AEX, GeoEye, Getmapping, Aerogrid, IGN, IGP, UPR-EGP, and the GIS User Community'
    m1 = folium.Map(location=[28.644800, 77.216721],zoom_start=18,tiles='https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png',attr='https://www.openstreetmap.org/copyrigh');m1._id = "map";m1._name = "_";m1.add_child(folium.ClickForLatLng(format_str='"[" + lat + "," + lng + "]"', alert=False))
    LatLngPopup().add_to(m1);Fullscreen().add_to(m1);Geocoder().add_to(m1);LatLngPopup().add_to(m1);folium.Marker([0.0,0.0]).add_to(m1);aa=LocateControl();aa._id='gps';aa._name="getlocation";aa.add_to(m1)
    #s = "<button  hx-post=/service/  >this gps</button>"
    #folium.Marker([28.644800, 77.216721],popup= s).add_to(m1)
    #flyTo=True,auto_start=True)
    #LocateControl(strings={"popup":"<b>Lat:</b> ${lat}<br /><b>Lon:</b> ${lng}"}).add_to(m1)
    #aa['strings']={"popup":"<b>Lat:</b> ${lat}<br /><b>Lon:</b> ${lng}"}
    #m1.add_child(folium.LayerControl(position='topright',collapsed=True,))
    aaa = Element(send_client_data.C_js_py.server_on_js);m1 = m1.get_root();m1.script.get_root().render();m1.script._children[aaa.get_name()]=aaa
    ee = Element(fun.HtmlH.add_jjs(fun.HtmlH,"jjs"));m1 = m1.get_root();m1.script.get_root().render();m1.script._children[ee.get_name()]=ee
    #folium.add_child(ClickForMarker(popup="<b>Lat:</b> ${lat}<br /><b>Lon:</b> ${lng}"))
    m = m1._repr_html_()
    return render(request,'map.html',{"m":m})#{'m':d}) 

def recvid(request):

    return render(request,'map.html') 
def dot(request,id):
    print(id)

    return render(request,'map.html') 
def service(request):
    if request.POST:
       print(request.POST)
       print("وصلت الحمدلله رب العالمين")
    print("dqsfd")
    return render(request,'htmx.html')
