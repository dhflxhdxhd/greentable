const btn = document.querySelector(".js-btn");
const mapbtn = document.querySelector('.js-mapbtn');



function MovetoMap() {
    console.log("지도 페이지로 이동");
    location.href="map/"
}

function begin() {
  console.log("start");
  location.href="form/"
}

function init() {
    btn.addEventListener("click", begin);
    mapbtn.addEventListener("click", MovetoMap);
}

init();
