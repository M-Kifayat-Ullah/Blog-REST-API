# Blog REST API

A REST API built with Python and Django REST Framework featuring complete CRUD operations and Token Authentication.

## Features
- Complete CRUD operations (Create, Read, Update, Delete)
- Token Authentication (Login API)
- Protected endpoints — only authenticated users can access
- Browsable API interface

## Technologies Used
- Python 3.13
- Django 5.2
- Django REST Framework
- SQLite Database

## API Endpoints

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| GET | /api/posts/ | Get all posts | Yes |
| POST | /api/posts/ | Create new post | Yes |
| GET | /api/posts/1/ | Get single post | Yes |
| PUT | /api/posts/1/ | Update post | Yes |
| DELETE | /api/posts/1/ | Delete post | Yes |
| POST | /api/login/ | Login & get token | No |

## Setup & Installation

1. Clone the repository
   git clone https://github.com/M-Kifayat-Ullah/Blog-REST-API.git

2. Navigate to project folder
   cd Blog-REST-API

3. Install dependencies
   pip install django djangorestframework

4. Run migrations
   python manage.py migrate

5. Create admin user
   python manage.py createsuperuser

6. Start server
   python manage.py runserver

7. Open browser
   http://127.0.0.1:8000/api/posts/

## How to Use API

### Step 1 — Login and get token
POST /api/login/
{
    "username": "your_username",
    "password": "your_password"
}

### Step 2 — Use token in every request
Headers:
Authorization: Token your_token_here

## Screenshots
<img width="959" height="506" alt="image" src="https://github.com/user-attachments/assets/23d3fbac-7314-4a36-83e3-a201d8c6f7f4" />
<img width="956" height="506" alt="image" src="https://github.com/user-attachments/assets/b994c44c-62f6-42bc-8ab0-fe70db73a8d6" />
<img width="671" height="467" alt="image" src="https://github.com/user-attachments/assets/1e87fb07-ba78-4a70-99bc-de24454854b2" />
<img width="674" height="471" alt="image" src="https://github.com/user-attachments/assets/494c29ee-5a2b-43b0-83eb-619234397b8e" />





## Author
Kifayat Ullah Younis
- GitHub: github.com/M-Kifayat-Ullah
- LinkedIn: linkedin.com/in/kifayat-ullah-younis-9a305425b
