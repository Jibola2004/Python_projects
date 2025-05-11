# 📝 ToDo List API with Auth

A simple and secure ToDo List API built using **FastAPI**, supporting **user registration**, **login**, and **task management** with token-based authentication.

---

## 🚀 Features

- ✅ User registration (`/register`)
- 🔐 User login with JWT token (`/login`)
- 🛡️ Token-protected routes (with OAuth2)
- 🧾 Create, view, update, and delete tasks
- 🧪 Interactive API docs via Swagger (`/docs`)

---

## 📦 Tech Stack

- **FastAPI** – for building fast, asynchronous APIs
- **Python-JOSE** – for JWT token generation and verification
- **Passlib (bcrypt)** – for password hashing
- **OAuth2PasswordBearer** – for token-based authentication

---

## 📚 API Endpoints

### 👤 Auth

- `POST /register` – Register a new user
- `POST /login` – Login and get access token

### ✅ Tasks (Protected)

- `GET /tasks` – Get all tasks
- `POST /tasks` – Add a new task
- `PUT /tasks/{task_id}` – Toggle task completion
- `DELETE /tasks/{task_id}` – Delete a task

---

## 🧪 Testing the API

After running the server, visit:

- Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
- Redoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

You can test endpoints directly from the Swagger UI after logging in and providing the Bearer token.


