# Django Tailwind Demo

This project is a small sandbox showing how to use **django-tailwind** to add Tailwind CSS to a Django application.

## Setup

1. Install dependencies:
   ```bash
   pip install django django-tailwind dramatiq django_dramatiq
   ```
2. Install Tailwind assets:
   ```bash
   cd ambar
   python manage.py tailwind install --no-input
   ```
3. Run migrations and start the development server:
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

To run the Dramatiq worker in another shell, execute:
```bash
python manage.py rundramatiq
```

Then open <http://127.0.0.1:8000/> to see a basic page styled with Tailwind.
