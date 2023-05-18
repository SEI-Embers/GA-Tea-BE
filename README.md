# API Documentation

This document provides an overview of the API endpoints available for the app. The API allows users to create, read, update, and delete posts and comments. Before accessing the API, users need to create an account.

## Base URL

The base URL for accessing the API endpoints is `https://ga-tea-be-production.up.railway.app/`. Please adjust the base URL based on your project setup and deployment configuration.

## Models

### UserManage Model

Explains the logic of user authentication.

### Account Model

- `bio`: TextField (blank=True)
- `github`: CharField (default='', blank=True)
- `linkedin`: CharField (default='', blank=True)
- `skills`: ArrayField (CharField(max_length=200), default=list)
- `is_active`: BooleanField (default=True)
- `is_staff`: BooleanField (default=False)
- `updated_at`: DateTimeField (auto_now=True)
- `pic`: CharField (default='https://imgur.com/a/2L57GM9')

### Post Model

- `title`: CharField (max_length=128, blank=True)
- `body`: TextField
- `pic`: CharField (blank=True)
- `skills`: ArrayField (CharField(max_length=200), null=True, blank=True)
- `timeline`: DateTimeField
- `created_at`: DateTimeField (default=timezone.now)
- `owner`: ForeignKey (settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="posts", null=True)
- `tag`: ManyToManyField (Hashtag, blank=True)

### Comment Model

- `body`: TextField
- `owner`: ForeignKey (settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="comments", null=True)
- `post`: ForeignKey (Post, on_delete=models.CASCADE, related_name="comments")

## Authentication Endpoints

### Login

- Endpoint: `/api/auth/login/`
- Method: POST
- Description: Login and obtain an access token.

### Registration

- Endpoint: `/api/auth/register/`
- Method: POST
- Description: Register a new user.

### Token Refresh

- Endpoint: `/api/auth/refresh/`
- Method: POST
- Description: Refresh an access token.

## User Endpoints

### Get All Users

- Endpoint: `/api/users/`
- Method: GET
- Description: Retrieve a list of all users.

### Get User Details

- Endpoint: `/api/users/{id}/`
- Method: GET
- Description: Retrieve details of a specific user by ID.

## Post Endpoints

### Get All Posts

- Endpoint: `/api/posts/`
- Method: GET
- Description: Retrieve a list of all posts.

### Get Post Details

- Endpoint: `/api/posts/{id}/`
- Method: GET
- Description: Retrieve details of a specific post by ID.

### Get Comments for a Post

- Endpoint: `/api/posts/{id}/comments/`
- Method: GET
- Description: Retrieve all comments for a specific post.

### Create Comment

- Endpoint: `/api/posts/{id}/comments/`
- Method: POST
- Description: Create a new comment for a post.

## Admin Panel

### Django Administration Panel

- Endpoint: `/admin/`
- Description: Access the Django administration panel. Only accessible to users with staff/admin privileges.

## CRUD Functionality for Posts and Comments

The API supports the following CRUD (Create, Read, Update, Delete) operations for posts and comments:

### Create

#### Create a Post

- Endpoint: `/api/posts/`
- Method: POST












Post Project items:
Career:
company_name = models.CharField()
status = models.CharField()
timeline = models.DateTimeField()
















