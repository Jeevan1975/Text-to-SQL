# 🧠 Text-to-SQL Natural Language Querying System

A full-stack Text-to-SQL engine that converts natural-language questions into safe, validated SQL queries and executes them on a live PostgreSQL database.
Built using FastAPI, LangChain, PostgreSQL, SQLAlchemy, OpenAI/Gemini/Groq LLMs, HTML, Tailwind CSS, and Vanilla JavaScript.

Users can type plain-English questions such as “Show the top 10 customers by revenue this month” and the system will:
  1. Convert the NL query → SQL using an LLM
  2. Validate SQL (strict read-only)
  3. Execute safely on the database
  4. Return formatted results in a clean UI

## 📌 Table of Contents
- [Introduction](#-introduction)
- [Live Demo](#-live-demo)
- [Features](#-features)
  - [Core Features](#-core-features)
  - [Developer Features](#%E2%80%8D-developer-features)
- [Tech Stack](#-tech-stack)
- [Architecture](#-architecture)
- [Installation Guide](#%EF%B8%8F-installation-guide)
- [Environment Variables](#-environment-variables)
- [Security & Guardrails](#-security--guardrails)

## 🎯 Introduction
This project allows users to interact with a SQL database without writing SQL.
The system takes a plain English question, understands it using an LLM, translates it into safe SQL, and returns clean structured results.
Engineers, analysts, and non-technical teams can query data just by typing natural language.

This project contains:
- A FastAPI backend with a modular LangChain-based Text-to-SQL engine
- A PostgreSQL database with schema auto-introspection
- A SQL validator preventing harmful commands (UPDATE/DELETE/DROP/etc.)
- A fallback SQL correction chain
- A frontend interface built with HTML, Tailwind, and JavaScript
- A scalable structure fit for enterprise-grade deployment


## 🌐 Live Demo
- Website: [https://text-to-sql.com](https://text-to-sql-nine.vercel.app)


## 🚀 Features
### 🧠 Core Features
- Natural-language to SQL conversion using advanced LLMs
- Real-time SQL validation (read-only enforcement)
- SQL correction fallback (auto-fixes broken queries)
- Database schema introspection with SQLAlchemy
- Smart LIMIT handling & row control
- Clean results table with Tailwind UI
- Schema viewer to understand available tables/columns
- Frontend powered by Fetch API for fast interactions

### 👨‍💻 Developer Features
- Modular LangChain engine (easy to swap models)
- Pluggable LLM wrapper (OpenAI / Gemini / Groq)
- Strict SQL guardrails
- Query pipeline with step-by-step execution
- Ready-to-use API endpoints for NL→SQL
- Unit-test friendly architecture


## 🧱 Tech Stack
| Layer / Function       | Technology Used                          |
| ---------------------- | ---------------------------------------- |
| Backend Framework      | FastAPI                                  |
| LLM & NL Processing    | LangChain, OpenAI/Gemini/Groq            |
| Database               | PostgreSQL + SQLAlchemy                  |
| Frontend UI            | HTML + Tailwind CSS + JavaScript         |
| Real-Time/Async Engine | Uvicorn / ASGI                           |
| Safe SQL Execution     | Custom SQL Validator + SQLAlchemy Engine |


## 🧩 Architecture
User Query → FastAPI Endpoint → LangChain → LLM → SQL Generator →
SQL Validator → Safe SQL Executor → JSON Results → Tailwind UI Renderer

### 🔍 Detailed Flow

- User sends an NL query through UI
- FastAPI receives it via /query/execute
- System loads DB schema dynamically
- LangChain generates SQL using injected schema + custom prompts
- SQL Validator checks for harmful keywords
- SQL Executor runs validated SQL safely (read-only)
- If SQL fails → SQL Fixer tries to correct it
- Results returned to UI and displayed nicely


## 🛠️ Installation Guide
1. **Clone the Repository**
   ```bash
   https://github.com/Jeevan1975/Text-to-SQL.git
   cd backend
   ```
2. **Create Virtual Environment**
   ```bash
   python -m venv env
   source env/bin/activate  # Windows: env\Scripts\activate
   ```
3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```
4. **Set Up Environment Variables**
   ```
   Create a .env inside the backend folder
   ```
5. **Run Development Server**
   ```bash
    uvicorn app.main:app --reload
   ```


## 🌱 Environment Variables
Create a `.env` file inside the backend folder (values shown are examples):
```
SUPABASE_HOST=aws-1-ap-south-1.pooler.supabase.com
SUPABASE_PORT=6543
SUPABASE_PASSWORD=<your-database-password>
SUPABASE_USER=<supabase-user>

GOOGLE_API_KEY=<your-api-key>
```


## 🔐 Security & Guardrails
- Only SELECT queries are allowed
- Forbidden: UPDATE, DELETE, INSERT, DROP, TRUNCATE, ALTER, REPLACE
- All SQL validated before execution
- API keys stored securely in .env

