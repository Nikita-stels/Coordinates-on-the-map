elem.onclick = function() {
    var lat = latitude_web.value
    var lon = longitude_web.value
    var rad = Radius_web.value
    console.log(lat, lon, rad)
    var data = {
        latitude: lat,
        longitude: lon,
        radius: rad
    }
    console.log(data)
    var json = JSON.stringify(data);
    var request = new XMLHttpRequest();
    request.open("POST", "http://http://127.0.0.1:8888/api/v2/web_get_map");
    request.setRequestHeader('Content-type', 'application/json; charset=utf-8');
    request.send(json);
    request.onload = () => console.log(request.response)
    request.onload = function () {
        if (request.status == "200") {
            console.log(request.json)
    }
   
}
  };