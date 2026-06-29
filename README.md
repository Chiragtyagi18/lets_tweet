# 🐦 TweetApp

A full-featured Twitter/X-inspired microblogging platform built with Django. Share your thoughts, connect with others, and express yourself in 280 characters or less.

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-6.0-092E20?logo=django&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-7952B3?logo=bootstrap&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)

---

## ✨ Features

- **User Authentication** — Register, login, and logout with secure session management
- **Create Tweets** — Post text (up to 280 characters) with optional image attachments
- **Edit & Delete** — Full CRUD operations — only manage your own tweets
- **Search** — Find tweets by content or username in real time
- **Responsive Design** — Beautiful dark theme UI that works on desktop, tablet, and mobile
- **Image Uploads** — Attach images to your tweets with drag-and-drop file support
- **User Profiles** — Auto-generated avatars with username initials
- **Admin Panel** — Manage all tweets and users via Django admin

---

## 🛠 Tech Stack

| Layer | Technology |
|-------|-----------|
| **Backend** | Django 6.0.6 |
| **Frontend** | HTML5, CSS3, Bootstrap 5.3 |
| **Icons** | Bootstrap Icons 1.11.3 |
| **Database** | SQLite3 (default) |
| **Language** | Python 3.12 |
| **Auth** | Django built-in auth system |

---

## 📁 Project Structure

```
django_projects/
├── django_projects/          # Project configuration
│   ├── settings.py           # Django settings
│   ├── urls.py               # Root URL configuration
│   ├── wsgi.py               # WSGI entry point
│   └── asgi.py               # ASGI entry point
├── tweets/                   # Main application
│   ├── models.py             # Tweet model
│   ├── views.py              # View functions
│   ├── urls.py               # App URL routes
│   ├── forms.py              # Tweet creation/edit form
│   ├── admin.py              # Admin registration
│   └── templates/            # App-specific templates
│       ├── tweet_list.html   # Home feed / search results
│       ├── tweet_form.html   # Create / edit tweet form
│       ├── tweet_delete.html # Delete confirmation page
│       └── index.html        # Landing page
├── templates/                # Global templates
│   ├── layout.html           # Base template (navbar + layout)
│   └── registration/         # Auth templates
│       ├── login.html
│       ├── register.html
│       └── logged_out.html
├── static/
│   └── css/
│       └── style.css         # Custom dark theme styles
├── media/
│   └── photos/               # Uploaded tweet images
├── db.sqlite3                # SQLite database
├── manage.py                 # Django management script
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.12** or higher
- **pip** (Python package manager)

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/TweetApp.git
   cd django_projects
   ```

2. **Create a virtual environment**

   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**

   - **Windows:**
     ```bash
     venv\Scripts\activate
     ```
   - **macOS/Linux:**
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**

   ```bash
   pip install django pillow
   ```

5. **Run database migrations**

   ```bash
   python manage.py migrate
   ```

6. **Create a superuser** (for admin access)

   ```bash
   python manage.py createsuperuser
   ```

7. **Start the development server**

   ```bash
   python manage.py runserver
   ```

8. **Open your browser** and navigate to:

   | URL | Description |
   |-----|-------------|
   | `http://localhost:8000/` | Home (redirects to tweet feed) |
   | `http://localhost:8000/tweets/` | Tweet feed |
   | `http://localhost:8000/accounts/login/` | Login page |
   | `http://localhost:8000/tweets/register/` | Registration page |
   | `http://localhost:8000/admin/` | Admin panel |

---

## 📋 URL Routes

| URL Pattern | View | Name | Method | Auth Required |
|-------------|------|------|--------|:---:|
| `/` | Redirect → `/tweets/` | `home` | GET | No |
| `/tweets/` | `tweet_list` | `tweet_list` | GET | No |
| `/tweets/search/` | `search_tweets` | `search_tweets` | GET | No |
| `/tweets/create/` | `tweet_create` | `tweet_create` | GET/POST | Yes |
| `/tweets/edit/<id>/` | `tweet_edit` | `tweet_edit` | GET/POST | Yes |
| `/tweets/delete/<id>/` | `tweet_delete` | `tweet_delete` | GET/POST | Yes |
| `/tweets/register/` | `register` | `register` | GET/POST | No |
| `/accounts/login/` | Django auth login | `login` | GET/POST | No |
| `/accounts/logout/` | Django auth logout | `logout` | POST | Yes |

---

## 🗄 Data Model

### Tweet

| Field | Type | Description |
|-------|------|-------------|
| `id` | AutoField | Primary key (auto-generated) |
| `text` | CharField(280) | Tweet content |
| `user` | ForeignKey to User | Author of the tweet |
| `image` | ImageField (optional) | Attached image |
| `created_at` | DateTimeField | Auto-set on creation |
| `updated_at` | DateTimeField | Auto-set on save |

---

## 🎨 Design

The UI features a custom **dark theme** inspired by X (formerly Twitter) with:

- **Gradient backgrounds** — Deep blue-to-black gradient body
- **Glassmorphism navbar** — Frosted glass effect with backdrop blur
- **Card-based layout** — Responsive CSS Grid for tweet display
- **Smooth animations** — Fade-in transitions on page load
- **Custom scrollbar** — Styled to match the dark theme
- **Gradient buttons** — Primary (blue-purple) and danger (red) gradients
- **Hover effects** — Cards lift with shadow on hover
- **Mobile-first** — Fully responsive across all breakpoints

---

## ⚙️ Configuration

Key settings in `django_projects/settings.py`:

```python
# Media files (uploaded images)
MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Authentication redirects
LOGIN_URL = '/accounts/login'
LOGIN_REDIRECT_URL = '/tweets/'
LOGOUT_REDIRECT_URL = '/accounts/login'

# Static files
STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
```

---

## 🧪 Development

### Run Tests

```bash
python manage.py test
```

### Collect Static Files (for production)

```bash
python manage.py collectstatic
```

### Access Django Shell

```bash
python manage.py shell
```

---

## 📝 License

This project is open source and available under the MIT License.

---

## 👤 Author

**Chirag Tyagi**

Built with ❤️ using Django
