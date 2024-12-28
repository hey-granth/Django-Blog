# Django Notes

## Flask VS Django

- Flask is a micro web framework for Python based on Werkzeug, Jinja 2 and good intentions.
- Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design.

## Django File Structure

![img.png](django-tree-structure.png)

- `blog/admin.py`: Registers and manages the admin interface for the blog app.

- `blog/apps.py`: Configuration for the blog app within the project.

- `blog/__init__.py`: Marks the blog directory as a Python package.

- `blog/migrations/__init__.py`: Marks the migrations folder as a Python package; used for database migrations.

- `blog/models.py`: Defines the database schema and data structure for the blog app.

- `blog/tests.py`: Contains test cases for the blog app to ensure functionality.

- `blog/views.py`: Contains logic to handle HTTP requests and responses for the blog app.

- `db.sqlite3`: SQLite database file storing the project's data.

- `django_project/asgi.py`: Configures the ASGI application for handling asynchronous web requests.

- `django_project/__init__.py`: Marks the django_project directory as a Python package.

- `django_project/settings.py`: Contains configuration settings for the Django project.

- `django_project/urls.py`: Maps URLs to their respective views in the project.

- `django_project/wsgi.py`: Configures the WSGI application for serving the project in production.

- `manage.py`: A command-line utility for managing the Django project (e.g., running the server, migrations).

---
## include() function
- include() function allows referencing other URL configurations.
- include function cuts off the URL which is already processed and sends the remaining string to the included URLconf for further processing.
- When we go to `localhost/blog/` it will cut off the `blog/` part and send the remaining string to the blog app's URLconf for further processing.
- When er go to `localhost/about/` it will cut off the `about/` part and send the remaining string to the about app's URLconf for further processing.

---