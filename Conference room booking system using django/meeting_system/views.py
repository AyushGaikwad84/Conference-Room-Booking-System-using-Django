from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages
from bookingapp.models import useraccount,contactmsg,room_booking
from django.contrib.auth.hashers import make_password
from datetime import datetime

def home(request):
    user = request.session.get('user')
    return render(request, "index.html", {"user": user})


def contact_page(request):
    if request.method == "POST":
        t1 = request.POST.get("name")
        t2 = request.POST.get("email")
        t3 = request.POST.get("contact_number")
        t4 = request.POST.get("msg")
        messages.success(request,"Thanks for Contacting us!")

        contactmsg.objects.create(
            name = t1,
            email = t2,
            contact_number = t3,
            contact_msg = t4,
        )
        return render(request, "contact.html", {"msg": "Submitted successfully!"})

    return render(request, "contact.html")

def rooms_page(request):
    return render(request,"rooms.html")


# So this function get an room id from urls.py, and choose id and return new html file
def book_room(request, room_id):
    dummy_rooms = {
        1: {"title": "Executive Room", "price": "1500", "capacity": "10"},
        2: {"title": "Meeting Hub", "price": "1200", "capacity": "8"},
        3: {"title": "Team Room", "price": "1000", "capacity": "6"},
    }

    room = dummy_rooms.get(room_id)
    if not room:
        msg = "Room not found"
        return render(request, "book_room.html",{'roomnotfound': msg})

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        mbno = request.POST.get("mbno")
        booking_date = request.POST.get("booking_date")
        start_time = request.POST.get("start_time")
        end_time = request.POST.get("end_time")
        extras = request.POST.get("extras")

        # ✅ Validations
        if not mbno.isdigit() or len(mbno) != 10:
            msg = "Enter a valid 10-digit mobile number."
            return render(request, "book_room.html", {"msg": msg, "room": room})

        today = datetime.today().date()
        if booking_date < str(today):
            msg = "Booking date cannot be in the past."
            return render(request, "book_room.html", {"msg": msg, "room": room})

        if start_time >= end_time:
            msg = "End time must be after start time."
            return render(request, "book_room.html", {"msg": msg, "room": room})

        room_booking.objects.create(
            name=name,
            email=email,
            mbno = mbno,
            booking_date=booking_date,
            start_time=start_time,
            end_time=end_time,
            extras=extras,
            room_title=room['title'],
            room_capacity=room['capacity'],
        )

        return render(request, "book_room.html", {"name": name, "room": room, "toast": "Room Booked Successfully..."})

    return render(request, "book_room.html", {"room": room})

def signup(request):
    if request.method == "POST":
        signupname = request.POST.get("signupname")
        signupemail = request.POST.get("signupemail")
        signuppass = request.POST.get("signuppass")
        signupconfirmpass = request.POST.get("signupconfirmpass")
        if signuppass == signupconfirmpass:
            if useraccount.objects.filter(email=signupemail).exists():
                msg = "Email already registered"
                return render(request, "signup.html", {"msg": msg})
            if useraccount.objects.filter(name=signupname).exists():
                msg = "User Name already exists. Please use different username"
                return render(request, "signup.html", {"msg": msg})
            hashed_pass = make_password(signuppass)
            useraccount.objects.create(name = signupname, 
                                       email = signupemail, 
                                       password = hashed_pass)
            return redirect("login")
        else:
            msg = "Passwords do not match"
            return render(request, "signup.html", {"msg": msg})

    return render(request,"signup.html")

def login(request):
    msg = ""
    if request.method == "POST":
        logname = request.POST.get("logname")
        logpass = request.POST.get("logpass")

        try:
            user = useraccount.objects.get(name=logname, password=logpass)
            # user = request.session.get('user')
            request.session['user'] = user.name 
            return render(request, "index.html", {"user": user})
        except useraccount.DoesNotExist:
            msg = "Invalid credentials. User does not exist."

    return render(request, "login.html", {"msg": msg})

