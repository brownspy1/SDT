let card = [];

const cart_count = document.getElementById("cart_count");
const drink_container = document.getElementById("drinks_api");
const not_faceh = document.getElementById("not_faceh");

fetch("https://www.thecocktaildb.com/api/json/v1/1/random.php")
    .then(res => res.json())
    .then(data => {
        console.log(data.drinks[0]);
        const e = data.drinks[0];
        creat_cocktail_card(e);
    });



const searce_hit = (e = 0) => {
    drink_container.replaceChildren();
    const searce_text = document.getElementById("serceh_text").value;
    if (searce_text === "") {
        alert("Fuck you!")
    }
    fetch(`https://www.thecocktaildb.com/api/json/v1/1/search.php?s=${searce_text}`)
        .then(Request => Request.json())
        .then(data => {
            if (data.drinks === null) {
                not_faceh.classList.remove('d-none');

            } else {
                not_faceh.classList.add('d-none');
                data.drinks.forEach(item => {
                    creat_cocktail_card(item)
                })
            }
            console.log(data.drinks);

        })
}
const creat_cocktail_card = (item = {}) => {
    const div = document.createElement("div");
    div.classList.add("Card_api");
    div.innerHTML = /*html*/`
  <div class="card" style="width: 18rem;">
  <img src="${item.strDrinkThumb}" class="card-img-top" alt="...">
  <div class="card-body">
    <h5 class="card-title">${item.strDrink}</h5>
    <p>Catagory: <span>${item.strCategory}</span></p>
    <p class="card-text">${item.strInstructionsIT.slice(0, 50)}....</p>
    <a href="#" class="btn btn-primary ad-btn" id="" >Add to Cart</a>
    <a href="#" class="btn btn-primary show-btn">Details</a>
  </div>
</div>
    `;
    const ad_btn = div.querySelector(".ad-btn");
    ad_btn.addEventListener("click", () => addCart(item));
    const show_btn = div.querySelector(".show-btn");
    show_btn.addEventListener("click", () => showModal(item));
    drink_container.appendChild(div);
}

const cartsValues = document.getElementById("carts-values");
const addCart = (e = {}) => {
    if (card.length <= 6) {
        const isExist = card.some((object) => object.idDrink === e.idDrink)
        if (isExist) {
            return;
        }
        card.push(e);
        cart_count.innerText = card.length;
        const div = document.createElement("div");
        div.classList.add("carts-item");
        div.innerHTML = /*html*/ `
        <div class="carts-tems-bg  d-flex  justify-content-center align-items-center" >
            <p class=" text1 " style="width: 20%;">${card.length}</p>
          <img src="${e.strDrinkThumb}"  class="cart-image" alt="" srcset="">
          <p class=" text1 " style="width: 40%;">${e.strDrink.slice(0, 5)}</p>
        </div>
        `
        cartsValues.appendChild(div);
    } else {
        alert("Cart is full of 7 item!");
        return;
    }
}


const showModal = (object = {}) => {
    const modalElement = document.getElementById("drinkModal");
    const myModal = new bootstrap.Modal(modalElement);
    const modalBody = document.getElementById("modalBody");
    modalBody.innerHTML = /*html*/ `
        <img src="${object.strDrinkThumb}" alt="" class="image" >
        <h3>${object.strDrink}</h3>
        <p> <b>Drinks Type: </b> <span>${object.strAlcoholic}</span></p>
        <p> <b> Catagory: </b><span>${object.strCategory}</span></p>
        <h4 class="bg-items">Racipi</h4>
        <p>${object.strInstructions}</p>
        <div className="in-cont">
            <h4>Ingredient</h4>
        <div class="d-flex gap-1 ul-cont">
            <ul class="bg-items ul-item" style="width:25% ">${object.strIngredient1}</ul>
            <ul class="bg-items ul-item" style="width:25% ">${object.strIngredient2}</ul>
            <ul class="bg-items ul-item" style="width:25% ">${object.strIngredient3}</ul>
            <ul class="bg-items ul-item" style="width:25% ">${object.strIngredient4}</ul>
        </div>
        </div>
    `
    myModal.show();
}