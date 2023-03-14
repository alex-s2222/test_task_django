from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, HttpResponse

from .forms import NewUserForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

from .models import Room, Booking
from django.db.models import Q


from datetime import datetime


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("main:main")
        messages.error(
            request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="main/register.html", context={"register_form": form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("main:main")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="main/login.html", context={"login_form": form})


def select_room(request, room_pk: int):
    log_message: str = None
    room: object = Room.objects.get(pk=room_pk)

    if request.method == "POST" and request.user.is_authenticated:
        date_now = datetime.now().date()
        start_date = datetime.strptime(
            request.POST['start_date'], '%Y-%m-%d').date()
        end_date = datetime.strptime(
            request.POST['end_date'], '%Y-%m-%d').date()

        if (start_date > end_date) or (start_date == end_date):
            log_message = "начальная дата должна быть больше конечной"
        elif (start_date < date_now) or (end_date < date_now):
            log_message = "даты должны быть больше сегодняшней"
        else:
            booking = Booking(
                room=room, start_date=start_date, end_date=end_date, user_name=request.user.username)
            booking.save()
            log_message = "комната забронирована"

    return render(request, template_name='rooms/view_room.html', context={'room': room, 'log': log_message})


def main(request):
    select_date_for_room: bool = None
    rooms: object = None
    if request.method == "POST":
        try:
            sort_by = request.POST['sort']
            if sort_by == '1':
                rooms = Room.objects.order_by('price')
            elif sort_by == '2':
                rooms = Room.objects.order_by('seat')
            elif sort_by == '3':
                select_date_for_room = True
                try:
                    start_date = datetime.strptime(request.POST['start_date'], '%Y-%m-%d').date()
                    end_date = datetime.strptime(request.POST['end_date'], '%Y-%m-%d').date()
                    
                    rooms = _search_rooms_by_date(start_date=start_date, end_date=end_date)
                except:
                    rooms = Room.objects.all()
        except:
            rooms = Room.objects.all()
    else:
        rooms = Room.objects.all()
    return render(request, template_name='main/main.html', context={'rooms': rooms, 'select_date': select_date_for_room})


def my_booking(request):
    if request.user.is_authenticated:
        user = request.user
        all_user_booking = Booking.objects.filter(user_name=user.username)
        return HttpResponse(render(request, template_name='main/booking.html', context={'all_booking': all_user_booking}))
    return redirect('/login')


def delete_room(request, booking_pk: int):
    booked_room = Booking.objects.get(pk=booking_pk)
    if request.method == "POST":
        booked_room.delete()
        return redirect('/my_booking/')
    return render(request=request, template_name="main/delete_booked.html", context={"booking": booked_room})


def _search_rooms_by_date(start_date: datetime, end_date: datetime) -> list[Room]:
    rooms_id_from_booked: list
    booked_room: list[object] = Booking.objects.filter(Q(start_date__range=(start_date, end_date)) or +
                                                       Q(end_date__range=(start_date, end_date)))

    rooms_id_from_booked = list({room.room_id for room in booked_room})

    rooms = Room.objects.exclude(pk__in=rooms_id_from_booked)
    return rooms
