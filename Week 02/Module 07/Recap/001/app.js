const target = document.getElementById("titel");
target.style.color = "red";
console.log("Hello");

const allBox = document.getElementsByClassName("box");


for (let i = 0; i < allBox.length; i++) {
    const element = allBox[i];
    element.style.backgroundColor = "red";
    let orginal = element.style.backgroundColor;
    element.addEventListener("click", () => {
        if (element.style.backgroundColor == "black" && element.innerText != "box 5") {
            element.style.backgroundColor = orginal;
        } else if (element.style.backgroundColor == "black" && element.innerText == "box 5") {

        
            element.style.backgroundColor = "green";
        } else {
            element.style.backgroundColor = "black";

        }
    })

    if (element.innerText == "box 5") {
        element.style.backgroundColor = "green";
        element.style.borderColor = "green";
    }
}

const abc = (e)=>{
    console.log(e);
}
// console.log(allBox);