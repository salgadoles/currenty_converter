const amount = document.getElementById("amount"),
fromCoutry = document.getElementById("fromCountry"),
toCountry = document.getElementById("toCountry"),
selectedSymbol = document.getElementById("selectedSymbol"),
selectedFromImg = document.getElementById("selectedFromImg"),
selectedToImg = document.getElementById("selectedToImg"),
//Rotate = Document.querySelector(".form-control i"),
formOutput = document.querySelector(".form-output");

window.addEventListener("load", () => {
    fetch("https://restcountries.com/v3.1/all")
    .then((response)=>response.json())
    .then((data) =>{
        console.log(data);
    });

});
