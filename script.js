const amount = document.getElementById("amount"),
  fromCountry = document.getElementById("fromCountry"),
  toCountry = document.getElementById("toCountry"),
  selectedSymbol = document.getElementById("selectedSymbol"),
  selectedFromImg = document.getElementById("selectedFromImg"),
  selectedToImg = document.getElementById("selectedToImg"),
  Rotate = document.querySelector(".form-control i"),
  formOutput = document.querySelector(".form-output"),
  clearBtn = document.getElementById("clearBtn");

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

          fromCountry.appendChild(option1);
          toCountry.appendChild(option2);
        }
      });

      sortOptions(fromCountry);
      sortOptions(toCountry);

      fromCountry.value = "INR";
      toCountry.value = "USD";

      setCurrenctSymbol();
      setSelectedCountry(fromCountry, selectedFromImg);
      setSelectedCountry(toCountry, selectedToImg);
    });
});

function setCurrenctSymbol() {
  let selectedCrSymbol =
    fromCountry.options[fromCountry.selectedIndex].getAttribute("data-symbol");
  selectedSymbol.innerHTML = selectedCrSymbol;
}

function setSelectedCountry(optionElement, imgElement) {
  let selectedCrImg =
    optionElement.options[optionElement.selectedIndex].getAttribute("data-image");
  imgElement.setAttribute("src", selectedCrImg);
}

function rotateCurrency() {
  const rotateIcon = document.querySelector(".fa-right-left");
  rotateIcon.classList.toggle("rotate");

  let fromCT = fromCountry.value;
  let toCT = toCountry.value;

  fromCountry.value = toCT;
  toCountry.value = fromCT;

  setCurrenctSymbol();
  setSelectedCountry(fromCountry, selectedFromImg); 
  setSelectedCountry(toCountry, selectedToImg);  
  convertCurrency();
}

function convertCurrency() {
  fetch(
    `https://v6.exchangerate-api.com/v6/cdbcf1df6c8cc80bb2113586/latest/${fromCountry.value}`
  )
    .then((response) => response.json())
    .then((data1) => {
      fetch(
        `https://v6.exchangerate-api.com/v6/cdbcf1df6c8cc80bb2113586/latest/${toCountry.value}`
      )
        .then((response) => response.json())
        .then((data2) => {
          let exchangeRatesFrom = data2.conversion_rates[toCountry.value];
          let totalExchangeRatesFrom = (
            amount.value * exchangeRatesFrom
          ).toLocaleString();

          let exchangeRateTo = data1.conversion_rates[toCountry.value];
          let totalExchangeRateTo = (
            amount.value * exchangeRateTo
          ).toLocaleString();

          let selectedFromCountry =
            fromCountry.options[fromCountry.selectedIndex].getAttribute(
              "data-currency"
            );

          let selectedToCountry =
            toCountry.options[toCountry.selectedIndex].getAttribute(
              "data-currency"
            );

          let lastUpdate =
            "Last update: " +
            data1.time_last_update_utc.split("00:00:01")[0];
          let nextUpdate =
            "Next update on: " +
            data1.time_next_update_utc.split("00:00:01")[0];

          let stringBuilder = "";
          stringBuilder += `<p>${amount.value} ${selectedFromCountry}</p>`;
          stringBuilder += `<p>${totalExchangeRateTo} ${selectedToCountry}</p>`;
          stringBuilder += `<p>${amount.value}${toCountry.value} = ${totalExchangeRatesFrom}${fromCountry.value}<span>${lastUpdate}<br>${nextUpdate}</span> </p>`;
          formOutput.innerHTML = stringBuilder;
        });
    });
}

function clearConversion() {
  amount.value = "";
  selectedSymbol.innerHTML = "";
  selectedFromImg.setAttribute("src", "");
  selectedToImg.setAttribute("src", "");
  formOutput.innerHTML = "";
  fromCountry.value = "";
  toCountry.value = "";
}
