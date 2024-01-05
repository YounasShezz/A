from django.shortcuts import render
from folium import  ClickForMarker
import folium
from ubersys.MapConfigu import Map
from folium.plugins import Geocoder,LocateControl,Search
import asyncio
from time import sleep
import httpx
from django.http import HttpResponse
from django.middleware.csrf import get_token
import  branca 
from html import escape
from jinja2 import Template
from branca.element import Figure
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
#from folium.map import Popup





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
dicted = {"m":Map,'create_dot':ClickForMarker()}


Element = branca.element.Element
@csrf_protect
def mapy(request):
    #d=dicted["m"](location=[33.54625554856057, -0.27859149632496194],width='50%',zoom_start=14,)._repr_html_()
    d = {"zoom_start":17,'width':"50%","height":"50%",'location':[33.55129184778379, -0.27462011299984185]}
    #m = Map(**d)
    fig = Figure(width=550,height=350)
    
    #f1 = fig.script.to_dict()['children']
    #print(f1, '- - ch')
    ssc = request.get_signed_cookie#['CSRF_COOKIE_USED']#CSRF_COOKIE']
    csrf = RequestContext(request)
    print((ssc))
    fig._template = Template(
        "<!DOCTYPE html>\n"
        "<html>\n"
        "<head>\n"
        "{% if this.title %}<title>{{this.title}}</title>{% endif %}"
        "    {{this.header.render(**kwargs)}}\n"
        "<script src=https://unpkg.com/htmx.org@1.9.4/dist/htmx.min.js></script>"
        "</head>\n"
        "<body hx-headers={\"X-CSRFToken\": \"{{ csrf_token }}\"}>\n"

        
        '<form action="" method="post"><div  hx-post=/service/ ></form>'
        "Get Some HTML, Including A Value in the Request</div>"
        "    {{this.html.render(**kwargs)}}\n"
        "</body>\n"
        "<script>\n"
        "    {{this.script.render(**kwargs)}}\n"
        "</script>\n"
        "</html>\n"
    )
    #"<div hx-post=/service/ hx-vals="+{'myVal': 'My Value','aa':'bbb','X-CSRFToken': '"+ssc+"'}\>"

    m1 = folium.Map(location=[28.644800, 77.216721],zoom_start=11)
    
    s = '<button hx-post="/service/" hx-vals={"X-CSRFToken": "{{ csrf_token }}"}>hello</button>'

    folium.Marker([28.644800, 77.216721],popup= s).add_to(m1)
    LocateControl(auto_start=True).add_to(m1)
    m1.add_to(fig)
    m1.add_to(fig)
    m = fig._repr_html_()
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
