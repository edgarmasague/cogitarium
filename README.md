# 🤖 Cogitarium

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Build](https://img.shields.io/badge/build-passing-brightgreen.svg)]()
[![Made with FastAPI](https://img.shields.io/badge/Made%20with-FastAPI-009688.svg)](https://fastapi.tiangolo.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 🧑‍💻 Autor / Author

**Edgar Masagué**  
[GitHub](https://github.com/edgarmasague)

---

## 📄 License / Licencia / Licença

- **English**:  
  This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

- **Español**:  
  Este proyecto está bajo la licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.

- **Português**:  
  Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para detalhes.


## 🗺️ Roadmap

[Ver Roadmap completo](ROADMAP.md) |  
[See Full Roadmap](ROADMAP.md) |  
[Ver Roteiro completo](ROADMAP.md)

---

## 🌐 Available Languages / Idiomas Disponibles / Idiomas Disponíveis

- [🇬🇧 English](#-english)
- [🇪🇸 Español](#-español)
- [🇵🇹 Português](#-português)

---

## 🇬🇧 English

**Cogitarium** (from Latin *cogitare*, "to think") is an AI assistant designed to be your second digital brain.  
Built with **FastAPI**, **Jinja2**, and modern technologies, it allows you to store, search, and retrieve information easily, with a special focus on supporting memory for users.

### 🧠 Features

- Interactive web chat (FastAPI + Jinja2).
- Assistant mode via terminal (CLI).
- Compatible with OpenAI, Azure, Ollama, and GitHub models.
- Modular and extensible architecture.
- Local document search powered by Lunr.js.
- Ideal for people with Alzheimer's or anyone wanting to externalize and organize their knowledge.
- *Cogitarium doesn't just store information: it helps you think better.*

### 📂 Project Structure

```
.
├── .gitignore
├── LICENSE
├── Makefile
├── README.md
├── Roadmap.md
├── backend/
│   ├── cache/
│   ├── config/
│   │   ├── __init__.py
│   │   └── config.py
│   ├── core/
│   │   ├── __init__.py
│   │   ├── ai_config.py
│   │   ├── assistant.py
│   │   ├── cache.py
│   │   ├── embedder.py
│   │   ├── embeddings.py
│   │   ├── i18n.py
│   │   ├── init.py
│   │   ├── loader.py
│   │   ├── logger.py
│   │   ├── query_rewrite.py
│   │   ├── search.py
│   │   ├── translator.py
│   │   └── vector_store.py
│   ├── data/
│   ├── logs/
│   ├── routes/
│   │   ├── __init__.py
│   │   └── cache.py
│   │   ├── chat.py
│   │   └── home.py
│   │   └── logs.py
│   ├── templates/
│   │   └── cache.html
│   │   └── home.html
│   │   └── logs.html
│   ├── translations/
│   │   └── en.json
│   │   └── es.json
│   │   └── pt.json
│   ├── cli.py
│   └── main.py
│   └── requirements.txt
├── devcontainer/
    └── devcontainer.json

```

### 🛠️ Makefile Commands

| Command        | Description                            |
| -------------- | -------------------------------------- |
| `make run`     | Launches FastAPI server with reload.   |
| `make cli`     | Starts the assistant in terminal mode. |
| `make install` | Installs all dependencies.             |
| `make format`  | Formats code with Black.               |
| `make lint`    | Runs code linting with Flake8.         |
| `make clean`   | Removes all cache and logs folders.    |
| `make help`    | Displays available Makefile commands.  |

---

## 🇪🇸 Español

**Cogitarium** (del latín *cogitare*, "pensar") es un asistente de IA diseñado como un segundo cerebro digital.  
Construido con **FastAPI**, **Jinja2** y tecnologías modernas, permite almacenar, buscar y recuperar información fácilmente, pensado especialmente para apoyar la memoria de sus usuarios.

### 🧠 Características

- Chat web interactivo (FastAPI + Jinja2).
- Modo asistente desde terminal (CLI).
- Compatible con modelos OpenAI, Azure, Ollama y GitHub.
- Arquitectura modular y extensible.
- Búsqueda local de documentos mediante Lunr.js.
- Ideal para personas con Alzheimer o para quienes desean organizar su conocimiento.
- *Cogitarium no solo guarda información: te ayuda a pensar mejor.*

### 📂 Estructura del Proyecto

```
.
├── .gitignore
├── LICENSE
├── Makefile
├── README.md
├── Roadmap.md
├── backend/
│   ├── cache/
│   ├── config/
│   │   ├── __init__.py
│   │   └── config.py
│   ├── core/
│   │   ├── __init__.py
│   │   ├── ai_config.py
│   │   ├── assistant.py
│   │   ├── cache.py
│   │   ├── embedder.py
│   │   ├── embeddings.py
│   │   ├── i18n.py
│   │   ├── init.py
│   │   ├── loader.py
│   │   ├── logger.py
│   │   ├── query_rewrite.py
│   │   ├── search.py
│   │   ├── translator.py
│   │   └── vector_store.py
│   ├── data/
│   ├── logs/
│   ├── routes/
│   │   ├── __init__.py
│   │   └── cache.py
│   │   ├── chat.py
│   │   └── home.py
│   │   └── logs.py
│   ├── templates/
│   │   └── cache.html
│   │   └── home.html
│   │   └── logs.html
│   ├── translations/
│   │   └── en.json
│   │   └── es.json
│   │   └── pt.json
│   ├── cli.py
│   └── main.py
│   └── requirements.txt
├── devcontainer/
    └── devcontainer.json
```

### 🛠️ Comandos Makefile

| Comando        | Descripción                                        |
| -------------- | -------------------------------------------------- |
| `make run`     | Inicia el servidor FastAPI con recarga automática. |
| `make cli`     | Ejecuta el asistente desde la terminal.            |
| `make install` | Instala todas las dependencias.                    |
| `make format`  | Formatea el código con Black.                      |
| `make lint`    | Aplica revisión de estilo con Flake8.              |
| `make clean`   | Elimina carpetas de cache y logs.                  |
| `make help`    | Muestra los comandos disponibles del Makefile.     |

---

## 🇵🇹 Português


**Cogitarium** (do latim *cogitare*, "pensar") é um assistente de IA projetado como um segundo cérebro digital.  
Desenvolvido com **FastAPI**, **Jinja2** e tecnologias modernas, permite armazenar, buscar e recuperar informações de forma simples, especialmente pensado para apoiar a memória dos usuários.

### 🧠 Características

- Chat web interativo (FastAPI + Jinja2).
- Modo assistente via terminal (CLI).
- Compatível com modelos da OpenAI, Azure, Ollama e GitHub.
- Arquitetura modular e expansível.
- Pesquisa local de documentos com Lunr.js.
- Ideal para pessoas com Alzheimer ou para quem deseja organizar seu conhecimento.
- *Cogitarium não apenas guarda informações: ajuda você a pensar melhor.*

### 📂 Estrutura do Projeto

```
.
├── .gitignore
├── LICENSE
├── Makefile
├── README.md
├── Roadmap.md
├── backend/
│   ├── cache/
│   ├── config/
│   │   ├── __init__.py
│   │   └── config.py
│   ├── core/
│   │   ├── __init__.py
│   │   ├── ai_config.py
│   │   ├── assistant.py
│   │   ├── cache.py
│   │   ├── embedder.py
│   │   ├── embeddings.py
│   │   ├── i18n.py
│   │   ├── init.py
│   │   ├── loader.py
│   │   ├── logger.py
│   │   ├── query_rewrite.py
│   │   ├── search.py
│   │   ├── translator.py
│   │   └── vector_store.py
│   ├── data/
│   ├── logs/
│   ├── routes/
│   │   ├── __init__.py
│   │   └── cache.py
│   │   ├── chat.py
│   │   └── home.py
│   │   └── logs.py
│   ├── templates/
│   │   └── cache.html
│   │   └── home.html
│   │   └── logs.html
│   ├── translations/
│   │   └── en.json
│   │   └── es.json
│   │   └── pt.json
│   ├── cli.py
│   └── main.py
│   └── requirements.txt
├── devcontainer/
    └── devcontainer.json
```

### 🛠️ Comandos Makefile

| Comando        | Descrição                                                |
| -------------- | -------------------------------------------------------- |
| `make run`     | Inicia o servidor FastAPI com recarregamento automático. |
| `make cli`     | Executa o assistente no terminal.                        |
| `make install` | Instala todas as dependências.                           |
| `make format`  | Formata o código usando Black.                           |
| `make lint`    | Verifica estilo do código com Flake8.                    |
| `make clean`   | Remove pastas de cache e logs.                           |
| `make help`    | Mostra os comandos disponíveis.                          |
