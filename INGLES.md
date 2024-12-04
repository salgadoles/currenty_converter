

<p align="center">
  <img src="https://umbrasil.org.br/wp-content/uploads/2015/11/2000px-Marys_monogram_Marist_Brothers.svg_.png" alt="Descrição da imagem" width="100" height="100" margin-top=""/>
</p>
<h1 style="text-align: center;">Currency Converter Project</h1>

---
<br>
<br>

# About the Project

<br>
<br>



---

This project was an activity proposed by the teacher [Leonardo Rocha](https://github.com/LeonardoRochaMarista) in the Web Programming 1 course, at [Colégio Marista Ir. Acácio](https://github.com/MaristaIrAcacio). The proposal presented in the classroom was to create a currency converter, which would query a currency exchange API to obtain up-to-date exchange rates. During the development, I chose to create two versions of the converter, using two different programming languages: one in Python and the other in JavaScript. Below, you can check the features of each version, followed by a detailed technical explanation of how the project was implemented.

---
<br>
<br>
<br>

# JavaScript Features

The Currency Converter is a simple and practical tool that allows the conversion between various currencies quickly and accurately. It displays the flags of the corresponding countries and updates the exchange rates in real-time, ensuring always updated information, including the last update date.

The system includes a button to swap the input fields, making the conversion process easier. Additionally, there is a clear button, which quickly erases the entered values, providing a smoother and more efficient user experience.

<br>

![alt text](<Captura de Tela (102).png>)


---

# Python Features

<br>

The "Currency Converter" project is a Python application developed to convert values between different currencies, using an API to obtain real-time exchange rates. The system allows the user to select the source and target currencies, displays the flags of the corresponding countries, and automatically updates the information, including the last update date.

The tool also includes a button to swap the source and target currencies quickly and easily, as well as a button to clear the input fields, ensuring smoother and more efficient navigation.

---

<br>
<br>
<br>
<br><br>

# Python Project Structure

<br>

This format is clean and to the point. Just fill in with the specific information about your project!

1. **`steam.py`** – This is the main file that interacts with the graphical user interface (GUI) using `customtkinter`, obtaining the currency data and exchange rates, and performing the conversion.
2. **`pegar_moedas.py`** – Contains functions to load data related to the currencies and available conversions from XML files.
3. **`pegar_cotacao.py`** – Handles obtaining the currency exchange rates via an external API.

Now, let's explain each part.

---

### **`steam.py`** – GUI and Conversion Logic

#### **1. Initial Settings**

```python
import customtkinter
from pegar_moedas import nomes_moedas, conversoes_disponiveis
from pegar_cotacao import pegar_cotacao_moeda

# Appearance settings
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

# Window settings
janela = customtkinter.CTk()
janela.geometry("500x500")
```

#### **Explanation:**

- **`import customtkinter`**: The `customtkinter` module is a customized version of Tkinter (Python's GUI library). It provides widgets with a modern and customizable look.
- **`from pegar_moedas import nomes_moedas, conversoes_disponiveis`**: This imports functions from the `pegar_moedas.py` file to get the names of the currencies and available conversions.
- **`from pegar_cotacao import pegar_cotacao_moeda`**: This imports the `pegar_cotacao_moeda` function from the `pegar_cotacao.py` file, which is responsible for making the request to the API and obtaining the currency rates.
- **`customtkinter.set_appearance_mode("dark")`**: Sets the interface theme to "dark" mode.
- **`customtkinter.set_default_color_theme("dark-blue")`**: Sets the color theme to "dark-blue", providing a modern dark visual for the interface.
- **`janela = customtkinter.CTk()`**: Creates the main window for the graphical interface.
- **`janela.geometry("500x500")`**: Sets the window size to 500x500 pixels.

---

#### **2. Loading Data**

```python
dic_conversoes_disponiveis = conversoes_disponiveis()  # Calls the function to get the dictionary
moedasDisponiveis = nomes_moedas()  # Calls the function to get the currency names
```

#### **Explanation:**

- **`dic_conversoes_disponiveis = conversoes_disponiveis()`**: Calls the `conversoes_disponiveis()` function that loads the possible currency conversions (from the XML file).
- **`moedasDisponiveis = nomes_moedas()`**: Calls the `nomes_moedas()` function that loads the names of the available currencies (also from the XML file).



---

#### **3. Title and Texts**

```python
titulo = customtkinter.CTkLabel(janela, text="Currency Converter", font=('', 20))

# Texts and selection menus
textoMoedaInicio = customtkinter.CTkLabel(janela, text="Select your source currency")
textoMoedaFinal = customtkinter.CTkLabel(janela, text="Select your target currency")
```

#### **Explanation:**

- **`titulo = customtkinter.CTkLabel(janela, text="Currency Converter", font=('', 20))`**: Creates a label with the text "Currency Converter" that will be displayed at the top of the window.
- **`textoMoedaInicio`** and **`textoMoedaFinal`**: These are labels instructing the user to select the source and target currencies.

---

#### **4. Function `carregar_moeda_destino`**

```python
def carregar_moeda_destino(moeda_selecionada):
    lista_moeda_destino = dic_conversoes_disponiveis[moeda_selecionada]
    selecionadorMoedaFinal.configure(values=lista_moeda_destino)
    selecionadorMoedaFinal.set(lista_moeda_destino[0])
```

#### **Explanation:**

- The function **`carregar_moeda_destino`** is called whenever the user selects a source currency.
- **`dic_conversoes_disponiveis[moeda_selecionada]`**: Retrieves the list of possible target currencies for the selected source currency.
- **`selecionadorMoedaFinal.configure(values=lista_moeda_destino)`**: Updates the target currency selection menu with the corresponding options.
- **`selecionadorMoedaFinal.set(lista_moeda_destino[0])`**: Sets the default target currency (the first item in the list).

---

#### **5. Conversion Function**

```python
def conversor():
    moeda_origem = campo_moeda_origem.get()
    moeda_destino = campo_moeda_destino.get()
    if moeda_origem and moeda_destino:
        cotacao = pegar_cotacao_moeda(moeda_origem, moeda_destino)
        texto_cotacao_moeda.configure(text=f"1 {moeda_origem} ={cotacao} {moeda_destino}")
```

#### **Explanation:**

- **`campo_moeda_origem.get()`**: Retrieves the selected source currency from the menu.
- **`campo_moeda_destino.get()`**: Retrieves the selected target currency.
- If both currencies are selected, the function calls **`pegar_cotacao_moeda(moeda_origem, moeda_destino)`** to fetch the current exchange rate between the selected currencies.
- **`texto_cotacao_moeda.configure(text=f"1 {moeda_origem} ={cotacao} {moeda_destino}")`**: Displays the exchange rate result in the graphical interface, showing the exchange rate between the two currencies.

---

#### **6. Conversion Button**

```python
botaoConversor = customtkinter.CTkButton(janela, text='Convert', command=conversor)
```

#### **Explanation:**

- Creates a button in the interface with the text "Convert".
- When the button is clicked, the **`conversor`** function is called to perform the currency conversion.

---

#### **7. Frame and Currency List**

```python
listaMoedas = customtkinter.CTkScrollableFrame(janela)
texto_cotacao_moeda = customtkinter.CTkLabel(janela, text="")
```

#### **Explanation:**

- **`listaMoedas = customtkinter.CTkScrollableFrame(janela)`**: Creates a scrollable frame to list the available currencies. This is useful when there are many currencies to display.
- **`texto_cotacao_moeda`**: Creates a label to display the conversion rate.

---

### **`pegar_moedas.py`** – Loading Currencies and Conversions

#### **1. Function `nomes_moedas`**

```python
def nomes_moedas():
    with open('coins.xml', 'rb') as arquivos_moedas:
        dic_moedas = xmltodict.parse(arquivos_moedas)
        moedas = dic_moedas['xml']
        return moedas
```

#### **Explanation:**

- The function **`nomes_moedas`** opens the `coins.xml` file and parses it using the `xmltodict` library.
- **`dic_moedas = xmltodict.parse(arquivos_moedas)`**: Converts the XML file into a Python dictionary.
- **`moedas = dic_moedas['xml']`**: Extracts the list of currencies from the parsed dictionary.
- **`return moedas`**: Returns the list of currencies to be used in the application.

---

Here is the translated text in English:

---

#### **Explanation:**

- **`with open('coins.xml', 'rb') as arquivos_moedas:`**: Opens the XML file containing the currency names.
- **`xmltodict.parse(arquivos_moedas)`**: Uses the `xmltodict` module to parse the XML file into a Python dictionary.
- **`dic_moedas['xml']`**: Accesses the list of currencies within the dictionary returned by `xmltodict`.
- **`return moedas`**: Returns the currency names.

---

#### **2. Function `conversoes_disponiveis`**

```python
def conversoes_disponiveis():
    with open('conversoes.xml', 'rb') as arquivos_conversoes:
        dic_conversoes = xmltodict.parse(arquivos_conversoes)
        dic_conversoes_disponiveis = {}

        for par_conversao in conversoes:
            moedas_origem, moedas_destino = par_conversao.split("-")

            if par_conversao in dic_conversoes_disponiveis:
                dic_conversoes_disponiveis[moedas_origem].append(moedas_destino)
            else:
                dic_conversoes_disponiveis[moedas_origem] = [moedas_destino]

        return dic_conversoes_disponiveis
```

#### **Explanation:**

- Loads the `conversoes.xml` file containing the possible currency conversions.
- For each conversion, the function organizes a dictionary of source and target currencies.

---

### **`pegar_cotacao.py` – Fetching Currency Exchange Rates**

#### **1. Function `pegar_cotacao_moeda`**

```python
def pegar_cotacao_moeda(moeda_origem, moeda_destino):
    url = f"https://api.exchangerate-api.com/v4/latest/{moeda_origem}"
    response = requests.get(url)
    dados = response.json()
    cotacao = dados['rates'][moeda_destino]
    return cotacao
```

#### **Explanation:**

- **`url = f"https://api.exchangerate-api.com/v4/latest/{moeda_origem}"`**: Constructs the URL to fetch exchange rates using the external API.
- **`response = requests.get(url)`**: Makes an HTTP request to fetch data from the API.
- **`dados = response.json()`**: Converts the API response from JSON format to a Python dictionary.
- **`cotacao = dados['rates'][moeda_destino]`**: Retrieves the exchange rate between the two currencies from the API's returned data.

---

### **JavaScript Project Structure**

#### **1. `DOMContentLoaded` Event Listener**

```javascript
document.addEventListener('DOMContentLoaded', () => {
    const moedaOrigemSelect = document.getElementById('moedaOrigem');
    const moedaDestinoSelect = document.getElementById('moedaDestino');
    const valorInput = document.getElementById('valor');
    const resultadoDiv = document.getElementById('resultado');
    const converterButton = document.getElementById('converter');
```

#### **Explanation:**

- **`document.addEventListener('DOMContentLoaded', () => {...})`**: This code adds an event listener that waits until the page content (DOM) is fully loaded before executing the function. This ensures that JavaScript does not execute before the page elements are available.
  
- **`const moedaOrigemSelect = document.getElementById('moedaOrigem');`**: Here, we select the `<select>` element with the ID `"moedaOrigem"`, which is the dropdown menu for selecting the source currency.
  
- **`const moedaDestinoSelect = document.getElementById('moedaDestino');`**: Similar to the previous one, selects the `<select>` element with the ID `"moedaDestino"`, which is the menu for selecting the target currency.

- **`const valorInput = document.getElementById('valor');`**: Selects the input field where the user enters the value to be converted.

- **`const resultadoDiv = document.getElementById('resultado');`**: Selects the `<div>` where the conversion result will be displayed.

- **`const converterButton = document.getElementById('converter');`**: Selects the conversion button for when the user clicks it.

---

### **2. Function `carregarMoedas`**

```javascript
const carregarMoedas = async () => {
    const response = await fetch('https://api.exchangerate-api.com/v4/latest/USD');
    const data = await response.json();
    const moedas = Object.keys(data.rates);
```

#### **Explanation:**

- **`const carregarMoedas = async () => {...}`**: Defines an asynchronous function called `carregarMoedas`, which will fetch exchange rate data from the API.

- **`const response = await fetch('https://api.exchangerate-api.com/v4/latest/USD');`**: The `fetch` function is used to make an HTTP request to the exchange rate API (Exchangerate API). The `await` keyword waits for the API response before continuing the code. The `USD` in the URL indicates that we are fetching exchange rates relative to the dollar (base currency).

- **`const data = await response.json();`**: After receiving the API response, we use the `.json()` method to convert the response into JSON format, allowing us to access the API data in a structured way.

- **`const moedas = Object.keys(data.rates);`**: Here, we extract the keys of the `rates` object, which contains the exchange rates of various currencies relative to USD. The `Object.keys()` function returns an array with the currency names (e.g., EUR, BRL, JPY, etc.).

---
### **3. Filling Dropdown Menus with Currencies**

```javascript
currencies.forEach(currency => {
    const option = document.createElement('option');
    option.value = currency;
    option.textContent = currency;
    originCurrencySelect.appendChild(option);
    destinationCurrencySelect.appendChild(option.cloneNode(true));
});
```

#### **Explanation:**

- **`currencies.forEach(currency => {...})`**: The `forEach` method iterates through each item in the `currencies` array (the currencies provided by the API response).

- **`const option = document.createElement('option');`**: For each currency, we dynamically create an `<option>` element to be added to the dropdown menus.

- **`option.value = currency;`**: Sets the value of the option to the currency name (e.g., "USD", "BRL"), which will be the value submitted when the user selects a currency.

- **`option.textContent = currency;`**: Sets the text displayed in the dropdown menu as the currency name.

- **`originCurrencySelect.appendChild(option);`**: Adds the option to the origin currency dropdown (`originCurrencySelect`).

- **`destinationCurrencySelect.appendChild(option.cloneNode(true));`**: Clones the same option and adds it to the destination currency dropdown (`destinationCurrencySelect`). This ensures that both dropdown menus have the same currency options.

Let’s continue explaining the JavaScript code!

---

### **4. `convert` Function**

```javascript
const convert = async () => {
    const originCurrency = originCurrencySelect.value;
    const destinationCurrency = destinationCurrencySelect.value;
    const amount = parseFloat(amountInput.value);

    if (isNaN(amount) || amount <= 0) {
        resultDiv.textContent = "Please enter a valid amount.";
        return;
    }

    const response = await fetch(`https://api.exchangerate-api.com/v4/latest/${originCurrency}`);
    const data = await response.json();
    const exchangeRate = data.rates[destinationCurrency];
    const result = amount * exchangeRate;

    resultDiv.textContent = `${amount} ${originCurrency} equals ${result.toFixed(2)} ${destinationCurrency}`;
};
```

#### **Explanation:**

- **`const convert = async () => {...}`**: Defines an asynchronous function named `convert`, which handles the currency conversion based on user input.

- **`const originCurrency = originCurrencySelect.value;`**: Retrieves the selected origin currency from the dropdown menu. This value will be the currency code, such as "USD" or "BRL."

- **`const destinationCurrency = destinationCurrencySelect.value;`**: Similarly, retrieves the selected destination currency from the dropdown menu.

- **`const amount = parseFloat(amountInput.value);`**: Gets the amount entered by the user in the input field and converts it to a decimal number (float) using `parseFloat`. This ensures that the amount is correctly processed in calculations.

- **`if (isNaN(amount) || amount <= 0) {...}`**: This conditional block checks if the user-entered value is not a valid number (using `isNaN`) or is less than or equal to 0. If so, it displays an error message prompting the user to enter a valid amount and stops execution.

- **`const response = await fetch(...)`**: Makes a request to the API to fetch exchange rates for the selected origin currency. The API URL is dynamically generated based on the origin currency.

- **`const data = await response.json();`**: Converts the API response from JSON format to allow easy manipulation of the returned data.

- **`const exchangeRate = data.rates[destinationCurrency];`**: Retrieves the exchange rate for the destination currency from the `rates` object returned by the API. This object contains the exchange rates for all currencies relative to the base currency (in this case, the origin currency).

- **`const result = amount * exchangeRate;`**: Performs the conversion by multiplying the user-entered amount by the exchange rate obtained from the API.

- **`resultDiv.textContent = ...`**: Displays the conversion result in the `div` element on the page. The `toFixed(2)` function rounds the result to two decimal places.

---

### **5. Attaching an Event to the Convert Button**

```javascript
convertButton.addEventListener('click', convert);
```

#### **Explanation:**

- **`convertButton.addEventListener('click', convert);`**: Links the `convert` function to the `click` event of the convert button (`convertButton`). This means the function is executed every time the user clicks the button.

---

### **6. Calling `loadCurrencies` on Page Load**

```javascript
loadCurrencies();
```

#### **Explanation:**

- **`loadCurrencies();`**: Finally, the `loadCurrencies` function is called when the page loads to populate the dropdown menus with available currencies. This ensures users have currency options ready when the page opens.

---

### Code Flow:

1. The script starts by waiting for the DOM to load fully.
2. When the page loads, the `loadCurrencies` function is called to populate the dropdown menus with available currencies.
3. The user selects origin and destination currencies, enters an amount, and clicks the convert button, triggering the `convert` function.
4. The `convert` function validates the input, fetches exchange rates from the API, performs the conversion, and displays the result.

This code structure is modular, ensuring that responsibilities (such as loading currencies and performing conversions) are well-separated, making the code easy to read and maintain.

---

## Technologies Used

- **Python**: The primary programming language used to develop the project.
- **CustomTKinter**: A web framework used to create the interface and interactivity for the Python application.
- **APIs (Currency API & Country Flags API)**: External APIs to fetch real-time exchange rates and country flags.
- **HTML/CSS**: Technologies used to structure and style the user interface, ensuring a visually appealing and responsive design.
- **JavaScript**: Used to add interactivity, such as updating dropdown menus and clearing fields.

--- 

# 👨‍💻 Developer

| [<img loading="lazy" src="https://avatars.githubusercontent.com/u/140810343?v=4" width=95><br><sub>Samuel (Sal) Lima do Amaral</sub>](https://github.com/salgadoles)
| :--: |
