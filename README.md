# Django Blog API

## Overview


This Django application provides a blog platform with functionalities including blog management, category management, author profiles, reviews, and blog images. The API is built using Django REST Framework (DRF) and supports filtering, searching, pagination, and OAuth authentication using JWT.

## Installation

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/qobiljons/blog-api.git


2. **Install Dependencies:**
   ```bash
   pipenv install
   pipenv shell  # Activate virtual environment (optional)

3. **Set Up Environment Variables**
   Create a file named .env in the root directory. Add the following lines, replacing placeholders:
   ```bash
   SECRET_KEY=your-secret-key
   DEBUG=True
   DB_NAME= add_db_name
   DB_USER=add_db_user
   DB_PASSWORD=password
   DB_HOST=add_host
   DB_PORT=3306
4. **Run Migrations**
    ```bash
   python manage.py migrate
     

5. **  Run the development server**
   ```bash
   python manage.py runserver

6. **Usage**
   Visit http://localhost:8000/ in your browser.
   To fully use the api,
   first register and start using the api fully!
   
   #Note: This is a basic setup guide. Additional configuration and development steps might be required.

## API Endpoints

### Authentication Endpoints

- **POST /api/token/** - Obtain a JWT token by providing username and password.
- **POST /api/token/refresh/** - Refresh a JWT token.
- **POST /api/token/revoke/** - Revoke a JWT token.

### Author Endpoints

- **GET /authors/me/** - Retrieve or update the profile of the current authenticated author.
- **GET /authors/{id}/** - Retrieve author details.
- **PUT /authors/{id}/** - Update author details.
- **DELETE /authors/{id}/** - Delete an author.

### Blog Endpoints

- **GET /blogs/** - List all blogs.
- **POST /blogs/** - Create a new blog.
- **GET /blogs/{id}/** - Retrieve details of a specific blog.
- **PUT /blogs/{id}/** - Update a specific blog.
- **DELETE /blogs/{id}/** - Delete a specific blog.

### Category Endpoints

- **GET /categories/** - List all categories.
- **POST /categories/** - Create a new category.
- **GET /categories/{id}/** - Retrieve details of a specific category.
- **PUT /categories/{id}/** - Update a specific category.
- **DELETE /categories/{id}/** - Delete a specific category. *Note: Categories with associated blogs cannot be deleted.*

### Review Endpoints

- **GET /blogs/{blog_pk}/reviews/** - List all reviews for a specific blog.
- **POST /blogs/{blog_pk}/reviews/** - Create a new review for a specific blog.
- **GET /blogs/{blog_pk}/reviews/{id}/** - Retrieve details of a specific review.
- **PUT /blogs/{blog_pk}/reviews/{id}/** - Update a specific review.
- **DELETE /blogs/{blog_pk}/reviews/{id}/** - Delete a specific review.

### Blog Image Endpoints

- **GET /blogs/{blog_pk}/images/** - List all images for a specific blog.
- **POST /blogs/{blog_pk}/images/** - Upload a new image for a specific blog.
- **GET /blogs/{blog_pk}/images/{id}/** - Retrieve details of a specific image.
- **DELETE /blogs/{blog_pk}/images/{id}/** - Delete a specific image.

## Views

- **home**: Renders the homepage.
- **docs**: Renders the documentation page.
- **about**: Renders the about page.
- **custom_404**: Renders a custom 404 error page.

## Authentication

- **OAuth with JWT**: The API uses JSON Web Tokens (JWT) for authentication. Obtain and manage tokens via the authentication endpoints.

## Custom Permissions

- **IsOwnerOrReadOnly**: Allows modification only by the owner.
- **IsAdminOrReadOnly**: Grants full access to admins, read-only access to others.
- **IsAuthorOrReadOnly**: Allows modification only by the author.
- **IsBlogOwnerOrReadOnly**: Allows modification only by the blog owner.

## Filtering, Searching, and Pagination

- **Filtering**: Filter blogs by various parameters using `BlogFilter`.
- **Searching**: Search blogs by title.
- **Pagination**: Paginate API responses using `DefaultPagination`.

## Customization

- **Pagination**: Customize pagination settings in `DefaultPagination`.
- **Filters**: Modify `BlogFilter` for custom filtering options.

