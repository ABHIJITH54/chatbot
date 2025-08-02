# 🧠 IT Support Chatbot using LangChain RAG, Ollama & Django

A fully local, AI-powered IT support chatbot that uses **LangChain's Retrieval-Augmented Generation (RAG)** and **Ollama's `phi3` LLM** to deliver contextual and accurate answers based on a custom `.docx` knowledge base. Built with **Django**, **ChromaDB**, and **Bootstrap**.

---

## 🚀 Features

- ✅ Local LLM inference using **Ollama (`phi3`)**
- ✅ **RAG pipeline** using LangChain + ChromaDB
- ✅ Chat interface built with **Django, HTML, CSS, JS**
- ✅ REST API 
- ✅ .docx knowledge base ingestion & chunking
- ✅ Stores chat sessions & messages in **MySQL**


---

## 📦 Tech Stack

| Layer         | Technology                           |
|---------------|----------------------------------------|
| LLM Backend   | [Ollama](https://ollama.com) (`phi3`) |
| RAG           | LangChain + ChromaDB                  |
| Embeddings    | `nomic-embed-text` via Ollama         |
| Backend       | Django (Function-based views)         |
| Database      | MySQL (Chat messages, sessions, KB)   |
| Frontend      | HTML, CSS, JS, Bootstrap              |
| File Support  | `.docx` documents (IT KB ingestion)   |

---

## 📁 Project Structure

