
## Problem 1: Regular Expression 

The `reg.py` file contains code for extracting numbers from text using regular expressions. 


## Problem 2: A functioning web  app with API

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
   git clone https://gitlab.com/jztchl/points-web-app.git
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


## Problem 3: 

### A. Scheduling Periodic Tasks

My experience with scheduling tools is somewhat limited, but I’ve learned about **Cron** and **at** during my MCA studies:

- **Cron**: Excellent for scheduling recurring tasks on UNIX-like systems. It’s highly reliable and scalable, making it ideal for tasks that need to run at regular intervals.
- **at**: Suitable for one-time tasks that need to be executed at a specific future time.

For most periodic tasks, **Cron** would be my preferred choice due to its robustness and scalability. If the scheduling needs become more complex, tools like **Celery** might offer more flexibility and features.

### B. Flask vs. Django


**Choosing Flask:**
- **Microservices and Small Applications**: Use Flask when you are about to build a small, focused application or microservice; it is lightweight and does not burden you with superfluous features or components, leaving you all the freedom to design the application exactly as you need it. For starters, Flask is an excellent choice for prototyping or dashing out simple RESTful APIs super-quickly.

- **Flexibility**: Flask doesn't enforce any project structure; you are free to put your code anywhere you wish. In fact, sometimes this can be kind of a double-edged sword: it's really awesome if you know exactly how to do what you want and want to have a custom kind of architecture; otherwise, it might be very overwhelming to a beginner or to a more complex project that needs a little more structure in place.

- **Learning Curve**: Learning Flask is relatively easy, especially for beginners in web development. Getting a simple application up and running with Flask is so easy and can be done quickly without the need to learn much more about lots of other concepts or plenty of settings.

- **Extensions**: Flask has a large, active ecosystem of extensions that you can add to your app as needed. Whether it be adding support for database migrations, user authentication, or forms — you are free to pick and use what you want without being forced down a particular line of tools.

**Why Choose Django?**
- **Large and Scalable Projects**: Django has been designed for applications that are going to be large, where a lot of things come out of the box. It follows the batteries-included philosophy, meaning it comes with an admin panel, ORM (Object-Relational Mapping), and many other features out of the box, features that would naturally be included via some kind of extra integration in Flask. This is one reason Django is especially appropriate for sophisticated, data-driven websites.

- **Security**: Django comes prepackaged with loads of security features, such as protection from SQL injection, cross-site scripting (XSS), and cross-site request forgery (CSRF) by default. Everything is taken care of automatically by the framework, so developers can build secure applications without thinking too much about applying this or that explicit protection.

- **Rapid Development**: It offers a range of ready-to-use features that, in combination with Django, greatly speed project development. More so, projects that are based on common web patterns. For example, the admin interface automatically creates a read-and-write place around the contents of your database so that you don't have to make it yourself.

- **Scalability and Maintenance**: The strict structure enforced by Django results in a consistent layout of projects, which therefore eases the scalability and maintenance of large applications. The framework enforces best practices, featuring the MVT pattern, which enables the developers to be clean and organized in the development of their applications.

- **Community and Ecosystem**: Being a community-supported framework, Django enjoys support from a huge community which actively maintains its documentation and a good number of third-party packages. Whichever specialized feature you want to be a part of your app—a set of e-commerce features, a REST API service, or CMS functionality, you are bound to find a well-maintained Django package.

**When to Use Flask Over Django:**
- If you are developing a lightweight, single-purpose application and you don't need more support inbuilt.
- If you want complete control over what components are used in a system.
- In case you are prototyping or need to get your project up and running quickly and don't want to deal with many things.
- If you are OK with some more manual work in things like database management, authentication, and routing.

**When to Use Django Instead of Flask:**
- If you are building a complex application that needs an admin interface, user authentication, and an ORM right out of the box.
- If you require a lot of in-built security features.
- If you're working on a project that is likely to be complex and increase in complexity over time, such that it will need a well-organized, maintainable structure.
- If you see that you need good community support and an ecosystem of reusable apps or packages.


### C. Software Engineering Best Practices

- **Modularity**: Divide your code into small, more workable chunks or pieces (modules) in such a way that each module or any chunk contains some specific unit of work, and all of these independent pieces can be used time and again, i.e., independently.
- **Documentation**: Take notes and prepare README files that may help you or others understand the code and set up the project quickly.
- **Normalized Database Schema**: Arrange your database in such a way that it avoids duplication of data. It maintains consistency and is easily managed.
- **requirements.txt**: A file listing all libraries that will make another person replicate your environment and get their project running.

