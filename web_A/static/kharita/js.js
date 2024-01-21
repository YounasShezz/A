document.body.addEventListener("load", runScript());
function myFunction() {
  // Get the text field
  var copyText = document.getElementsByClassName("lat");

  // Select the text field
  copyText.select();
  copyText.setSelectionRange(0, 99999); // For mobile devices

  // Copy the text inside the text field
  navigator.clipboard.writeText(copyText.value);

  // Alert the copied text
  alert("Copied the text: " + copyText.value);
}
function checkExist() {
  try {
    if (getlocation_gps != 'undefined'){
      return true;
      //csrfmiddlewaretoken
      var csr = window.parent.document.body.getAttribute('csrfg');
      //document.body.setAttribute('')
      dt.setAttribute('hx-vals', `js:{'csrfmiddlewaretoken':'${csr}','lat': '${getlocatttion_gps._event.latlng.lat}','lng': '${getlocatttion_gps._event.latlng.lng}'}`)
    }
  } catch (e) {
    console.log(e);
  }
}

function runScript(ev) {
  if (checkExist === true){
    var la= document.getElementById("cntrl-lat");
    var lo= document.getElementById("cntrl-lng");
    //alert(la,lo);
    la.setAttribute('value', getlocation_gps._event.latlng.lat);
    lo.setAttribute('value', getlocation_gps._event.latlng.lng);
    console.log(ev);
  }else{
    console.log('no data');
  }
}