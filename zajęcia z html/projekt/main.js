// Pobranie elementu kontenera obrazów
const track = document.getElementById("image-track");

// Obsługa zdarzenia wciśnięcia myszy lub dotknięcia ekranu
const handleOnDown = e => {
    // Zapisanie pozycji X myszy w momencie wciśnięcia
    track.dataset.mouseDownAt = e.clientX;
};

// Obsługa zdarzenia puszczenia myszy lub zakończenia dotknięcia ekranu
const handleOnUp = () => {
    // Zresetowanie pozycji X myszy
    track.dataset.mouseDownAt = "0";
    // Zapisanie poprzedniego procentowego przesunięcia obrazu
    track.dataset.prevPercentage = track.dataset.percentage;
};

// Obsługa zdarzenia przesuwania myszy lub dotykania ekranu
const handleOnMove = e => {
    // Sprawdzenie, czy mysz jest wciśnięta
    if (track.dataset.mouseDownAt === "0") return;

    // Obliczenie różnicy w położeniu X myszy od momentu wciśnięcia
    const mouseDelta = parseFloat(track.dataset.mouseDownAt) - e.clientX;
    // Obliczenie maksymalnej możliwej różnicy w położeniu X
    const maxDelta = window.innerWidth / 2;

    // Obliczenie procentowego przesunięcia obrazu
    const percentage = (mouseDelta / maxDelta) * -100;
    // Obliczenie nowego procentowego przesunięcia obrazu
    const nextPercentageUnconstrained = parseFloat(track.dataset.prevPercentage) + percentage;
    const nextPercentage = Math.max(Math.min(nextPercentageUnconstrained, 0), -100);

    // Zapisanie nowego procentowego przesunięcia obrazu
    track.dataset.percentage = nextPercentage;

    // Przesunięcie kontenera obrazów o obliczone procentowe przesunięcie
    track.style.transform = `translate(${nextPercentage}%, -50%)`;

    // Dla każdego obrazu w kontenerze ustawienie pozycji obiektu w zależności od przesunięcia
    for (const image of track.getElementsByClassName('image')) {
        image.style.objectPosition = `${100 + nextPercentage}% center`;
    }
};

// Przypisanie funkcji obsługi zdarzenia wciśnięcia myszy
window.onmousedown = e => handleOnDown(e);

// Przypisanie funkcji obsługi zdarzenia dotknięcia ekranu
window.ontouchstart = e => handleOnDown(e.touches[0]);

// Przypisanie funkcji obsługi zdarzenia puszczenia myszy
window.onmouseup = e => handleOnUp(e);

// Przypisanie funkcji obsługi zdarzenia zakończenia dotknięcia ekranu
window.ontouchend = e => handleOnUp(e.touches[0]);

// Przypisanie funkcji obsługi zdarzenia przesuwania myszy
window.onmousemove = e => handleOnMove(e);

// Przypisanie funkcji obsługi zdarzenia przesuwania na ekranie dotykowym
window.ontouchmove = e => handleOnMove(e.touches[0]);
