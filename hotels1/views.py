

# Create your views here.

from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import CustomUser
from django.contrib.auth import logout
# from .models import Booking  # Assuming you have a Booking model defined
# hotels/views.py
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from roomtypes.models import Roomtype




# Register View

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')  # Redirect to login after successful registration
    else:
        form = CustomUserCreationForm()

    return render(request, 'templates/register.html', {'form': form})

# Logout View

def logout_view(request):
    logout(request)
    messages.success(request, 'You have successfully logged out.')
    return redirect('index')  # Redirect to the home page or login page


# hotels/views.py


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful! You are now logged in.')
            return redirect('index')
        else:
            messages.error(request, 'Registration failed. Please try again.')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('index')
        else:
            messages.error(request, 'Invalid email or password.')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)  # Log the user out
    return render(request, 'logout.html')  # Render the logout template


def dashboard(request):
    bookings = Booking.objects.filter(user=request.user)  # Assuming there's a related booking model
    return render(request, 'dashboard.html', {'bookings': bookings})

def booking_form(request):
    if request.method == 'POST':
        # Handle the booking form submission (this depends on your form structure)
        # Save the booking information to the database
        pass  # Replace with your logic
    return render(request, 'booking_form.html')

# # hotels/views.py


# # def register(request):
# #     if request.method == 'POST':
# #         form = CustomUserCreationForm(request.POST)
# #         if form.is_valid():
# #             form.save()  # Save the new user
# #             return redirect('login')  # Make sure 'login' matches the name in urls.py
# #     else:
# #         form = CustomUserCreationForm()

# #     return render(request, 'register.html', {'form': form})

# # hotels/views.py


# def login_view(request):
#     form = AuthenticationForm()
#     if request.method == 'POST':
#         form = AuthenticationForm(data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('home')  # Redirect to a home page or dashboard after login
#     return render(request, 'templates/login.html', {'form': form})

# # hotels/views.py
# from django.shortcuts import render, redirect
# from .forms import CustomUserCreationForm

# def register(request):
#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()  # Save the new user
#             return redirect('login')  # Adjust this redirect to your login URL name
#     else:
#         form = CustomUserCreationForm()

#     return render(request, 'templates/register.html', {'form': form})




# hotels/views.py
# from django.shortcuts import render, redirect
# from .forms import CustomUserCreationForm

# def register(request):
#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()  # Save the new user
#             return redirect('login')  # Redirect to a login page after registration
#     else:
#         form = CustomUserCreationForm()

#     return render(request, 'templates/register.html', {'form': form})


# hotels/views.py
from .forms import CustomUserCreationForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the user to the database
            return redirect('login')  # Redirect to a login URL after registration
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})


def facility(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the user to the database
            return redirect('home')  # Redirect to a login URL after registration
    else:
        form = CustomUserCreationForm()
    return render(request, 'facility.html', {'form': form})

def amenity(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the user to the database
            return redirect('home')  # Redirect to a login URL after registration
    else:
        form = CustomUserCreationForm()
    return render(request, 'amenity.html', {'form': form})


def loan(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the user to the database
            return redirect('home')  # Redirect to a login URL after registration
    else:
        form = CustomUserCreationForm()
    return render(request, 'loan.html', {'form': form})

def payment_form(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the user to the database
            return redirect('home')  # Redirect to a login URL after registration
    else:
        form = CustomUserCreationForm()
    return render(request, 'payment_form.html', {'form': form})

def room_types(request):
    roomtypes = Roomtype.objects.order_by('-room_type')
    context = {"roomtypes" : roomtypes}
    return render(request, 'room_types.html', context)