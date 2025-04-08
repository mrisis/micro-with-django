# Django Microservices Project

This project is a microservices architecture written in Django. It contains two main services:
- **Authentication Service:** Handles user authentication and authorization.
- **Social Networking Service:** Provides social networking features such as posts, comments, and user interactions.

---

## Features
### Authentication Service
- User registration and login.
- JWT-based authentication.
- Token verification and refresh.

### Social Networking Service
- Create, update, and delete posts.
- Commenting on posts.
- Following/unfollowing users.

---

## Technologies Used
- **Backend Framework:** Django
- **Database:** PostgreSQL
- **Caching:** Redis
- **Containerization:** Docker
- **API Development:** Django REST Framework (DRF)

---

## Installation

### Prerequisites
- Python 3.9 or higher
- Docker and Docker Compose
- PostgreSQL
- Redis

### Clone the Repository
```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo

# Project Setup Guide

## Prerequisites
- Python 3.9 or higher
- Docker and Docker Compose installed on your system

---

## Clone the Repository
```bash
git clone https://github.com/mrisis/micro-with-django
cd micro-with-django
```

---

## Create Virtual Environment
To set up the project locally, create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate
```

Then install the required dependencies:
```bash
pip install -r requirements.txt
```

---

## Create `.env` File
In the root directory of the project, create a `.env` file and define the environment variables as follows:

```plaintext
# .env file
DB_NAME= data base name
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=postgres
DB_PORT=5432
SECRET_KEY=secret key
DEBUG=True
```

Replace the placeholder values (e.g., `your-secret-key`) with your actual configuration.

---

## Run the Project Using Docker
To run the project with Docker Compose:

1. Build the Docker images:
    ```bash
    docker-compose up --build
    ```


## Useful Commands
Stop the containers:
```bash
docker-compose down
```

Rebuild the containers if needed:
```bash
docker-compose up --build
```

View logs for all services:
```bash
docker-compose logs -f
```

---

## Directory Structure
Here’s a brief overview of the project’s directory structure:

```plaintext
your-repo/
├── auth_service/       # Authentication microservice
├── social_service/     # Social networking microservice
├── docker-compose.yml  # Docker Compose configuration
├── requirements.txt    # Python dependencies
├── .env                # Environment variables
└── README.md           # Project documentation
```

---

## Troubleshooting
If you encounter any issues:

1. Ensure Docker and Docker Compose are properly installed.
2. Verify that the `.env` file contains the correct values.
3. Check the logs for specific errors:
    ```bash
    docker-compose logs
    ```

4. create super user:
```bash
   docker-compose exec api_service python manage.py createsuperuser

```

# API Endpoints Guide

## Authentication Service 

### Login
**URL:** `localhost:8000/api/auth/login/`  
  

**Request Example:**
```json
{
  "username": "user123",
  "password": "password123"
}
```

### Register


### Register
**URL:** `localhost:8000/api/auth/register/`  
  

**Request Example:**
```json
{
  "username": "user123",
  "password": "password123",
   "email": "user123@gmail.com"
}
```







## Social Networking Service 

### Get Posts
**URL:** `api/social/posts/`  
**Method:** `GET`  
**Description:** Retrieve a list of all posts.  


### Create Post
**URL:** `api/social/posts/create/`  
**Method:** `POST`  
**Description:** Create a new post.  

