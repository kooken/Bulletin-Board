# Bulletin Board API

A RESTful API for a bulletin board application where users can post ads and leave comments. Built with Django REST Framework.

## Features

- JWT-based authentication (register, login, token refresh)
- Post, edit, and delete ads with image uploads
- Leave comments on ads
- Filter ads by title
- Paginated ad listings (4 per page)
- Role-based access control (user / admin)
- Swagger and ReDoc API documentation
- Dockerized setup with PostgreSQL

## Tech Stack

- **Python 3** / **Django 5**
- **Django REST Framework**
- **Djoser** — user registration and authentication endpoints
- **Simple JWT** — JWT token management
- **PostgreSQL** — database
- **drf-nested-routers** — nested routes for comments under ads
- **django-filter** — ad search/filtering
- **drf-yasg** — Swagger / ReDoc docs
- **Docker** / **docker-compose**

## API Endpoints

| Method | Endpoint | Description | Auth required |
|--------|----------|-------------|---------------|
| POST | `/api/users/users/` | Register a new user | No |
| POST | `/api/users/token/` | Obtain JWT token pair | No |
| POST | `/api/users/token/refresh/` | Refresh access token | No |
| GET | `/api/board/ads/` | List all ads (paginated, filterable) | No |
| POST | `/api/board/ads/` | Create an ad | Yes |
| GET | `/api/board/ads/{id}/` | Retrieve an ad | No |
| PATCH | `/api/board/ads/{id}/` | Update an ad | Owner or Admin |
| DELETE | `/api/board/ads/{id}/` | Delete an ad | Owner or Admin |
| GET | `/api/board/ads/me/` | List current user's ads | Yes |
| GET | `/api/board/ads/{id}/comments/` | List comments on an ad | Yes |
| POST | `/api/board/ads/{id}/comments/` | Add a comment | Yes |
| PATCH | `/api/board/ads/{id}/comments/{id}/` | Update a comment | Owner or Admin |
| DELETE | `/api/board/ads/{id}/comments/{id}/` | Delete a comment | Owner or Admin |

Interactive docs available at:
- Swagger UI: `http://localhost:8000/swagger/`
- ReDoc: `http://localhost:8000/redoc/`

## Getting Started

### Prerequisites

- [Docker Desktop](https://www.docker.com/products/docker-desktop/)

### Setup

1. Clone the repository:
   ```bash
   git clone <repo-url>
   cd Bulletin-Board
   ```

2. Create a `.env` file in the project root (see [.env.example](.env.example)):
   ```env
   DJANGO_SECRET_KEY=your-secret-key

   POSTGRES_DB=bulletin_board
   POSTGRES_USER=postgres
   POSTGRES_PASSWORD=postgres
   POSTGRES_HOST=db
   POSTGRES_PORT=5432

   EMAIL_HOST=smtp.example.com
   EMAIL_PORT=465
   EMAIL_HOST_USER=your@email.com
   EMAIL_HOST_PASSWORD=your-password
   ```

3. Build and start the containers:
   ```bash
   docker-compose up --build
   ```

4. The API will be available at `http://localhost:8000`.

### Create a superuser

After the containers are running:
```bash
docker-compose exec app python manage.py csu
```

This creates an admin account with email `admin@ads.com` and password `admin`.

### Running without Docker

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Set up the database and run migrations:
   ```bash
   python manage.py migrate
   ```

3. Start the development server:
   ```bash
   python manage.py runserver
   ```

## Project Structure

```
Bulletin-Board/
├── board/              # Ads and comments app
│   ├── models.py       # Ad, Comment models
│   ├── views.py        # AdViewSet, CommentViewSet
│   ├── serializers.py  # Ad and Comment serializers
│   ├── permissions.py  # IsAdmin, IsOwner permissions
│   ├── filters.py      # Title filter for ads
│   ├── paginators.py   # Page-size pagination
│   └── urls.py         # Nested router config
├── users/              # Custom user app
│   ├── models.py       # User model with role support
│   ├── managers.py     # UserManager
│   ├── serializers.py  # Registration serializer
│   └── urls.py         # Auth and token endpoints
├── config/             # Django project config
│   ├── settings.py
│   └── urls.py
├── docker-compose.yml
├── Dockerfile
└── requirements.txt
```

## User Roles

| Role | Permissions |
|------|-------------|
| `user` | Create ads and comments; edit/delete own content |
| `admin` | Edit/delete any ad or comment |
