# Points Webapp

Welcome to the Points Webapp! This Django-based application lets users track and manage tasks related to various apps and keep track of their points. With separate panels for users and admins, it offers a comprehensive way to handle app-related tasks and rewards.

## Key Features

### User Panel

- **User Dashboard:** `/user-panel/` - Renders the HTML dashboard for managing tasks and points.
- **Login:** `/user-login/` - API endpoint for secure user login.
- **Token Refresh:** `/token/refresh/` - API endpoint to refresh session tokens.
- **Register:** `/register/` - API endpoint for user registration.
- **App List:** `/apps-list/` - API endpoint to retrieve the list of available apps.
- **Upload Task:** `/task/upload/` - API endpoint to submit task screenshots.
- **User Profile:** `/user/profile/` - API endpoint to view  user profile.
- **Points Summary:** `/user/points/` - API endpoint to check total points.
- **Completed Tasks:** `/completed-tasks/` - API endpoint to view completed tasks.

### Admin Panel

- **Admin Dashboard:** `/admin-panel/` - Renders the HTML dashboard for managing app tasks and user activities.
- **Admin Login:** `/admin-login/` - API endpoint for secure admin login.
- **Token Refresh:** `/token/refresh/` - API endpoint to refresh session tokens.
- **Restricted View:** `/admin-only/` - API endpoint for accessing admin-only information.
- **Create App:** `/app/create/` - API endpoint to add new apps.
- **App List:** `/apps-list/` - API endpoint to retrieve the list of available apps.
- **Delete App:** `/app/delete/<int:pk>/` - API endpoint to remove apps from the system.

## Technologies Used

- **Django**: The backbone of the application, making development and management straightforward.
- **SQLite**: A simple, reliable database for storing data.
- **JWT (JSON Web Tokens)**: For secure authentication.
- **Django REST Framework**: To build the APIs that power the app.

## Deployment

### Online Deployment

The project is deployed on [PythonAnywhere](https://jztchl.pythonanywhere.com/user-panel/). You can access it here

### Local Deployment

To run the project locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/jztchl/points-webapp.git
   cd points-webapp
   ```

2. Set up a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Apply database migrations:

   ```bash
   python manage.py migrate
   ```

5. Start the development server:
   ```bash
   python manage.py runserver
   ```

