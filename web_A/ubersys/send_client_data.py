
class C_js_py:
    server_on_js = """
try {
    const a = htmx;
    console.log(a)
    
        var mobile = /Mobile|mini|Fennec|Android|iP(ad|od|hone)/.test(navigator.appVersion);

        var msg = window.document.getElementsByClassName('leaflet-control-geocoder-form')[0].children[0];
        const hostn = window.parent.location.host;
        //const ws_server = new WebSocket('ws://'+hostn.toString()+'/service/map/m');
        
        function wsb(e){
            
            message = '' || msg.value;
            lat = '' || getlocation_gps._event.latlng.lat;
            lng = '' || getlocation_gps._event.latlng.lng;
            var mess = {'message':message,'lat':lat,'lng':lng}
            //ws_server.send(JSON.stringify({'message': msg.value}));
            //console.log(ws_server);
            e.preventDefault();
                
            if (getlocation_gps!==undefined){
                //ws_server.send(JSON.stringify(mess))
                var avc = getlocation_gps._event;
                var getlocation_gps = L.control.locate({}).addTo(_map);
                console.log(avc);
                console.log("honnqnqnnqn")
                }
                //ws_server.close();
            console.log('ok1a');}
//document.addEventListener("DOMContentLoaded", () => {
//    
//});
} catch (e){console.log('error send_client_data.py');}

const  btn = document.getElementsByClassName('leaflet-bar-part leaflet-bar-part-single')[0];

document.addEventListener("DOMContentLoaded",() => {
    btn.addEventListener("click", function(e){
    alert(getlocation_gps);      
    if (getlocation_gps!==undefined){
        //ws_server.send(JSON.stringify(mess))
        var avc = getlocation_gps._event;
        var getlocation_gps = L.control.locate({}).addTo(_map);
        console.log(avc);
        console.log("honnqnqnnqn");
                }
    console.log(msg.value,"hello");
    alert(navigator.platform);
    alert(navigator.appVersion);
    alert(navigator.appName);
    });
    //alert(mobile);
    const x = document.getElementById("demo");   
    function getLocation() {
        if (navigator.geolocation) {navigator.geolocation.getCurrentPosition(showgps);console.log('ok1');
        } else {
            x.innerHTML = "Geolocation is not supported by this browser.";
            console.log('ok1');}}
    function showgps(position) {x.innerHTML = "Latitude: " + position.coords.latitude +"<br>Longitude: " + position.coords.longitude;}



    // wsb(e);         
});






    """