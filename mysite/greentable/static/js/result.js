
let loc = `{{locate}}`;
let place = `{{name}}`;

var mapContainer = document.getElementById('map'), // 지도를 표시할 div
    mapOption = {
        center: new kakao.maps.LatLng(33.450701, 126.570667), // 지도의 중심좌표
        level: 3 // 지도의 확대 레벨
    };

var map = new kakao.maps.Map(mapContainer, mapOption);
var geocoder = new kakao.maps.services.Geocoder();

geocoder.addressSearch(loc, function(result, status) {

     if (status === kakao.maps.services.Status.OK) {
        var coords = new kakao.maps.LatLng(result[0].y, result[0].x);

        var marker = new kakao.maps.Marker({
            map: map,
            position: coords,
        });

        var infowindow = new kakao.maps.InfoWindow({
            content: '<div style="width:150px;text-align:center;padding:6px 0;">'+place +'</div>'
        });
        infowindow.open(map, marker);
        map.setCenter(coords);
    }
});
