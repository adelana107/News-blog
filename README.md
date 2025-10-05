# 📰 News Blog (Django Project)

A fully functional news/blog web application built with **Django**.  
This project allows users to read categorized news articles, comment, like/dislike posts, manage profiles, and more.  
It also includes admin features for content management and supports user authentication.

---

## 🚀 Features

### 🧑‍💻 User Features
- Register, login, and logout securely  
- Update personal profiles with images  
- View total likes, dislikes, views, and posts  
- Comment and reply to posts  
- Like or dislike articles (AJAX-powered, no page reload)  
- Search posts by title or category  
- View categorized news pages:
  - Featured News  
  - Main News  
  - Latest News  
  - Trending News  
  - Breaking News  
  - Popular News  

### 🛠️ Admin/Poster Features
- Create, update, and delete posts  
- Assign posts to multiple categories  
- Automatically track post view counts  
- Manage comments and replies  
- Restrict post creation to users in the **“Poster”** group  

### ⚙️ Backend Highlights
- Django ORM for data management  
- Custom models: `Post`, `Category`, `Comment`, `Profile`, `Like`, `Dislike`, `UserLoginSession`  
- AJAX endpoints for like/dislike actions  
- Authentication and authorization with Django’s built-in `User` model  
- Template rendering and view-based routing  

---

## 🧱 Project Structure

News-blog/
├── blog/
│ ├── migrations/
│ ├── templates/
│ │ ├── home.html
│ │ ├── article.html
│ │ ├── profile.html
│ │ ├── create_post.html
│ │ ├── update_post.html
│ │ ├── delete_post.html
│ │ ├── search_page.html
│ │ ├── register_page.html
│ │ ├── login_page.html
│ │ ├── featured_news.html
│ │ ├── trending_news.html
│ │ ├── etc...
│ ├── static/
│ ├── forms.py
│ ├── models.py
│ ├── views.py
│ ├── urls.py
│ └── admin.py
├── NewsBlog/
│ ├── settings.py
│ ├── urls.py
│ ├── wsgi.py
│ └── asgi.py
├── db.sqlite3
├── manage.py
└── README.md

yaml


---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/adelana107/News-blog.git
cd News-blog
2️⃣ Create Virtual Environment
bash

python -m venv env
source env/bin/activate       # on Windows: env\Scripts\activate
3️⃣ Install Dependencies
bash

pip install -r requirements.txt
If no requirements.txt exists yet, you can create one:

bash

pip freeze > requirements.txt
4️⃣ Apply Migrations
bash

python manage.py makemigrations
python manage.py migrate
5️⃣ Create Superuser (for admin access)
bash

python manage.py createsuperuser
6️⃣ Run Development Server
bash

python manage.py runserver
Then open your browser and visit 👉 http://127.0.0.1:8000/

🧠 Core Functionality Overview
✅ Home Page (home)
Displays:

Featured, Main, Trending, Breaking, Popular, and Latest news

Advertisements (from a dedicated category)

All categories and post previews

✅ Article Page (article/<id>)
Displays full article content

Tracks view count

Allows comments and replies

Like/dislike with AJAX

✅ Authentication
login_user, logout_user, registerPage views handle all authentication logic

Uses MyUserCreationForm for registration

✅ Post Management
create_Post: For “Poster” group users

update_post: Edit existing posts

delete_post: Delete posts safely

✅ Search Feature
post_search: Search by title or category using Q filters

✅ Profile System
profile_page: Displays user stats (likes, dislikes, views, total posts)

update_profile: Allows editing profile details

🧩 Technologies Used
Component	Technology
Backend	Django (Python)
Database	SQLite (default)
Frontend	HTML, CSS, Django Templates
Auth	Django Auth System
AJAX	For Like/Dislike buttons
Other	Django ORM, Messages Framework

📸 Screenshots (Optional)
You can add screenshots of:

Home Page

Article Page

Create Post Page

Profile Page

Example:

md
Copy code
![Home Page Screenshot](screenshots/home.png)
🧑‍💻 Author
Adelana Oluwafunmibi Cornelius
🌐 GitHub Profile
