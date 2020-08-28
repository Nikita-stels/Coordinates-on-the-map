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
    request.open("POST", "http://127.0.0.1:8888/api/v2/web_get_map");
    request.setRequestHeader('Content-type', 'application/json; charset=utf-8');
    request.send(json);
    request.onload = () => console.log(request.response)
    request.onload = function () {
        if (request.status == "200") {
            console.log(request)
            document.write(request.responseText);
            // РАЗОБРАТЬСЯ СО СТАТУС КОДОМ И ВЫВОДОМ HTML
            obj = JSON.parse(request.response);

            obj_status = obj.status
            if (obj_status == false){
                alert('You entered incorrect coordinates, please try again.\nlatitude (0 to 90)\nlongitude (0 to 180)\nradius (up to 100)\n\nClick "OK" to continue')
                window.location.reload(); 
            }
            if (obj_status == "not_point")
                alert('There are no points in this radius!\nClick "OK" to continue')
                window.location.reload(); 
    }

}
  };