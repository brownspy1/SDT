const titel = document.getElementById("titel")

titel.style.color="white";

const boxes = document.getElementsByClassName("box");

for (let i = 0; i < boxes.length; i++) {
    const element = boxes[i];
    console.log(element);
    element.style.backgroundColor = "#00ff88ff";
    if (element.innerText == "box4") {
        element.style.backgroundColor = "red";
    }
}

const click_ent = document.getElementById("btn")
.addEventListener("click",(e)=>{
    let input = document.getElementById("inputfilde");
    let input_data = input.value;
    const container = document.getElementById("containar_com");
    const p = document.createElement('p');
    p.classList.add("task");
    p.innerText=input_data;
    console.log(p);
    container.appendChild(p);
    input.value = "";
    


    let alltags = document.getElementsByClassName("task");
    for(const item of alltags){
        item.addEventListener("click",(e)=>{
            // item.style.backgroundColor="green";
            e.target.parentNode.removeChild(item);
        });
    }


});