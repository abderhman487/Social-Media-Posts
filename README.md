# Posts API

## Overview

Posts API is a FastAPI application for post management, providing a RESTful API for creating, reading, updating, and deleting posts. The application also includes user authentication, post voting, and securing endpoints using JWT.

## Features

- **User Management**: Register users and securely store their data
- **Authentication**: Secure login system using JWT
- **Post Management**: Create, edit, delete, and view posts
- **Voting System**: Allow users to vote on posts
- **Enhanced Querying**: Search, filtering, and pagination
- **Database Migrations**: Using Alembic for schema changes and version control
- **CORS Support**: Cross-Origin Resource Sharing for frontend integration

## Technologies Used

- **FastAPI**: Fast framework for building APIs
- **PostgreSQL**: Relational database for data storage
- **SQLAlchemy**: ORM for database interaction
- **Pydantic**: For data validation and conversion
- **JWT**: For authentication and session management
- **Bcrypt**: For password encryption
- **Alembic**: For database migrations and schema versioning
- **CORS Middleware**: For handling cross-origin requests

## Project Structure

```
app/
├── __init__.py
├── main.py
├── config.py
├── database.py
├── models.py
├── oauth2.py
├── schemas.py
├── utils.py
└── routers/
    ├── post.py
    ├── user.py
    ├── auth.py
    └── vote.py
alembic/
├── versions/
│   └── 7dde9c99ac58_add_all_tables_to_apply_data_migration.py
├── env.py
└── script.py.mako
```

## Requirements

- Python 3.8+
- PostgreSQL
- `.env` file with required environment variables

## Setup

1. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # on Linux/Mac
   venv\Scripts\activate  # on Windows
   ```

2. Install requirements:
   ```
   pip install -r requirements.txt
   ```

3. Create a `.env` file with the following variables:
   ```
   DATABASE_HOSTNAME=localhost
   DATABASE_PORT=5432
   DATABASE_USERNAME=postgres
   DATABASE_NAME=posts
   DATABASE_PASSWORD=password
   SECRET_KEY=your_secret_key
   ALGORITHM=HS256
   ACCESS_TOKEN_EXPIRE_MINUTES=30
   ```

4. Set up the database using Alembic:
   ```
   alembic upgrade head
   ```

5. Run the application:
   ```
   uvicorn app.main:app --reload
   ```

## Database Migrations

This project uses Alembic for database migrations. Here are the common commands:

1. Create a new migration:
   ```
   alembic revision --autogenerate -m "description of changes"
   ```

2. Apply migrations:
   ```
   alembic upgrade head
   ```

3. Rollback to a previous version:
   ```
   alembic downgrade -1
   ```

4. Check current version:
   ```
   alembic current
   ```

5. View migration history:
   ```
   alembic history
   ```

## API Endpoints

### Users

- `POST /users/`: Create a new user
- `GET /users/{id}`: Get user information

### Authentication

- `POST /login`: Login and get JWT

### Posts

- `GET /posts/`: Get all posts (with vote counts)
- `GET /posts/{id}`: Get a specific post (with vote count)
- `POST /posts/`: Create a new post
- `PUT /posts/{id}`: Update a post
- `DELETE /posts/{id}`: Delete a post

### Voting

- `POST /vote/`: Vote on a post (add or remove)

## API Usage

### Create User
```http
POST /users/
Content-Type: application/json

{
    "email": "user@example.com",
    "password": "AnyPasswordYouWant"
}
```

### Login
```http
POST /login
Content-Type: application/x-www-form-urlencoded

username=user@example.com&password=password123
```

### Create Post
```http
POST /posts/
Content-Type: application/json
Authorization: Bearer {token}

{
    "title": "Post Title",
    "content": "Post Content",
    "published": true
}
```

### Vote on Post
```http
POST /vote/
Content-Type: application/json
Authorization: Bearer {token}

{
    "post_id": 1,
    "dir": 1
}
```

### CORS Configuration
The API is configured with CORS middleware to allow cross-origin requests:
```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

## Security

- Password encryption using Bcrypt
- Authentication using JWT
- User validation before operations
- Post ownership verification before editing or deletion
- CORS configuration for secure cross-origin requests

## Future Development

### Database Improvements
- Implement SQL Joins for better data retrieval
- Set up Joins in SQLAlchemy for related data
- Optimize "Get One" endpoint with Joins

### Cloud Deployment
- Deploy to Heroku
- Create Heroku app and configure
- Set up Heroku Procfile
- Add Postgres database on Heroku
- Configure environment variables in Heroku
- Run Alembic migrations on Heroku Postgres
- Automate code deployment to production

### Version Control & CI/CD
- Set up Git for version control
- Create GitHub repository
- Implement CI/CD with GitHub Actions
- Set up GitHub Secrets for secure variables
- Create Jobs for automated testing and deployment
- Configure testing database for CI/CD
- Build Docker images in CI pipeline
- Automate deployment to Heroku
- Handle failing tests in pipeline

### Self-Hosted Deployment
- Set up Ubuntu VM for deployment
- Update packages and security
- Install Python and PostgreSQL
- Configure Postgres security
- Create dedicated user and Python environment
- Configure environment variables
- Deploy with Gunicorn
- Create Systemd service for auto-start
- Set up Nginx as reverse proxy
- Configure domain name
- Implement SSL/HTTPS with certificates
- Enable Nginx configuration
- Configure firewall rules
- Automate code deployment to server

### Containerization
- Create Dockerfile for application
- Set up Docker Compose for multi-container deployment
- Configure Postgres container
- Implement bind mounts for data persistence
- Push containers to DockerHub
- Configure production vs development environments

### Testing
- Implement comprehensive test suite with Pytest
- Write basic test functions
- Use -s & -v flags for detailed output
- Test multiple functions with parametrize
- Create test classes for organization
- Implement fixtures for test setup
- Combine fixtures with parametrize
- Test exception handling
- Use FastAPI TestClient for endpoint testing
- Configure test flags for different scenarios
- Test user creation workflow
- Set up dedicated testing database
- Create and destroy database after each test
- Create fixtures for database interaction
- Handle trailing slashes in path tests
- Configure fixture scope for efficiency
- Create user fixture for authentication tests
- Test and validate token generation/validation
- Organize tests with conftest.py

## Author

Abderhman Gamal