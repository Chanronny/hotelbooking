# hotels/urls.py
from django.urls import path
from .views import (
    register,
    login_view,
    logout_view,
    dashboard,
    booking_form,
    about,
    home,
    facility,
    amenity,
    loan,payment_form,
    payment_form,
    room_types,
    
)

urlpatterns = [
    path('', home, name='home'),  # Home page
    path('about/', about, name='about'),  # About page
    path('register/', register, name='register'),  # Registration page
    path('login/', login_view, name='login'),  # Login page
    path('logout/', logout_view, name='logout'),  # Logout page
    path('dashboard/', dashboard, name='dashboard'),  # User dashboard
    path('booking_form/', booking_form, name='booking_form'),  # Booking form page
    path('facility/', facility, name='facility'),  # Facility page
    path('amenity/', amenity, name='amenity'),  # Amenity page
    path('loan/', loan, name='loan'),  # Loam Item page
    path('payment_form/', payment_form, name='payment_form'),  # Payment form page
    path('api/loan/', loan, name='loan'),  # Loan API endpoint
    path('amenity/path_to_previous_page/', loan, name='path_to_previous_page'),  # Path to previous form page
    path('room_types/', room_types, name='room_types'),  # Room Types page
]
