const mobile = [
  {"id": 1,"mobile_name": "iPhone 15 Pro","price": 1200,"color": "Titanium Blue"},
  {"id": 2,"mobile_name": "Samsung Galaxy S24","price": 999,"color": "Phantom Black"},
  {"id": 3,"mobile_name": "Google Pixel 8","price": 899,"color": "Mint Green"},
  {"id": 4,"mobile_name": "OnePlus 12","price": 850,"color": "Glacial Silver"},
  {"id": 5,"mobile_name": "Xiaomi 14 Pro","price": 750,"color": "Ceramic White"}
]

// for (let i = 0; i < mobile.length; i++) {
//     const element = mobile[i];
//     if (element.id == 2) {
//         console.log(element);
        
//     }
    
// }

//using find

const result = mobile.find(mobile=>mobile.id==1);
console.log(result);
