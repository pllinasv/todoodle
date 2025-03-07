# ToDoodle

ToDoodle is a simple and efficient to-do list application designed to help users manage their tasks seamlessly. Built with modern web technologies, it features a React (Next.js) frontend and a FastAPI backend, with PostgreSQL as the database.

Currently working in it.

## Features

- Create, update, and delete tasks
- Mark tasks as completed
- Categorize tasks
- User authentication (optional)
- Responsive UI with Next.js
- FastAPI backend for quick API responses
- PostgreSQL database for reliable data storage

## Tech Stack

### Frontend
- [Next.js](https://nextjs.org/) (React Framework)
- Tailwind CSS (for styling)
- Axios (for API requests)

### Backend
- [FastAPI](https://fastapi.tiangolo.com/) (Python framework for APIs)
- PostgreSQL (database)
- SQLAlchemy (ORM for database interactions)

## Installation

### Prerequisites
Ensure you have the following installed on your system:
- Node.js & npm
- Python (3.8+)
- PostgreSQL database

### Clone the Repository
```sh
git clone https://github.com/yourusername/todoodle.git
cd todoodle
```

### Backend Setup
```sh
cd backend
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
uvicorn main:app --reload
```

### Frontend Setup
```sh
cd frontend
npm install
npm run dev
```

The frontend should now be running at `http://localhost:3000`, and the backend API at `http://localhost:8000`.

## API Endpoints

### Default
| Method | Endpoint  | Description |
|--------|----------|-------------|
| GET    | /        | Redirects to API docs |

### User
| Method | Endpoint    | Description |
|--------|------------|-------------|
| GET    | /user/     | Fetch all users |
| GET    | /user/{id} | Fetch a specific user by ID |
| POST   | /user/     | Create a new user |
| PUT    | /user/{id} | Update a user |
| DELETE | /user/     | Delete all users |
| DELETE | /user/{id} | Delete a user by ID |

### Task
| Method | Endpoint    | Description |
|--------|------------|-------------|
| GET    | /task/     | Fetch all tasks |
| GET    | /task/{id} | Fetch a specific task by ID |
| POST   | /task/     | Create a new task |
| PUT    | /task/{id} | Update a task |
| DELETE | /task/     | Delete all tasks |
| DELETE | /task/{id} | Delete a task by ID |

### Task-User
| Method | Endpoint           | Description |
|--------|-------------------|-------------|
| GET    | /task-user/{user_id} | Fetch all tasks of a user |
| DELETE | /task-user/{user_id} | Delete all tasks of a user |

## Contributing
Feel free to submit issues and pull requests! Contributions are welcome.

## License
This project is licensed under the MIT License.

## Author
[Pol Llinas](https://github.com/pllinasv)

