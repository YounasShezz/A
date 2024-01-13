Function.prototype.extend = function(parent) {
    var child = this;
    child.prototype = parent;
    child.prototype.$super = parent;
    child.prototype = new child(Array.prototype.slice.call(arguments,1));
    child.prototype.constructor = child
}

//"$(function() {\n"
 // "document.getElementsByClassName('leaflet-control-locate').addEventListener('click', {\n"
 // "  alert('Hiiii');\n"
  //"});\n"
 // "var dt = window.parent.document.getElementById('FormData');\n"
 // "dt.setAttribute('hx-vals', `js:{'lat': '${getlocatttion_gps._event.latlng.lat}','lng': '${getlocatttion_gps._event.latlng.lng}'}`)\n"
//"});\n"