const form = document.querySelector("form");
const bosy = document.querySelector("body");

function validatePasswordLength(password) {
    return password.length >= 6;
}

function validateFormInput(event) {
    event.preventDefault();
    const login = document.querySelector("#login"); 
    const password = document.querySelector("#password"); 
    const passwordIsValid = validatePasswordLength(password.value); 
    console.log("event", event);
    console.log("login", login.value);
    console.log("password", password.value);
    console.log("passwordIsValid", passwordIsValid);

    if (!passwordIsValid) {
        password.classList.add("red-border");
    }
}

form.addEventListener("submit", validateFormInput);
form.addEventListener("submit", (event) => console.log(event))