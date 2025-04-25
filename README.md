# 🤖 IA Assistant with FastAPI

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

> Scroll down for [Spanish](#-español) or [Portuguese](#-português) versions.

### 🤖 AI Assistant with FastAPI

This is a modular project built using **FastAPI**, designed to offer an AI-powered assistant accessible via a web interface or terminal CLI.

### 🚀 Features

- Web chat with FastAPI + Jinja2.
- Terminal (CLI) assistant mode.
- Support for OpenAI, Azure, Ollama, GitHub-hosted models.
- Modular architecture.
- Local document search via Lunr.js.

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
│   │   ├── loader.py
│   │   ├── logger.py
│   │   ├── query_rewrite.py
│   │   └── search.py
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
| `make clean`   | Removes all `__pycache__` folders.     |
| `make help`    | Displays available Makefile commands.  |

---

## 🇪🇸 Español

### 🤖 Asistente IA con FastAPI

Este proyecto modular está construido con **FastAPI** y proporciona un asistente de IA accesible desde una interfaz web o mediante terminal.

### 🚀 Características

- Chat web con FastAPI + Jinja2.
- Modo asistente desde terminal (CLI).
- Compatible con modelos OpenAI, Azure, Ollama y GitHub.
- Arquitectura modular.
- Búsqueda local de documentos con Lunr.js.

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
│   │   ├── loader.py
│   │   ├── logger.py
│   │   ├── query_rewrite.py
│   │   └── search.py
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
| `make clean`   | Elimina carpetas `__pycache__`.                    |
| `make help`    | Muestra los comandos disponibles del Makefile.     |

---

## 🇵🇹 Português

### 🤖 Assistente IA com FastAPI

Este é um projeto modular desenvolvido com **FastAPI**, oferecendo um assistente de IA acessível via web ou terminal (CLI).

### 🚀 Funcionalidades

- Chat web com FastAPI + Jinja2.
- Modo terminal (CLI).
- Compatível com modelos OpenAI, Azure, Ollama e GitHub.
- Arquitetura limpa e modular.
- Busca local de documentos com Lunr.js.

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
│   │   ├── loader.py
│   │   ├── logger.py
│   │   ├── query_rewrite.py
│   │   └── search.py
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
| `make clean`   | Remove pastas `__pycache__`.                             |
| `make help`    | Mostra os comandos disponíveis.                          |
