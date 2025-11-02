fetch("https://jsonplaceholder.typicode.com/users")
.then(response => response.json())
.then(data => {
    console.log(data);
    
}).catch((Error) => {
    console.log(Error);
    
})

const getUser = (users_data)=>{
    const container = document.getElementById("user_contrainer");

    users_data.forEach((user) => {
        const div = document.createElement("div");
        div.classList.add("user");

        div.innerHTML = `
              <h3>Titel</h3>
              <p>para</p>
              <button>details</button>
        `;
        
    });
}