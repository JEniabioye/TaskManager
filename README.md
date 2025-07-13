# Django Task Manager
A simple web-based task manager built with Django. It allows users to register, log in, and manage their
personal task lists (CRUD operations).

## Features
- User registration and login/logout
- Create, update, and delete tasks
- Task list is private to each user
- Bootstrap-styled HTML for basic UI
- Django authentication system
- SQLite database (can be upgraded to PostgreSQL)
  
## Screenshots
(Optional: Add screenshots here if available)

## Technologies Used
- Python 3.x
- Django 4.x
- HTML/CSS (Bootstrap 5)
- SQLite (default)
- Git & GitHub
  
## Setup Instructions
### 1. Clone the repository
git clone https://github.com/JEniabioye/taskmanager.git
cd taskmanager
### 2. Create a virtual environment
python -m venv myenv
myenv\Scripts\activate # For Windows
### 3. Install dependencies
pip install -r requirements.txt
(Create a requirements.txt using pip freeze > requirements.txt if you haven't already.)
### 4. Run the server
python manage.py migrate
python manage.py createsuperuser # optional
python manage.py runserver
Visit http://127.0.0.1:8000 in your browser.
## Authentication
- Only logged-in users can manage tasks.
- Each user sees only their own tasks.
## Future Improvements
- PostgreSQL support
- Mobile responsive design
- Task categories/labels
- Task deadlines & reminders
- Deployment to Render or Railway
## License
This project is open-source and available under the MIT License.
