the video u submitted does not a sound but this does. i can not cancel to resubmit due to deadline already passed
https://www.loom.com/share/e2fa590919f04055a57dffbc796a4b91

# Social Media API

A robust RESTful API for a social media application built with Django and Django REST Framework. This backend handles user authentication, profiles, posts, and social interactions like following, liking, and commenting.

## Features

- **Authentication**: Secure JWT (JSON Web Token) authentication (Register, Login, Refresh).
- **User Profiles**: Custom user model with profile images, bios, and follower/following counts.
- **Posts**: Create and view posts. Includes a personalized feed of posts from users you follow.
- **Interactions**:
  - **Likes**: Like and unlike posts.
  - **Comments**: Add and delete comments on posts.
  - **Follow System**: Follow and unfollow other users.
- **Media**: Image upload support for profiles (and potentially posts).

## Tech Stack

- **Framework**: Django 6.0
- **API Toolkit**: Django REST Framework (DRF)
- **Authentication**: `djangorestframework-simplejwt`
- **Database**: SQLite (Default, easy to swap for PostgreSQL)
- **Image Processing**: Pillow

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.10 or higher
- Git

### Installation

1.  **Clone the repository**

    Open your terminal or command prompt and run:

    ```bash
    git clone https://github.com/yourusername/social-media-app-api.git
    cd social-media-app-api
    ```

2.  **Create a Virtual Environment**

    It's recommended to use a virtual environment to manage dependencies.

    *Windows:*
    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```

    *macOS/Linux:*
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Apply Database Migrations**

    Set up the database schema:

    ```bash
    python manage.py migrate
    ```

5.  **Create a Superuser (Optional)**

    If you want to access the Django Admin interface:

    ```bash
    python manage.py createsuperuser
    ```

### Running the Application

Start the development server:

```bash
python manage.py runserver
```

The API will be available at `http://127.0.0.1:8000/`.

## Testing the API

### Automated Verification Script
We have included a script to verify the core functionality of the API (Registration, Login, Posting, Liking, Commenting, Following).

Ensure your server is running in one terminal, then open a **new terminal**, activate your virtual environment, and run:

```bash
python verify_api.py
```

This script performs an end-to-end test of the main user flows.

### API Endpoints Overview

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| **Auth** | | |
| `POST` | `/auth/register/` | Register a new user |
| `POST` | `/auth/login/` | Login and get JWT tokens |
| `POST` | `/auth/refresh/` | Refresh access token |
| **Posts** | | |
| `POST` | `/posts/create/` | Create a new post |
| `GET` | `/posts/feed/` | Get personalized feed |
| `GET` | `/posts/post/<id>/` | Get post details |
| **Interactions** | | |
| `POST` | `/posts/like/<id>/` | Like a post |
| `POST` | `/posts/unlike/<id>/` | Unlike a post |
| `POST` | `/posts/comment/<id>/` | Add a comment |
| `POST` | `/interactions/follow/<id>/` | Follow a user |
| `POST` | `/interactions/unfollow/<id>/` | Unfollow a user |

## Project Structure

- `config/`: Project configuration and main URLs.
- `users/`: User model, authentication views, and profiles.
- `posts/`: Post models, serializers, and views.
- `interactions/`: Follow system logic.
- `verify_api.py`: Script for API validation.

## License

This project is open source and available under the [MIT License](LICENSE).
