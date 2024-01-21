var s = null;
var latlng = null;
function delMerkafa() {
    if(_map._panes.markerPane.childElementCount != 0){
        _map.removeLayer(s);
    }
}

document.addEventListener('DOMContentLoaded', (e)=>{
    var csrf = window.parent.document.body.getAttribute('hx-headers');
    document.body.setAttribute('hx-headers', csrf);
    document.body.setAttribute('class', "younes");

    /// HTML

    let deleteBtn = '<button id="delMarker" onclick="delMerkafa();">Delete</button>';
    let sendBtn = `<button id="sendPosition"  hx-post="/service/ hx-include="[X-CSRFToken= "${JSON.parse(csrf)['X-CSRFToken']}"] type="button">Send Position</button>`;
    let sendForm = '<div id="form_locat">'+deleteBtn+'<form hx-post="/service/">'+sendBtn+'<input type="hidden" name="csrfmiddlewaretoken" value="'+JSON.parse(csrf)['X-CSRFToken']+'"></form></div>';
    
    // attention do not supprimmmmm
    let parent_dom = window.parent.document;
    let getEl_parent = function (e){return parent_dom.getElementById(e)};
    let mapActivate = false;
    // attention do not supprimmmmm

    // add marker
    getEl_parent('hadidmawkieak').addEventListener('click', ()=>{
        if(_map._panes.markerPane.childElementCount == 0){
            // document.getElementsByClassName('leaflet-draw-draw-marker')[0].click();
            // getEl_parent('hadidmawkieak').setAttribute('style', 'display:none;');
            // getEl_parent('ihdifmawkieak').setAttribute('style', 'display:block;');

            mapActivate = true;
            console.log(mapActivate);
        }
    });
    console.log(mapActivate);

    _map.on('click',function(e){
        if (mapActivate == true){
            latlng = [e.latlng.lat,e.latlng.lng];
            s=L.marker(latlng).bindPopup(sendForm).addTo(_map);
            mapActivate = false;
        }
    });
});