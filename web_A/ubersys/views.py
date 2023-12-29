from django.shortcuts import render
from folium import Map, ClickForMarker
from ubersys.MapConfigu import Mapg
from folium.plugins import Geocoder,LocateControl
from folium.plugins import Search
import folium

# Create your views here.
dicted = {"m":Map,'create_dot':ClickForMarker()}
def mapy(request):
    #d=dicted["m"](location=[33.54625554856057, -0.27859149632496194],width='50%',zoom_start=14,)._repr_html_()
    d = {'width':"50%","height":"50%",'location':[0,0]}
    m = Mapg().getMap(**d)
    sea  =  Geocoder().add_to(m)
    ssea = Geocoder().add_to(m)
    LocateControl().add_to(m)
    folium.Marker(location=[0,0],tooltip='click here',popup='<button type="button">hello</button>').add_to(m)
    m= m._repr_html_()
    #m.fit_bounds([[33.49287793763297, -0.42423398786667726], [33.635917272959915, 0.0866302181259037]])

    return render(request,'map.html',{"m":m})#{'m':d}) 

def dot(request):

    return render(request,'map.html') 
