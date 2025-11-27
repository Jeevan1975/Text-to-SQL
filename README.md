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
  - [Customer Features](#%EF%B8%8F-customer-features)
  - [Admin Features](#%E2%80%8D-adminrestaurant-features)
  - [Real-Time System (WebSockets)](#-real-time-system-websockets)
- [Tech Stack](#-tech-stack)
- [Architecture](#-architecture)
- [Project Structure](#-project-structure)
- [Installation Guide](#%EF%B8%8F-installation-guide)
- [Environment Variables](#-environment-variables)
- [Setting Up Redis (WSL--Windows--Linux)](#-setting-up-redis-wsl--windows--linux)
- [Setting Up Supabase](#-setting-up-supabase)
- [Security & Privacy](#-security--privacy)
- [Future Enhancements](#-future-enhancements)
- [License](#license)

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
- Website: [https://text-to-sql.com](https://text-to-sql-9f81.onrender.com)


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
   git clone https://github.com/Jeevan1975/Text-to-SQL.git
   cd QR-Dine
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
4. **Apply Migrations**
   ```bash
   python manage.py migrate
   ```
5. **Create Superuser**
   ```bash
   python manage.py createsuperuser
   ```
6. **Run Development Server**
   ```bash
   python manage.py runserver
   ```

## 🌱 Environment Variables
Create a `.env` file in the project root (values shown are examples):
```
ENVIRONMENT=development
SECRET_KEY=<your-django-secret-key>
DEBUG=True

SUPABASE_URL=<your-supabase-url>
SUPABASE_KEY=<your-supabase-key>

DATABASE_URL=<postgresql-url>
DATABASE_PASSWORD=<password>

REDIS_URL=redis://127.0.0.1:637
SITE_BASE_URL=http://127.0.0.1:8000
```

## 🐘 Setting Up Redis (WSL / Windows / Linux)
### 💻 Ubuntu / Linux
```bash
sudo apt update
sudo apt install redis-server
sudo systemctl enable redis
sudo systemctl start redis
```

### 🪟 Windows (Recommended: WSL)
1. Enable WSL.
2. Install Ubuntu from Microsoft Store.
3. Inside Ubuntu:
   ```bash
   sudo apt update
   sudo apt install redis-server
   sudo service redis-server start
   ```
4. Test Redis:
   ```bash
   redis-cli ping
   ```

> Windows native Redis is no longer officially supported; WSL is recommended.

## 🌐 Setting Up Supabase
1. Create a Supabase project at https://app.supabase.com.
2. Create a **Storage Bucket** named `qr-images` and `menu-images`(public).
3. Add keys to `.env`:
   ```
   SUPABASE_URL=...
   SUPABASE_KEY=...
   ```
4. The system automatically generates QR PNGs, saves them to Supabase, returns the public URL, and stores it on each table model record.

## 🔐 Security & Privacy
- Table URLs use UUID-based tokens; QR codes encode `SITE_BASE_URL` + tokenized menu link.
- Order updates use order-specific WebSocket channels.
- Sensitive keys live in `.env`; keep `SECRET_KEY`, database, Supabase, and Redis credentials private.
- Cart data is session-only; QR codes do not contain personal data.
- Production settings enable HTTPS cookies and proxy headers when `ENVIRONMENT` is not `development`.

## 📈 Future Enhancements
- Online payment integration (Razorpay / Stripe).
- Invoice PDF generator.
- Kitchen Display System (KDS).
- Push notifications for “Order Ready”.
- Multi-restaurant SaaS support.
- Customer login + loyalty points.
- Analytics dashboard for sales & trends.

## License
This project is NOT open source. All rights reserved.
