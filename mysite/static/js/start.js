const btn = document.querySelector(".js-btn");

function begin() {
  console.log("start");
  location.href="form/"
}

function init() {
    btn.addEventListener("click", begin);
}

init();
