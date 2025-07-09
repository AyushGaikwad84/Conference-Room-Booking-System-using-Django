Conference Room Booking System
------------------------------

This is my first Django project built using Python and Django framework. It's a simple conference room booking platform where users can sign up, log in, contact admin, and book a room for meetings.


**Home Page**

![Screenshot 2025-07-09 224413](https://github.com/user-attachments/assets/4eacef25-8feb-4314-8c38-0533435d53f4)


![Screenshot 2025-07-09 224513](https://github.com/user-attachments/assets/297e4f4f-ee8f-4aae-8aae-8b077fea2d24)


![Screenshot 2025-07-09 224456](https://github.com/user-attachments/assets/929f3e4f-e2a3-4e69-aaa4-f213dff50b6d)


![Screenshot 2025-07-09 224537](https://github.com/user-attachments/assets/c0dc6cdd-6eaf-4949-912f-6b05a1c77db2)



***Admin View -***

Admin Panel to manage user and booking data


![Screenshot 2025-07-09 224720](https://github.com/user-attachments/assets/63e1bf7a-901f-42e5-84e5-789b1ed6f96e)


![Screenshot 2025-07-09 224900](https://github.com/user-attachments/assets/ca4bdb67-b89e-4cf4-87a5-a0cec4d3acf1)



Key Features:
-------------
- User Registration with hashed passwords
- User Login with session-based tracking
- Contact Form with admin-side message management
- Room Booking Form with time/date and mobile validations
- Manual Payment Confirmation via checkbox
- Admin Panel to manage user and booking data
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
GitHub: github.com/AyushGaikwad84  
Email: ayushsgaikwad8480@gmail.com

Note:
-----
This project was made for learning purposes only. It includes basic functionality and can be further enhanced for production use.
