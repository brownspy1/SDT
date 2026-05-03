fetch("https://jsonplaceholder.typicode.com/users")
    .then(res => res.json())
    .then(data => {
        showAlluser(data);
        console.log('data send to function!');
        console.log(data);
    })

const showAlluser = (users) => {
    const conatainer = document.getElementById("users");
    users.forEach((user) => {
        let { name, email, website, phone } = user;
        const div = document.createElement("div");
        div.classList.add('user-card');

        div.innerHTML = `
        <h1 class="defult-image">${name[0]}</h1>
        <h3>${name}</h3>
        <p>${email}</p>
        <h4>${phone}</h4>
        <a href="${website}">Go to site</a>`;
        conatainer.appendChild(div)
    
    })
}