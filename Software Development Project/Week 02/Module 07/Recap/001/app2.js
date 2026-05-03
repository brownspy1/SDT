const inputfild = document.getElementById("t-input");
const submit_btn = document.getElementById("btn-sub");

submit_btn.addEventListener("click",(e=0)=>{
    console.log(inputfild.value);
    const taskContainer = document.getElementById("task_container");
    const p = document.createElement("p");
    p.innerText = inputfild.value;
    p.classList.add("task");
    taskContainer.append(p);
    p.addEventListener("click",(e=0)=>{
        e.target.parentNode.removeChild(p);
    })
    inputfild.value = '';

})