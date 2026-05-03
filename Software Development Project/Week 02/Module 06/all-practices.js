// const mobile = [
//   {"id": 1,"mobile_name": "iPhone 15 Pro","price": 1200,"color": "Black"},
//   {"id": 2,"mobile_name": "Samsung Galaxy S24","price": 999,"color": "Black"},
//   {"id": 3,"mobile_name": "Google Pixel 8","price": 899,"color": "Mint Green"},
//   {"id": 4,"mobile_name": "OnePlus 12","price": 850,"color": "Glacial Silver"},
//   {"id": 5,"mobile_name": "Xiaomi 14 Pro","price": 750,"color": "Black"}
// ]
// ------------- variable assaing in es6 ---------------
// const name = "M.Mahadi";
// console.log(name);
// let bro = "Mahir";
// console.log(bro);
// bro = "Mahadi";
// console.log(bro);

// -------------- templat literal ------------------

// const name = "M.Mahadi";
// const age = 25;
// const city = "Dhaka";

// let details = `My name is ${name},\nI am ${age} and \nI am live in ${city}`
// console.log(details);

//-------------- sprad opration ---------------------
// const list = [1,2,3,4,5,6,7,8,9,10];
// const list2 = [11,12,13,14,15,16,17,18,19,20];

// let max_value = [...list,...list2];
// const max_num = Math.max(...max_value);
// console.log(...max_value);
// console.log(max_num);

//-------------- object distactuary ------------------
// const user = {
//     "name":"brownspy1",
//     "password":"#@7dfsi",
//     "email":"mh0643893@gmail.com"
// }
// const {name,password,email} = user;
// console.log(name);

// ------------- arry diistactury --------------------
// const list = ["M.Mahadi",{"age":21,"hight":5.6},"Barisal"];
// let [name,halth,livein] = list;

// console.log(name + '\n' +halth + '\n' + livein);

//-------------- arrow function ----------------------
// function add(a=0,b=0){
//     return a+b;
// }
// // const add = (a=0,b=0)=>{
// //     return a+b;
// // }
// // console.log(add(10,20));
//------------------- Object find -------------------------
// const mobiles = [
//   {"id": 1,"mobile_name": "iPhone 15 Pro","price": 1200,"color": "Black"},
//   {"id": 2,"mobile_name": "Samsung Galaxy S24","price": 999,"color": "Black"},
//   {"id": 3,"mobile_name": "Google Pixel 8","price": 899,"color": "Mint Green"},
//   {"id": 4,"mobile_name": "OnePlus 12","price": 850,"color": "Glacial Silver"},
//   {"id": 5,"mobile_name": "Xiaomi 14 Pro","price": 750,"color": "Black"}
// ]

// const mobile = mobiles.find(values=>{
//     return values.id == 2
//     });

// console.log(mobile.mobile_name);

//--------------- object filter ------------------------
// const mobiles = [
//   {"id": 1,"mobile_name": "iPhone 15 Pro","price": 1200,"color": "Black"},
//   {"id": 2,"mobile_name": "Samsung Galaxy S24","price": 999,"color": "Black"},
//   {"id": 3,"mobile_name": "Google Pixel 8","price": 899,"color": "Mint Green"},
//   {"id": 4,"mobile_name": "OnePlus 12","price": 850,"color": "Glacial Silver"},
//   {"id": 5,"mobile_name": "Xiaomi 14 Pro","price": 750,"color": "Black"}
// ]

// const mobile = mobiles.filter(value=>{
//     return value.color == "Black";
// })

// console.log(mobile);

//--------------------- foreach map ----------------------------------------

// const Mobile = mobiles.forEach(value=>{
//     console.log(value.mobile_name);
// })

// ------------------- map -----------------------------
// const mobile = mobiles.map(value=>{
//     return value.price+10;
// })

// console.log(...mobile);


//-------------------- find odd and even from list --------

// const list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20];

// const finds = (ar = [],vl = 1) => {
//     const list_of_odd = [];
//     const list_of_evn = [];

//     for (let i = 0; i < ar.length; i++) {
//         const element = ar[i];
//         if (element % 2 == 0) {
//             list_of_evn.push(element);
//         } else {
//             list_of_odd.push(element);
//         }
//     }

//     if (vl == 1) {
//         return list_of_evn;
//     }else{
//         return list_of_odd;
//     }
// }

// console.log(...finds(list,0));


//----------find big text from -------------

const list = ["mahadi","rafik","jabbar","karim00000000","Bangladesh"];

const big_text = (array)=>{
    let big = array[0];

    for (let i = 0; i < array.length; i++) {
        const element = array[i];
        if (big.length < element.length) {
            big = element;
        }
    }
    return big;
}

console.log(big_text(list));