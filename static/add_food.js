function loadYelp(ele) {
    if(event.key === 'Enter') {
    var tmp = ele.value;
    var xhttp = new XMLHttpRequest();

    tmp = tmp.split('/')[4];
    tmp = tmp.split('?');
    var restaurant = tmp[0];
    var img_id = tmp[1].replace("select=", "");

    tmp = "load?restaurant=" + restaurant + "&img_id=" + img_id;

    xhttp.onreadystatechange = function() {
        if (xhttp.readyState === 4) {
//            console.log(xhttp.response);
            var img = document.createElement("img");
            var tag = document.getElementById("pic");
            while(tag.firstChild){
                tag.removeChild(tag.firstChild);
            }
            img.src = JSON.parse(xhttp.response)['img_src'];
            img.style.height = '340px';
            img.style.width = "400px";
            tag.appendChild(img);


            var address = JSON.parse(xhttp.response)["address"];
            var restaurant = JSON.parse(xhttp.response)["restaurant"];
            var tag = document.getElementById("form");
            var restaurant_input = tag.getElementsByTagName("input")[0];
            restaurant_input.value = restaurant;

            var address_input = tag.getElementsByTagName("input")[1];
            address_input.value = address;
            tag.style.display = "block";
            }
        }
    xhttp.open("GET", "add/"+tmp, true);
    xhttp.send();
    }
}


function godb(tag){
    var form = tag.parentElement;
    var img_src = document.getElementById("pic").firstChild.src;
    var restaurant = form.getElementsByTagName("input")[0].value;
    console.log(restaurant);
    restaurant = restaurant.replace("&", "%and%")
    console.log(restaurant);
    var address = form.getElementsByTagName("input")[1].value;
    var price = form.getElementsByTagName("input")[2].value;
    var tmp = "load?restaurant=" + restaurant + "&img_src=" + img_src + "&price=" + price;

    var xhttp = new XMLHttpRequest();
    xhttp.open("POST", "add/"+tmp, true);
    xhttp.send()
}







function populateInfoWindow(marker, infowindow) {
    // Check to make sure the infowindow is not already opened on this marker.
    if (infowindow.marker != marker) {
        infowindow.marker = marker;
        infowindow.setContent('<div>' + marker.title + '</div>');
        console.log(marker.title)
        infowindow.open(map, marker);
        // Make sure the marker property is cleared if the infowindow is closed.
        infowindow.addListener('closeclick',function(){
            infowindow.setMarker = null;
        });
    }
}
