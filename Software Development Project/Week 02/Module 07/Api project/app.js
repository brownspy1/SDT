

const getracipis = () => {
    console.log("This is click");
    const food_container = document.getElementById("racipis");
    food_container.replaceChildren();
    const user_input = document.getElementById("mealname");
    // const name = user_input.value;
    const name = user_input.value;
    if (name) {
        fetch(`https://www.themealdb.com/api/json/v1/1/search.php?s=${name}`)
            .then(res => res.json())
            .then(data => {
                data.meals.forEach(recipy => {
                    const div = document.createElement("div");
                    const name = recipy.strMeal;
                    const id = recipy.idMeal;
                    document.getElementById("founded").innerText = `Total founded: ${data.meals.length}`;
                    const image = recipy.strMealThumb;
                    div.classList.add("racipiCard");
                    div.innerHTML = /*html*/`
                    <div className="card">
                     <img src="${image}" alt="${name}" class="racipy_image"/>
                     <h3>${name.slice(0, 15)}</h3>
                    </div>`
                    // add event on racipi cards
                    div.addEventListener("click", (e) => {

                        fetch(`https://www.themealdb.com/api/json/v1/1/lookup.php?i=${id}`)
                            .then(res => res.json())
                            .then(data => {
                                const Details = document.getElementById("details");
                                Details.replaceChildren();
                                const div = document.createElement("div");
                                let values = data.meals[0];
                                div.classList.add("details_card");
                                div.innerHTML = /*html*/`
                                <img src="${values.strMealThumb}" alt="" class="details_image"/>
                                <h3>${values.strMeal.slice(0,20)}</h3>
                                <p>${values.strIngredient1}</p>
                                <p>${values.strIngredient2}</p>
                                <p>${values.strIngredient3}</p>
                                <p>${values.strIngredient4}</p>
                                <p>${values.strIngredient5}</p>
                                <p>${values.strIngredient6}</p>
                                <p>${values.strIngredient7}</p>
                                <a href="${values.strYoutube}">See Video</a>
                            `
                                Details.appendChild(div);
                            })


                    })



                    food_container.appendChild(div);
                })
            }).catch(err => {
                const p = document.createElement("p");
                p.classList.add("notfound");
                p.innerText = "Not found!";
                food_container.appendChild(p);
                console.log(err);
            });
    } else {
        const p = document.createElement("p");
        p.classList.add("notfound");
        p.innerText = "Not found!";
        food_container.appendChild(p);
        console.log('Not found!');
    }
}