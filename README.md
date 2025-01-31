# Django To-Do List App

## Overview
A simple To-Do List application built with Django, allowing users to add and delete tasks.

## Features
- Add tasks with a title
- Mark tasks as completed
- Delete tasks from the list

## Installation

### 1. Clone the Repository
```sh
git clone https://github.com/Shadowsweep/Django_todo_list.git
cd todo_project
```

### 2. Set Up Virtual Environment
```sh
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3. Install Dependencies
```sh
pip install django
```

### 4. Run Migrations
```sh
python manage.py migrate
```

### 5. Run Development Server
```sh
python manage.py runserver
```
Visit: **http://127.0.0.1:8000/**

## Project Structure
```
django-todo-list/
│-- todo_project/
│   │-- settings.py
│   │-- urls.py
│-- tasks/
│   │-- models.py
│   │-- views.py
│   │-- forms.py
│   │-- urls.py
│   │-- templates/tasks/task_list.html
│-- manage.py
│-- README.md
```

## Usage
1. Visit the home page.
2. Enter a task in the form and click "Add Task".
3. View the list of tasks with completion status.
4. Click "Delete" to remove a task.

## License
This project is open-source under the MIT License.

