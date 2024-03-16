const COLORS = ["black", "red", "green", "yellow", "brown"];

const onKeydown = (event) => {
    const keyPressed = event.key;
    const allSquares = document.querySelectorAll(".square");

    if (keyPressed === " ") {
        // Zmiana koloru każdego kwadratu na losowy kolor z tablicy COLORS
        allSquares.forEach(square => {
            const randomColorIndex = Math.floor(Math.random() * COLORS.length);
            square.style.backgroundColor = COLORS[randomColorIndex];
        });
    } else if (keyPressed === "Backspace") {
        // Wypełnienie każdego kwadratu wartością klawisza "Backspace"
        allSquares.forEach(square => {
            square.innerHTML = keyPressed;
        });
    }

}

const body = document.querySelector("body"); // Poprawiono literówkę w selektorze
body.addEventListener("keydown", onKeydown);