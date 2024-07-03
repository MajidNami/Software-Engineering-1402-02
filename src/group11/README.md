# Newspaper Project

## Overview

The Newspaper Project is a Django-based web application that allows users to create, view, update, and delete articles and associated content such as authors, categories, and comments. The project also includes user-specific notes management.

## Features

- User Authentication and Authorization
- CRUD operations for Articles, Authors, Categories, and Comments
- User-specific Notes

## Technologies Used

- Django
- SQLite (default) or MySQL
- HTML/CSS

### Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/newspaper-project.git
    cd newspaper-project
    ```
   
2. **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Set up the database:**
    ```bash
    python manage.py migrate
    ```

4. **Create a superuser:**
    ```bash
    python manage.py createsuperuser
    ```

5. **Collect static files:**
    ```bash
    python manage.py collectstatic
    ```

6. **Run the development server:**
    ```bash
    python manage.py runserver
    ```

7. **Open the project in your browser:**
    Go to `http://127.0.0.1:8000/group11/` to view the homepage.

### Project Structure

- `group11/`: Main Django project directory.
  - `models.py`: Database models for the app.
  - `views.py`: View functions and classes for the app.
  - `urls.py`: URL configurations for the app.
  - `templates/`: HTML templates for the app.

### Usage

1. **Authors:**
   - Create, view, edit, and delete authors.
   - URL: `/authors/`

2. **Categories:**
   - Create, view, edit, and delete categories.
   - URL: `/categories/`

3. **Articles:**
   - Create, view, edit, and delete articles.
   - URL: `/articles/`

4. **Comments:**
   - View comments for an article.
   - Add new comments to an article.
   - URL: `/articles/<article_id>/comments/`

5. **Notes:**
   - Create, view, edit, and delete user-specific notes.
   - URL: `/notes/`



### Contact

For any inquiries, please contact joma.mo1381@gmail.com

---

Thank you for using the Newspaper Project!
