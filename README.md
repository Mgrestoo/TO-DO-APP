# ✓ TaskFlow - Modern TODO Application

A clean, modern task management application built with Django. Manage your tasks efficiently with user authentication, profiles, and real-time task completion tracking.

---

## 📋 Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Features Overview](#features-overview)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)

---

## ✨ Features

### Core Features
- **User Authentication**
  - Secure registration with password strength validation
  - Login/logout functionality
  - User-specific task isolation

- **Task Management**
  - Create, read, update, delete tasks
  - Mark tasks as complete/incomplete
  - Task descriptions (optional)
  - Timestamps for creation

- **User Profiles**
  - Profile picture upload with image validation
  - Bio/about section
  - Profile edit functionality

- **Form Validation**
  - Strong password requirements (8+ chars, letters, numbers, special chars)
  - Username uniqueness validation (case-insensitive)
  - Email validation
  - Real-time error feedback

- **Security**
  - CSRF protection on all forms
  - Password hashing using Django's built-in system
  - User-scoped data (can't access other users' tasks)
  - Login required decorators

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| **Backend** | Django 4.2+ |
| **Database** | SQLite (dev) / PostgreSQL (production-ready) |
| **Frontend** | Bootstrap 5, HTML5, CSS3 |
| **Authentication** | Django Auth |
| **File Storage** | Django ImageField |
| **Server** | Django development server (runserver) |

---

## 📁 Project Structure

```
todo_app/
├── config/                          # Project configuration
│   ├── settings.py                  # Django settings
│   ├── urls.py                      # Main URL routing
│   └── wsgi.py
│
├── tasks/                           # Main app
│   ├── models.py                    # Database models
│   │   ├── User (built-in)
│   │   ├── Task
│   │   └── UserProfile
│   ├── views.py                     # View logic
│   ├── forms.py                     # Form definitions
│   ├── validators.py                # Custom validators
│   ├── urls.py                      # App URL routing
│   ├── admin.py                     # Admin configuration
│   ├── templates/
│   │   ├── base.html                # Base template (navbar, footer)
│   │   └── tasks/
│   │       ├── register.html        # Registration page
│   │       ├── login.html           # Login page
│   │       ├── task_list.html       # Main tasks page
│   │       ├── task_form.html       # Create/edit task
│   │       ├── profile.html         # User profile page
│   │       └── create_post.html     # (Blog app)
│   └── migrations/                  # Database migrations
│
├── blog/                            # Blog app (bonus)
│   ├── models.py
│   ├── views.py
│   └── templates/
│
├── media/                           # User uploads (images)
│   └── profiles/
│
├── db.sqlite3                       # Database
├── manage.py                        # Django CLI
├── requirements.txt                 # Dependencies
└── README.md                        # This file
```

---

## 🚀 Installation

### Prerequisites
- Python 3.8+
- pip (Python package manager)
- Git

### Step 1: Clone Repository

```bash
git clone https://github.com/yourusername/todo-app.git
cd todo-app
```

### Step 2: Create Virtual Environment

```bash
# macOS/Linux
python -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
pip install django pillow
```

(Or create requirements.txt and run: `pip install -r requirements.txt`)

### Step 4: Apply Migrations

```bash
python manage.py migrate
```

### Step 5: Create Superuser (Optional, for admin)

```bash
python manage.py createsuperuser
# Follow prompts to create admin user
```

### Step 6: Run Server

```bash
python manage.py runserver
```

Visit: `http://localhost:8000/`

---

## 💻 Usage

### User Registration
1. Click **Register** on homepage
2. Enter username, email, password
3. Password must have:
   - 8+ characters
   - At least one letter
   - At least one number
   - At least one special character (!@#$%^&*, etc.)
4. Click **Create Account**

### Login
1. Enter username and password
2. Click **Login**
3. Redirected to task dashboard

### Create Task
1. Click **+ New Task** in navbar
2. Enter title (required, 4+ chars)
3. Enter description (optional)
4. Click **Create Task**

### Manage Tasks
- **Mark Complete**: Click "✓ Mark Complete" button
- **Mark Incomplete**: Click "↺ Mark Incomplete" button
- **Edit Task**: Click "✎ Edit" button
- **Delete Task**: Click "🗑 Delete" button (with confirmation)

### Profile Management
1. Click profile picture/name in navbar
2. Add bio (up to 500 chars)
3. Upload profile image (JPG, PNG, etc.)
4. Click **Save Profile**

---

**Last Updated:** March 2026
**Status:** Active Development 🚀