fetch("https://jsonplaceholder.typicode.com/users")
.then(response => response.json())
.then(data => {
    getUser(data);
    
}).catch((Error) => {
    console.log(Error);
    
})

const getUser = (users_data)=>{
    const container = document.getElementById("user_contrainer");

    users_data.forEach((user) => {
        const div = document.createElement("div");
        div.classList.add("user");

        div.innerHTML = `
              <h3>${user.name}</h3>
              <p>${user.email}</p>
              <button>details</button>
        `;
        container.appendChild(div);
        console.log(user);
        

    });
}