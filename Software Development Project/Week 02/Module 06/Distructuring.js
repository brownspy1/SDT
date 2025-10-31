// object Distructuring 
const user = {
    name: "M.Mahadi",
    age:20,
    skrill:["C","C++","html","Css","python","java","js","php"]
}

let {name,age,skrill} = user;

console.log(name);
console.log(age);
console.log(skrill);

// list Distructuring 
let list = ["C","C++","html","Css","python","java","js","php"];

let [one,two,three,four,five] = list;

console.log(one,three,five);
