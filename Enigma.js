function Enigma() {
    Draw();
}

function Draw() {
    Enigma = document.getElementById("Enigma");
    // 3 Rotors
    Menu = document.createElement("div")
    
    const Enigmas = ["1", "2", "3"];
    for (let X = 0; X < 3; X++) {
        Menu.setAttribute("id", Enigmas[X]);
        Enigma.append(Menu)
    }

}