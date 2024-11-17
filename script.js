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
    .then((response) => response.json())
    .then((data) => {
      data.forEach((country) => {
        if (country?.currencies != null) {
          let currencyKey = Object.keys(country.currencies)[0];
          let option1 = document.createElement("option");
          let option2 = document.createElement("option");

          option1.value = currencyKey;
          option2.value = currencyKey;

          option1.text =
            currencyKey + " - " + country.currencies[currencyKey].name;
          option2.text =
            currencyKey + " - " + country.currencies[currencyKey].name;

          const flagUrl = `https://flagcdn.com/w320/${country.cca2.toLowerCase()}.png`;

          option1.setAttribute("data-image", flagUrl);
          option2.setAttribute("data-image", flagUrl);

          option1.setAttribute(
            "data-symbol",
            country.currencies[currencyKey].symbol
          );
          option2.setAttribute(
            "data-symbol",
            country.currencies[currencyKey].symbol
          );

          option1.setAttribute(
            "data-currency",
            country.currencies[currencyKey].name
          );
          option2.setAttribute(
            "data-currency",
            country.currencies[currencyKey].name
          );

          option1.setAttribute("data-name", country.name.common);
          option2.setAttribute("data-name", country.name.common);

          fromCoutry.appendChild(option1);
          toCountry.appendChild(option2);
        }
      });

      // Ordenar as opções
      sortOptions(fromCoutry);
      sortOptions(toCountry);

      // Configurar valores padrão
      fromCoutry.value = "INR";
      toCountry.value = "USD";

      setCurrenctSymbol();
      setSelectedCountry(fromCoutry, selectedFromImg);
      setSelectedCountry(toCountry, selectedToImg);
    });
});

function setCurrenctSymbol() {
  let selectedCrSymbol =
    fromCoutry.options[fromCoutry.selectedIndex].getAttribute("data-symbol");
  selectedSymbol.innerHTML = selectedCrSymbol;
}

function setSelectedCountry(optionElement, imgElement) {
  let selectedCrImg =
    optionElement.options[optionElement.selectedIndex].getAttribute(
      "data-image"
    );
  imgElement.setAttribute("src", selectedCrImg);
}

function sortOptions(selectElement) {
  let options = Array.from(selectElement.options);

  // Remover duplicatas e ordenar
  let uniqueOptions = [
    ...new Map(options.map((item) => [item.text, item])).values(),
  ];

  uniqueOptions.sort((a, b) =>
    a.getAttribute("data-name").localeCompare(b.getAttribute("data-name"))
  );

  // Atualizar o select com as opções ordenadas
  selectElement.innerHTML = "";
  uniqueOptions.forEach((option) => selectElement.appendChild(option));
}
