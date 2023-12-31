from django.shortcuts import render
from folium import  ClickForMarker
from ubersys.MapConfigu import Map
from folium.plugins import Geocoder,LocateControl
from folium.plugins import Search
import folium
import openrouteservice as ors
import asyncio
from time import sleep
import httpx
from django.http import HttpResponse
import  branca 


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

def mapy(request):
    print(branca.element.Element)
    #d=dicted["m"](location=[33.54625554856057, -0.27859149632496194],width='50%',zoom_start=14,)._repr_html_()
    d = {"zoom_start":17,'width':"50%","height":"50%",'location':[33.55129184778379, -0.27462011299984185]}
    m = Map(**d)
    m._id='test'
    client = ors.Client(key='5b3ce3597851110001cf6248ba3731fdcaf24a8590b3de1441910')
    coords = [[ -0.27704977068507586,33.55512075616771]]
    vehicle_start = [ -0.2785127273139839,33.5534685032053]

    for coord in coords:
        folium.Marker(location=list(reversed(coord))).add_to(m)
    
    folium.Marker(location=list(reversed(vehicle_start)), icon=folium.Icon(color="red")).add_to(m)  

    vehicles = [
        ors.optimization.Vehicle(id=0, profile='driving-car', start=vehicle_start, end=vehicle_start, capacity=[5])]
    jobs = [ors.optimization.Job(id=index, location=coords, amount=[1]) for index, coords in enumerate(coords)]
    optimized = client.optimization(jobs=jobs, vehicles=vehicles, geometry=True)
    line_colors = ['green', 'orange', 'blue', 'yellow']
    for route in optimized['routes']:
        folium.PolyLine(locations=[list(reversed(coords)) for coords in ors.convert.decode_polyline(route['geometry'])['coordinates']],
                         color=line_colors[route['vehicle']]).add_to(m)
    sea  =  Geocoder().add_to(m)
    ssea = Geocoder().add_to(m)
    a= LocateControl()
    a._id='loc'
    my_jss = '''
    var ma = document.getElementById("map_{}");
    console.log(ma)
    '''.format(a._id)

    a.get_root().script.add_child(Element(my_jss)).add_to(m)

    my_js = '''
    var ma = document.getElementById("map_{}");
    console.log(ma)
    '''.format(m._id)
    m.get_root().script.add_child(Element(my_js))
    folium.Marker(location=[0,0],tooltip='click here',popup='<button type="button">hello</button>').add_to(m)
    m= m._repr_html_()
    #m.fit_bounds([[33.49287793763297, -0.42423398786667726], [33.635917272959915, 0.0866302181259037]])

    return render(request,'map.html',{"m":m})#{'m':d}) 

def dot(request):

    return render(request,'map.html') 
