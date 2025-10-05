# 📰 News Blog

A full-featured **Django-based News Blog** web application that allows users to **create, read, update, and delete news posts**.  
Built with **Django**, **HTML**, **CSS**, and **JavaScript**, this project demonstrates backend logic, template rendering, and frontend interactivity.

---

## 🚀 Features

✅ User authentication (login, register, logout)  
✅ Create, edit, and delete blog posts  
✅ Display all posts with details pages  
✅ Responsive and interactive frontend using CSS & JavaScript  
✅ Admin dashboard for managing articles  
✅ Dynamic URLs and Django templates  

---

## 🧱 Tech Stack

- **Backend:** Django (Python)  
- **Frontend:** HTML, CSS, JavaScript  
- **Database:** SQLite (default)  
- **Version Control:** Git & GitHub  

---

## 🗂️ Project Structure

News-blog/
├── blog/ # Main Django app (models, views, urls)
├── templates/ # HTML templates for pages
├── static/ # CSS, JS, images
├── news_blog/ # Project settings and configurations
├── manage.py # Django management script
├── requirements.txt # Python dependencies
└── README.md

yaml
Copy code

---

## ⚙️ Installation & Setup

Follow these steps to set up the project locally 👇

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/adelana107/News-blog.git
cd News-blog
2️⃣ Create a Virtual Environment
bash
Copy code
python -m venv env
Activate it:

Windows: env\Scripts\activate

Mac/Linux: source env/bin/activate

3️⃣ Install Dependencies
bash
Copy code
pip install -r requirements.txt
4️⃣ Run Database Migrations
bash
Copy code
python manage.py makemigrations
python manage.py migrate
5️⃣ Create Superuser (optional)
bash
Copy code
python manage.py createsuperuser
6️⃣ Start the Server
bash
Copy code
python manage.py runserver
Then visit:

cpp
Copy code
http://127.0.0.1:8000/
🧩 How It Works
Users can view all news articles on the homepage.

Logged-in users can create, edit, or delete posts.

Each article has a dedicated detail page.

The admin panel (/admin) allows full content management.

🎨 Frontend Design
HTML Templates: Used Django Template Language for dynamic rendering

CSS: For styling and responsiveness

JavaScript: For interactivity and DOM manipulation

Static Files: Served using Django’s staticfiles system

🧪 Testing
Run tests using:

bash
Copy code
python manage.py test
You can also manually test pages through the browser at http://127.0.0.1:8000/.

🌍 Deployment (Optional)
When deploying to production:

Set DEBUG = False in settings.py

Configure ALLOWED_HOSTS

Collect static files:

bash
Copy code
python manage.py collectstatic
Use a production server like Gunicorn with Nginx

Host on platforms like Render, Railway, or PythonAnywhere

🤝 Contributing
Contributions are welcome!

Fork this repo

Create a new branch:

bash
Copy code
git checkout -b feature-name
Commit changes:

bash
Copy code
git commit -m "Add new feature"
Push branch:

bash
Copy code
git push origin feature-name
Open a Pull Request

🧑‍💻 Author
Adelana Oluwafunmibi
GitHub: adelana107
