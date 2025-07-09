Conference Room Booking System
------------------------------

This is my first Django project built using Python and Django framework. It's a simple conference room booking platform where users can sign up, log in, contact admin, and book a room for meetings.

Key Features:
-------------
- User Registration with hashed passwords
- User Login with session-based tracking
- Contact Form with admin-side message management
- Room Booking Form with time/date and mobile validations
- Manual Payment Confirmation via checkbox
- Admin Panel to manage user and booking data
- 404 error handling
- Responsive navigation and basic styling
- Welcome message and logout option in navbar
- Form data stored in the database and visible in admin

Technologies Used:
------------------
- Python 3.x
- Django 5.x
- HTML5 & CSS3
- SQLite (Default Django DB)
- Bootstrap (optional styling)
- Basic JavaScript (for toasts)

How to Run:
-----------
1. Clone or download the project folder.
2. Open terminal / command prompt in the project root directory.
3. Create and activate a virtual environment:
   - python -m venv venv
   - venv\Scripts\activate  (Windows)
   - source venv/bin/activate (Mac/Linux)

4. Install Django:
   - pip install django

5. Run migrations:
   - python manage.py makemigrations
   - python manage.py migrate

6. Run the server:
   - python manage.py runserver

7. Open in browser: http://127.0.0.1:8000/

Pages:
------
- /              => Home page
- /signup/       => Register new user
- /login/        => Login page
- /logout/       => Logout user
- /contact/      => Contact form
- /rooms/        => All rooms
- /book-room/id/ => Booking form for selected room

Folder Structure:
-----------------
- bookingapp/            - Main Django app
- templates/             - All HTML pages
- static/                - CSS and image files
- db.sqlite3             - Database file
- manage.py              - Django project entry point

To Do (Future Updates):
-----------------------
- Booking history for users
- User profile page
- FAQs section
- Razorpay or Stripe integration for real payment
- Prevent booking the same slot twice
- Admin dashboard improvements

Developer Info:
---------------
Created by Ayush  
GitHub: github.com/your-username  
Email: your.email@example.com

Note:
-----
This project was made for learning purposes only. It includes basic functionality and can be further enhanced for production use.
