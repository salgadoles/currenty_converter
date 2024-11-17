const amount = document.getElementById("amount"),
fromCoutry = document.getElementById("fromCountry"),
toCountry = document.getElementById("toCountry"),
selectedSymbol = document.getElementById("selectedSymbol"),
selectedFromImg = document.getElementById("selectedFromImg"),
selectedToImg = document.getElementById("selectedToImg"),
Rotate = document.querySelector(".form-control i"),
formOutput = document.querySelector(".form-output");

window.addEventListener("load", () => {
    fetch("https://restcountries.com/v3.1/all")
    .then((response)=>response.json())
    .then((data) =>{
      data.forEach((country) => {
        if (country?.currencies != null) {
            console.log(country.currencies);
         let currencyKey =Object.keys(country.currencies)[0]
            let option1 = document.createElement("option");
            let option2 = document.createElement("option");
            option1.value=currencyKey;
            option2.value=currencyKey;
        
            option1.text=
                currencyKey+" - "+country.currencies[currencyKey].name;
            option2.text=
                currencyKey+" - "+country.currencies[currencyKey].name;

            fromCoutry.appendChild(option1);
            toCountry.appendChild(option2);
        }  
    });
});
});
