
class C_js_py:
    server_on_js = """
const msg = document.getElementsByClassName('leaflet-control-geocoder-form')[0].children[0].value.toString();
const  btn = document.getElementsByClassName('leaflet-control-geocoder-icon')[0]

const ws_server = new WebSocket(
    'ws://127.0.0.1:8000/service/map/m');

btn.onclick = function(e){
    console.log(msg)
    ws_server.send(JSON.stringify({
        'message': msg
    }));
    }

"""