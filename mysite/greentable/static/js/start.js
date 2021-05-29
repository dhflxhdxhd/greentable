const main = document.querySelector("#main");
const qna = document.querySelector("#qna");
const result = document.querySelector("#result");
const start_button = document.querySelector(".js-start");
var qnaBox = document.querySelector(".js-qnaBox");
const endPoint = 4;
const select = [];

result.style.display = "none";

function setResult(){

}

function calResult(){

}


function goResult(){
    qna.style.display = "none";
    result.style.display = "block";

    setResult();
}

function addAnswer(answerText, qId, Id){
    var answer = document.querySelector(".js-answerBox");
    var answerBtn = document.createElement('button');

    answerBtn.classList.add('answerList');
    answer.appendChild(answerBtn);
    answerBtn.innerHTML = answerText;

    answerBtn.addEventListener("click",function(){
        var children = document.querySelectorAll(".answerList");

        select[qId] = Id;  // 결과 페이지 : 선택한 번호.
        console.log(select);

        for(let i=0; i<children.length; i++){
            children[i].disabled = true;
            children[i].style.display = "none" ;
        }
        goNext(++qId);
    },false);
}

function goNext(qId) {

    if(qId == endPoint ){
        goResult();
        return;
    }

    qnaBox.innerHTML = qnaList[qId].q;
    for (let i in qnaList[qId].a) {
        addAnswer(qnaList[qId].a[i].answer,qId, i);
    }
}

function begin() {
    main.style.display = "none";
    qna.style.display = "block"

    let qId = 0;
    goNext(qId);
}

function init() {
    start_button.addEventListener("click", begin);
}

init();
