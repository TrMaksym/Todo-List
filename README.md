# Todo-List

A simple Django web application for managing tasks and tags. Users can create, view, update, and delete tasks, assign tags to them, and filter tasks by tags.

Features

Create, edit, and delete tasks with a user-friendly interface.

Assign tags to tasks for categorization.

Toggle task completion status.

Create, edit, and delete tags.

Styled with Bootstrap 5 via crispy-bootstrap5.

```Installation

    Clone the repository:

    git clone <repository-url>
    cd Todo-List
```
```Create and activate a virtual environment:

python -m venv venv
venv\Scripts\activate  # On Windows
```

```Install dependencies:

pip install -r requirements.txt
```

```Apply migrations:
python manage.py migrate
```

```Run the server:
python manage.py runserver
```

Requirements

Django 5.2

django-crispy-forms

crispy-bootstrap5

django-debug-toolbar

python-decouple See requirements.txt for details.