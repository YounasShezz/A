import openrouteservice as ors
import folium

def route_on_map():    
    client = ors.Client(key='5b3ce3597851110001cf6248ba3731fdcaf24a8590b3de1441910bcc')
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
