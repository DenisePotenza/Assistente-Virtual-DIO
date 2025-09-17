🗣️ Assistente Virtual com Python

Este projeto implementa um sistema de assistência virtual do zero, utilizando Processamento de Linguagem Natural (PLN) com Python.
O assistente é capaz de ouvir comandos de voz, responder com voz sintetizada e executar ações automatizadas como abrir páginas da web ou buscar informações no Wikipedia.

🚀 Funcionalidades

* 🎤 **Reconhecimento de fala (Speech-to-Text)**: converte a fala do usuário em texto.
* 🔊 **Síntese de fala (Text-to-Speech)**: responde em áudio utilizando voz sintetizada.
* 🌐 **Ações automatizadas via comando de voz**:
   * Pesquisar no Wikipedia e ler o resumo.
   * Abrir o YouTube no navegador.
   * Localizar a farmácia mais próxima no Google Maps.
* 🛑 Encerramento do assistente por comando de voz ("sair" ou "encerrar").

🛠️ Tecnologias utilizadas

* **Python 3.x**
* **SpeechRecognition** - reconhecimento de voz.
* **PyAudio** - captura de áudio do microfone.
* **pyttsx3** - conversão de texto em fala.
* **Wikipedia** - consultas na enciclopédia.
* **Webbrowser** - abrir links no navegador.

📦 Instalação

Clone este repositório:

```
bash

git clone https://github.com/DenisePotenza/Assistente-Virtual-DIO.git
cd Assistente-Virtual-DIO
```



Crie um ambiente virtual (opcional, mas recomendado):

```
bash

python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```



Instale as dependências:

```
bash

pip install -r requirements.txt
```



Se o pyaudio falhar no Linux, instale antes:

```
bash

sudo apt-get install portaudio19-dev python3-pyaudio
```



▶️ Como usar

Execute o programa no terminal:

```
bash

python assistente.py
```



Depois diga comandos como:

* **"abrir youtube"**
* **"pesquisar no wikipedia"**
* **"farmácia mais próxima"**
* **"sair"**

📄 Exemplo de execução

```
bash

🎤 Ouvindo...
Você disse: pesquisar no wikipedia
🔊 Assistente: O que você deseja pesquisar no Wikipedia?
🎤 Ouvindo...
Você disse: inteligência artificial
🔊 Assistente: Inteligência artificial é a área da ciência da computação...
```


📌 Melhorias futuras

* Adicionar integração com APIs (Google, Spotify, etc).
* Criar interface gráfica (GUI) para o assistente.
* Permitir configuração de atalhos personalizados.

👩‍💻 Autor(a)

Projeto desenvolvido por Denise Potenza.
