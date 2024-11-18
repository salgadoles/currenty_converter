<p 
align="center">
  <img src="https://umbrasil.org.br/wp-content/uploads/2015/11/2000px-Marys_monogram_Marist_Brothers.svg_.png" alt="Descrição da imagem" width="100" height="100 margin-top = >



</p>
<h1 style="text-align: center;">Projeto Conversor De Moedas</h1>


---
<br>
<br>

# Sobre o Projeto

<br>
<br>

Aqui está o texto melhorado:

---

Este projeto foi uma atividade proposta pelo docente [Leonardo Rocha](https://github.com/LeonardoRochaMarista) na disciplina de Programação Web 1, no [Colégio Marista Ir. Acácio](https://github.com/MaristaIrAcacio). A proposta apresentada em sala de aula consistia na criação de um conversor de moedas, que consultaria uma API de câmbio para obter os valores atualizados das moedas. Durante o desenvolvimento, optei por criar duas versões do conversor, utilizando duas linguagens diferentes: uma em Python e outra em JavaScript. Abaixo, você pode conferir as funcionalidades de cada versão, seguido pela explicação técnica detalhada de como o projeto foi implementado.

---
<br>
<br>
<br>

# Funcionalidades JavaScript

O Conversor de Moedas é uma ferramenta simples e prática que permite a conversão entre diversas moedas de forma rápida e precisa. Ele exibe as bandeiras dos países correspondentes e atualiza as taxas de câmbio em tempo real, garantindo informações sempre atualizadas, incluindo a última data de atualização.

O sistema conta com um botão para inverter os campos de entrada, facilitando o processo de conversão. Além disso, há um botão de limpar, que apaga rapidamente os valores digitados, proporcionando uma experiência de usuário mais fluida e eficiente.

<br>

![alt text](<Captura de Tela (102).png>)

---
<br>
<br>
<br>


# Funcionalidades Python

<br>

O projeto "Currency Converter" é uma aplicação Python desenvolvida para converter valores entre diferentes moedas, utilizando uma API para obter as taxas de câmbio em tempo real. O sistema permite ao usuário selecionar as moedas de origem e destino, exibe as bandeiras dos países correspondentes e atualiza as informações automaticamente, incluindo a última data de atualização.

A ferramenta também inclui um botão para inverter as moedas de origem e destino de forma prática e rápida, além de um botão para limpar os campos de entrada, garantindo uma navegação mais fluida e eficiente.



---

<br>
<br>
<br>
<br><br>

# Estrutura do Projeto Python

<br>

Esse formato é bem enxuto e direto ao ponto. Basta preencher com as informações específicas do seu projeto!

1. **`steam.py`** – É o arquivo principal que interage com a interface gráfica (GUI) usando o `customtkinter`, obtendo as informações de moedas e taxas de câmbio e realizando a conversão.
2. **`pegar_moedas.py`** – Contém funções para carregar dados relacionados às moedas e às conversões possíveis a partir de arquivos XML.
3. **`pegar_cotacao.py`** – Lida com a obtenção das cotações das moedas via uma API externa.

Agora, vamos explicar parte por parte.

---

### **`steam.py`** – Interface gráfica e lógica de conversão

#### **1. Configurações Iniciais**

```python
import customtkinter
from pegar_moedas import nomes_moedas, conversoes_disponiveis
from pegar_cotacao import pegar_cotacao_moeda

# Configurações da aparência
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

# Configurações da janela
janela = customtkinter.CTk()
janela.geometry("500x500")
```

#### **Explicação:**

- **`import customtkinter`**: O módulo `customtkinter` é uma versão customizada do Tkinter (biblioteca de GUI do Python). Ele fornece widgets com um visual moderno e personalizável.
- **`from pegar_moedas import nomes_moedas, conversoes_disponiveis`**: Está importando funções do arquivo `pegar_moedas.py` para obter os nomes das moedas e as conversões disponíveis.
- **`from pegar_cotacao import pegar_cotacao_moeda`**: Importa a função `pegar_cotacao_moeda` do arquivo `pegar_cotacao.py`, que é responsável por fazer a requisição à API e obter a cotação de moedas.
- **`customtkinter.set_appearance_mode("dark")`**: Define o tema da interface como "dark" (modo escuro).
- **`customtkinter.set_default_color_theme("dark-blue")`**: Define o tema de cor como "dark-blue", proporcionando um visual moderno e escuro para a interface.
- **`janela = customtkinter.CTk()`**: Cria a janela principal da interface gráfica.
- **`janela.geometry("500x500")`**: Define o tamanho da janela como 500x500 pixels.

---

#### **2. Carregando Dados**

```python
dic_conversoes_disponiveis = conversoes_disponiveis()  # Chama a função para obter o dicionário
moedasDisponiveis = nomes_moedas()  # Chama a função para obter as moedas
```

#### **Explicação:**

- **`dic_conversoes_disponiveis = conversoes_disponiveis()`**: Chama a função `conversoes_disponiveis()` que carrega as conversões possíveis entre as moedas (do arquivo XML).
- **`moedasDisponiveis = nomes_moedas()`**: Chama a função `nomes_moedas()` que carrega os nomes das moedas (também do arquivo XML).

---

#### **3. Título e Textos**

```python
titulo = customtkinter.CTkLabel(janela, text="Conversor de Moedas", font=('', 20))

# Textos e menus de seleção
textoMoedaInicio = customtkinter.CTkLabel(janela, text="Selecione sua moeda de origem")
textoMoedaFinal = customtkinter.CTkLabel(janela, text="Selecione sua moeda de destino")
```

#### **Explicação:**

- **`titulo = customtkinter.CTkLabel(janela, text="Conversor de Moedas", font=('', 20))`**: Cria um rótulo (label) com o texto "Conversor de Moedas" que será exibido na parte superior da janela.
- **`textoMoedaInicio`** e **`textoMoedaFinal`**: São rótulos (labels) que instruem o usuário a selecionar as moedas de origem e destino.

---

#### **4. Função `carregar_moeda_destino`**

```python
def carregar_moeda_destino(moeda_selecionada):
    lista_moeda_destino = dic_conversoes_disponiveis[moeda_selecionada]
    selecionadorMoedaFinal.configure(values=lista_moeda_destino)
    selecionadorMoedaFinal.set(lista_moeda_destino[0])
```

#### **Explicação:**

- A função **`carregar_moeda_destino`** é chamada sempre que o usuário seleciona uma moeda de origem.
- **`dic_conversoes_disponiveis[moeda_selecionada]`**: Obtém a lista de moedas de destino possíveis para a moeda de origem selecionada.
- **`selecionadorMoedaFinal.configure(values=lista_moeda_destino)`**: Atualiza o menu de seleção de moeda de destino com as opções correspondentes.
- **`selecionadorMoedaFinal.set(lista_moeda_destino[0])`**: Define a moeda de destino padrão (o primeiro item da lista).

---

#### **5. Função de Conversão**

```python
def conversor():
    moeda_origem = campo_moeda_origem.get()
    moeda_destino = campo_moeda_destino.get()
    if moeda_origem and moeda_destino:
        cotacao = pegar_cotacao_moeda(moeda_origem, moeda_destino)
        texto_cotacao_moeda.configure(text=f"1 {moeda_origem} ={cotacao} {moeda_destino}")
```

#### **Explicação:**

- **`campo_moeda_origem.get()`**: Obtém a moeda de origem selecionada no menu.
- **`campo_moeda_destino.get()`**: Obtém a moeda de destino selecionada.
- Se ambas as moedas forem selecionadas, a função chama **`pegar_cotacao_moeda(moeda_origem, moeda_destino)`** para buscar a cotação atual entre as moedas selecionadas.
- **`texto_cotacao_moeda.configure(text=f"1 {moeda_origem} ={cotacao} {moeda_destino}")`**: Exibe o resultado da cotação na interface gráfica, mostrando a taxa de câmbio entre as duas moedas.

---

#### **6. Botão de Conversão**

```python
botaoConversor = customtkinter.CTkButton(janela, text='Converter', command=conversor)
```

#### **Explicação:**

- Cria um botão na interface com o texto "Converter".
- Quando o botão é clicado, a função **`conversor`** é chamada para realizar a conversão entre as moedas.

---

#### **7. Frame e Lista de Moedas**

```python
listaMoedas = customtkinter.CTkScrollableFrame(janela)
texto_cotacao_moeda = customtkinter.CTkLabel(janela, text="")
```

#### **Explicação:**

- **`listaMoedas = customtkinter.CTkScrollableFrame(janela)`**: Cria um frame rolável para listar as moedas disponíveis. Isso é útil caso haja muitas moedas para exibir.
- **`texto_cotacao_moeda`**: Cria um label para exibir a cotação da conversão.

---

### **`pegar_moedas.py`** – Carregando as Moedas e Conversões

#### **1. Função `nomes_moedas`**

```python
def nomes_moedas():
    with open('coins.xml', 'rb') as arquivos_moedas:
        dic_moedas = xmltodict.parse(arquivos_moedas)
        moedas = dic_moedas['xml']
        return moedas
```

#### **Explicação:**

- **`with open('coins.xml', 'rb') as arquivos_moedas:`**: Abre o arquivo XML contendo os nomes das moedas.
- **`xmltodict.parse(arquivos_moedas)`**: Usa o módulo `xmltodict` para parsear o arquivo XML em um dicionário Python.
- **`dic_moedas['xml']`**: Acessa a lista de moedas dentro do dicionário retornado pelo `xmltodict`.
- **`return moedas`**: Retorna os nomes das moedas.

---

#### **2. Função `conversoes_disponiveis`**

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
``

`

#### **Explicação:**

- Carrega o arquivo `conversoes.xml` que contém as conversões possíveis entre as moedas.
- Para cada conversão, a função organiza um dicionário de moedas de origem e destino.

---

### **`pegar_cotacao.py`** – Obtendo a Cotação das Moedas

#### **1. Função `pegar_cotacao_moeda`**

```python
def pegar_cotacao_moeda(moeda_origem, moeda_destino):
    url = f"https://api.exchangerate-api.com/v4/latest/{moeda_origem}"
    response = requests.get(url)
    dados = response.json()
    cotacao = dados['rates'][moeda_destino]
    return cotacao
```
<br>
<br>
<br>
<br><br>

# Estrutura do Projeto JavaScript

#### **Explicação:**

- **`url = f"https://api.exchangerate-api.com/v4/latest/{moeda_origem}"`**: Constroi a URL para consultar a cotação usando a API externa.
- **`response = requests.get(url)`**: Faz a requisição HTTP para obter os dados da API.
- **`dados = response.json()`**: Converte a resposta da API de JSON para um dicionário Python.
- **`cotacao = dados['rates'][moeda_destino]`**: Obtém a taxa de câmbio entre as duas moedas a partir dos dados retornados pela API.






### **1. Ouvinte de evento `DOMContentLoaded`**

```javascript
document.addEventListener('DOMContentLoaded', () => {
    const moedaOrigemSelect = document.getElementById('moedaOrigem');
    const moedaDestinoSelect = document.getElementById('moedaDestino');
    const valorInput = document.getElementById('valor');
    const resultadoDiv = document.getElementById('resultado');
    const converterButton = document.getElementById('converter');
```

#### **Explicação:**

- **`document.addEventListener('DOMContentLoaded', () => {...})`**: Este código adiciona um ouvinte de evento que espera até que o conteúdo da página (DOM) seja totalmente carregado antes de executar o que está dentro da função. Isso garante que o JavaScript não execute antes que os elementos da página estejam disponíveis.
  
- **`const moedaOrigemSelect = document.getElementById('moedaOrigem');`**: Aqui, selecionamos o elemento `<select>` com o id `"moedaOrigem"`, que é o menu suspenso para selecionar a moeda de origem.
  
- **`const moedaDestinoSelect = document.getElementById('moedaDestino');`**: Similar ao anterior, selecionamos o elemento `<select>` com o id `"moedaDestino"`, que é o menu para selecionar a moeda de destino.

- **`const valorInput = document.getElementById('valor');`**: Seleciona o campo de entrada onde o usuário vai inserir o valor que deseja converter.

- **`const resultadoDiv = document.getElementById('resultado');`**: Seleciona o `<div>` onde o resultado da conversão será exibido.

- **`const converterButton = document.getElementById('converter');`**: Seleciona o botão de conversão para quando o usuário clicar nele.

---

### **2. Função `carregarMoedas`**

```javascript
const carregarMoedas = async () => {
    const response = await fetch('https://api.exchangerate-api.com/v4/latest/USD');
    const data = await response.json();
    const moedas = Object.keys(data.rates);
```

#### **Explicação:**

- **`const carregarMoedas = async () => {...}`**: Define uma função assíncrona chamada `carregarMoedas`, que vai ser responsável por buscar as taxas de câmbio de moedas da API.

- **`const response = await fetch('https://api.exchangerate-api.com/v4/latest/USD');`**: A função `fetch` é usada para fazer uma solicitação HTTP para a API de taxas de câmbio (Exchangerate API). O `await` espera que a resposta da API chegue antes de continuar o código. O `USD` após a URL indica que estamos buscando as taxas de câmbio em relação ao dólar (moeda base).

- **`const data = await response.json();`**: Após obter a resposta da API, usamos o método `.json()` para converter a resposta em formato JSON, o que permite acessar os dados da API de forma estruturada.

- **`const moedas = Object.keys(data.rates);`**: Aqui, estamos extraindo as chaves do objeto `rates` que contém as taxas de câmbio das moedas em relação ao USD. O `Object.keys()` retorna um array com os nomes das moedas (ex: EUR, BRL, JPY, etc.).

---

### **3. Preenchendo os menus suspensos com as moedas**

```javascript
moedas.forEach(moeda => {
    const option = document.createElement('option');
    option.value = moeda;
    option.textContent = moeda;
    moedaOrigemSelect.appendChild(option);
    moedaDestinoSelect.appendChild(option.cloneNode(true));
});
```

#### **Explicação:**

- **`moedas.forEach(moeda => {...})`**: O `forEach` percorre cada item do array `moedas` (as moedas disponíveis na resposta da API).

- **`const option = document.createElement('option');`**: Para cada moeda, criamos dinamicamente um elemento `<option>`, que vai ser adicionado aos menus suspensos.

- **`option.value = moeda;`**: Define o valor da opção como o nome da moeda (por exemplo, "USD", "BRL", etc.), que será o valor que será enviado quando o usuário escolher a moeda.

- **`option.textContent = moeda;`**: Define o texto exibido para o usuário no menu suspenso como o nome da moeda.

- **`moedaOrigemSelect.appendChild(option);`**: Adiciona a opção ao menu de moeda de origem (`moedaOrigemSelect`).

- **`moedaDestinoSelect.appendChild(option.cloneNode(true));`**: Clona a mesma opção e a adiciona ao menu de moeda de destino (`moedaDestinoSelect`). Isso é feito porque as opções de moedas para ambos os menus devem ser as mesmas.

Vamos continuar com a explicação do código JavaScript!

### **4. Função `converter`**

```javascript
const converter = async () => {
    const moedaOrigem = moedaOrigemSelect.value;
    const moedaDestino = moedaDestinoSelect.value;
    const valor = parseFloat(valorInput.value);

    if (isNaN(valor) || valor <= 0) {
        resultadoDiv.textContent = "Por favor, insira um valor válido.";
        return;
    }

    const response = await fetch(`https://api.exchangerate-api.com/v4/latest/${moedaOrigem}`);
    const data = await response.json();
    const taxaCambio = data.rates[moedaDestino];
    const resultado = valor * taxaCambio;

    resultadoDiv.textContent = `${valor} ${moedaOrigem} equivale a ${resultado.toFixed(2)} ${moedaDestino}`;
};
```

#### **Explicação:**

- **`const converter = async () => {...}`**: Aqui, estamos definindo uma função assíncrona chamada `converter`, que será responsável por realizar a conversão de uma moeda para outra com base no valor inserido pelo usuário.

- **`const moedaOrigem = moedaOrigemSelect.value;`**: Obtém o valor da moeda de origem selecionada no menu suspenso. Esse valor será o código da moeda, como "USD", "BRL", etc.

- **`const moedaDestino = moedaDestinoSelect.value;`**: Da mesma forma, obtém o valor da moeda de destino selecionada pelo usuário no menu suspenso.

- **`const valor = parseFloat(valorInput.value);`**: Pega o valor inserido pelo usuário no campo de input, e o converte para um número decimal (float) usando `parseFloat`. Isso é necessário para garantir que o valor seja tratado corretamente durante os cálculos.

- **`if (isNaN(valor) || valor <= 0) {...}`**: Este bloco condicional verifica se o valor inserido pelo usuário não é um número válido (usando `isNaN`) ou se é menor ou igual a 0. Caso seja, exibe uma mensagem de erro informando o usuário para inserir um valor válido e retorna, interrompendo a execução da função.

- **`const response = await fetch(...)`**: Faz uma requisição à API para obter as taxas de câmbio em relação à moeda de origem selecionada. A URL da API é dinâmica, dependendo da moeda de origem.

- **`const data = await response.json();`**: Converte a resposta da API em formato JSON para manipular os dados que foram retornados.

- **`const taxaCambio = data.rates[moedaDestino];`**: Obtém a taxa de câmbio para a moeda de destino, utilizando o valor de `moedaDestino`. A API retorna um objeto `rates` que contém as taxas de todas as moedas em relação à moeda base (no caso, a moeda de origem). Acessamos a taxa de câmbio específica da moeda de destino.

- **`const resultado = valor * taxaCambio;`**: Realiza a conversão multiplicando o valor inserido pelo usuário pela taxa de câmbio obtida da API.

- **`resultadoDiv.textContent = ...`**: Exibe o resultado da conversão no `div` do HTML. A função `toFixed(2)` é utilizada para arredondar o resultado para duas casas decimais.

---

### **5. Associando o evento ao botão de conversão**

```javascript
converterButton.addEventListener('click', converter);
```

#### **Explicação:**

- **`converterButton.addEventListener('click', converter);`**: Aqui, estamos associando a função `converter` ao evento de clique do botão de conversão (`converterButton`). Ou seja, sempre que o usuário clicar no botão, a função `converter` será chamada para processar a conversão.

---

### **6. Chamando a função `carregarMoedas` no carregamento da página**

```javascript
carregarMoedas();
```

#### **Explicação:**

- **`carregarMoedas();`**: Por fim, chamamos a função `carregarMoedas` quando a página é carregada para preencher os menus suspensos com as moedas disponíveis. Isso garante que o usuário tenha as opções de moeda carregadas automaticamente quando a página for aberta.

---

### Fluxo do Código:

1. O script começa aguardando o carregamento completo do DOM.
2. Quando a página é carregada, a função `carregarMoedas` é chamada para preencher as opções de moeda disponíveis nos menus suspensos.
3. Quando o usuário escolhe a moeda de origem e destino, insere um valor e clica no botão de conversão, a função `converter` é acionada.
4. A função `converter` valida o valor, faz uma requisição à API para obter as taxas de câmbio, realiza a conversão e exibe o resultado.

Essa organização de código é bem modular, garantindo que as responsabilidades (como carregar moedas e converter valores) estejam bem separadas, o que facilita a manutenção e a leitura do código.

<br>
<br>
<br>

---

<br>

## Tecnologias usadas:



- **Python**: A linguagem de programação principal utilizada para o desenvolvimento do projeto.
- **CustomTKinter**: Framework web utilizado para criar a interface e interatividade do aplicativos python.
- **APIs (Currency API & Country Flags API)**: APIs externas para obter taxas de câmbio em tempo real e as bandeiras dos países.
- **HTML/CSS**: Tecnologias utilizadas para estruturar e estilizar a interface do usuário, garantindo uma experiência visual agradável e responsiva.
- **JavaScript**: Usado para adicionar interatividade, como a troca de campos de moeda e a funcionalidade de limpar os campos.

<br>
<br>

--- 

# 👨‍💻 Programador

| [<img loading="lazy" src="https://avatars.githubusercontent.com/u/140810343?v=4" width=95><br><sub>Samuel (Sal) Lima do Amaral</sub>](https://github.com/salgadoles)
| :--: |

