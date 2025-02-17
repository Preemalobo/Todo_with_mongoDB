Todo App with FastAPI and MongoDB

This is a simple Todo App built using FastAPI and MongoDB. It provides RESTful APIs to create, read, update, and delete todo items.

📌 Features

CRUD operations for Todos

Uses MongoDB as the database

FastAPI for backend APIs

Pydantic models for data validation

Supports Swagger UI for API testing

🛠️ Installation & Setup

1️⃣ Clone the Repository

git clone https://github.com/Preemalobo/Todo_with_mongoDB.git
cd Todo_with_mongoDB

2️⃣ Create and Activate a Virtual Environment

python -m venv .venv  # Create virtual environment
source .venv/bin/activate  # Mac/Linux
.venv\Scripts\activate  # Windows

3️⃣ Install Dependencies

pip install -r requirements.txt

4️⃣ Set Up Environment Variables

Create a .env file and add your MongoDB URI:

MONGO_URI=mongodb+srv://<username>:<password>@cluster0.mongodb.net/todo_db

5️⃣ Run the FastAPI Server

uvicorn main:app --reload

The API will be available at: http://127.0.0.1:8000

📌 API Endpoints

Method

Endpoint

Description

POST

/todos/

Create a new todo

GET

/todos/

Get all todos

GET

/todos/{id}

Get a todo by ID

PUT

/todos/{id}

Update a todo

DELETE

/todos/{id}

Delete a todo

🛠️ API Documentation

After running the server, access the Swagger UI:

🚀 http://127.0.0.1:8000/docs

📜 http://127.0.0.1:8000/redoc

📌 Project Structure

Todo_with_mongoDB/
│── database/
│   ├── connection.py
│── models/
│   ├── todo_model.py
│── routes/
│   ├── todo_routes.py
│── main.py
│── config.py
│── requirements.txt
│── README.md

📌 Contributing

Feel free to fork this repo and submit PRs. Any contributions are welcome!
