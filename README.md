# Django Bootstrap Portfolio Site

Демонстрационный Django проект, демонстрирующий наследование шаблонов, переиспользуемые компоненты через includes и интеграцию Bootstrap 5. Создан в рамках курса по веб-разработке с фокусом на основы Django.

**Автор:** Георгий Белянин (Georgy Belyanin)  
**Email:** georgy.belyanin@gmail.com

![Django](https://img.shields.io/badge/Django-5.0+-092E20?style=flat&logo=django&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-7952B3?style=flat&logo=bootstrap&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat&logo=python&logoColor=white)

## 🎯 Learning Objectives

This project demonstrates:
- **Template Inheritance**: Using `{% extends %}` for DRY (Don't Repeat Yourself) principle
- **Includes**: Separating reusable components (nav, footer) into dedicated files
- **URL Routing**: Named URL patterns and `{% url %}` template tags
- **Bootstrap Integration**: Responsive design using Bootstrap 5
- **Django Best Practices**: Proper project structure and static file management

## 📁 Project Structure

```
django-bootstrap-site/
├── config/                 # Project configuration
│   ├── settings.py        # Django settings
│   ├── urls.py            # Root URL configuration
│   ├── asgi.py
│   └── wsgi.py
├── main/                   # Main application
│   ├── templates/
│   │   └── main/
│   │       ├── base.html           # Base template
│   │       ├── home.html           # Home page
│   │       ├── about.html          # About page
│   │       ├── projects.html       # Projects showcase
│   │       ├── contact.html        # Contact page
│   │       └── includes/
│   │           ├── nav.html        # Navigation menu
│   │           └── footer.html     # Footer
│   ├── static/
│   │   └── main/
│   │       └── css/
│   │           └── site.css        # Custom styles
│   ├── views.py           # View functions
│   ├── urls.py            # App URL patterns
│   └── ...
├── .gitignore
├── requirements.txt
├── manage.py
└── README.md
```

## 🚀 Quick Start (Windows 11)

### Prerequisites
- Python 3.10 or higher
- Git (optional, for cloning)

### Installation

1. **Clone the repository** (or download ZIP)
   ```powershell
   git clone https://github.com/yourusername/django-bootstrap-portfolio.git
   cd django-bootstrap-portfolio
   ```

2. **Create and activate virtual environment**
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

   > **Note:** If you get an execution policy error, run PowerShell as admin and execute:
   > ```powershell
   > Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
   > ```

3. **Install dependencies**
   ```powershell
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. **Run the development server**
   ```powershell
   python manage.py check
   python manage.py runserver
   ```

5. **Open in browser**
   Navigate to: `http://127.0.0.1:8000/`

## 📄 Pages

| Page | URL | Description |
|------|-----|-------------|
| **Home** | `/` | Welcome page with hero section and feature cards |
| **About** | `/about/` | Information about the project and skills |
| **Projects** | `/projects/` | Showcase of 6 example projects |
| **Contact** | `/contact/` | Contact form and information |

## 🎨 Features

### Template System
- **Base Template** (`base.html`): Contains common HTML structure, Bootstrap CDN links, and includes
- **Includes**: 
  - `nav.html`: Responsive Bootstrap navbar with named URL routing
  - `footer.html`: Site footer with copyright and links
- **Page Templates**: Extend base template and override content blocks

### Bootstrap Components Used
- Navbar (responsive with mobile toggle)
- Cards (project showcase)
- Jumbotron (hero section)
- Forms (contact page)
- Buttons and badges
- Grid system (responsive layout)

### URL Routing
All navigation uses Django's URL routing system:
```django
<!-- Instead of hardcoded paths -->
<a href="{% url 'home' %}">Home</a>
<a href="{% url 'about' %}">About</a>
<a href="{% url 'projects' %}">Projects</a>
<a href="{% url 'contact' %}">Contact</a>
```

## 🛠️ Technologies

- **Backend**: Django 5.0+
- **Frontend**: 
  - Bootstrap 5.3 (via CDN)
  - Custom CSS
- **Template Engine**: Django Templates (Jinja-based)
- **Python**: 3.10+

## 📝 Development Notes

### Key Concepts Demonstrated

1. **Template Inheritance**
   ```django
   {% extends 'main/base.html' %}
   ```

2. **Template Includes**
   ```django
   {% include 'main/includes/nav.html' %}
   {% include 'main/includes/footer.html' %}
   ```

3. **Named URL Patterns**
   ```python
   # urls.py
   path('about/', views.about, name='about')
   ```
   ```django
   <!-- template -->
   <a href="{% url 'about' %}">About</a>
   ```

4. **Static Files**
   ```django
   {% load static %}
   <link rel="stylesheet" href="{% static 'main/css/site.css' %}">
   ```

### Django Commands Reference

```powershell
# Check for issues
python manage.py check

# Run development server
python manage.py runserver

# Create a new app
python manage.py startapp appname

# Make migrations (if models change)
python manage.py makemigrations
python manage.py migrate
```

## 🧪 Testing the Project

After starting the server, verify:
- ✅ All 4 pages load without errors
- ✅ Navigation menu is identical across all pages
- ✅ Footer is identical across all pages
- ✅ All navigation links work correctly
- ✅ Bootstrap styles are applied (navbar, cards, etc.)
- ✅ Custom CSS is loaded
- ✅ Responsive design works on mobile

## 📚 What I Learned

- How to structure a Django project following best practices
- Template inheritance to avoid code duplication
- Using includes for reusable components
- Integrating Bootstrap 5 for responsive design
- Proper URL routing with named patterns
- Managing static files in Django
- Creating professional-looking web pages quickly

## 🔮 Future Enhancements

Potential improvements for learning:
- [ ] Add active page highlighting in navbar
- [ ] Implement working contact form with Django forms
- [ ] Add database models for projects
- [ ] Integrate user authentication
- [ ] Add custom 404 and 500 error pages
- [ ] Implement automated tests

## 👤 Автор

**Георгий Белянин (Georgy Belyanin)**  
Email: georgy.belyanin@gmail.com

## 📄 Лицензия

Это образовательный проект. Вы можете свободно использовать его в учебных целях.

## 🙋‍♂️ Вопросы?

Этот проект был создан в рамках курса по веб-разработке на Django. По вопросам, связанным с курсом, обращайтесь к материалам курса или к вашему преподавателю.

---

**Создано с ❤️ в рамках изучения веб-разработки на Django**
