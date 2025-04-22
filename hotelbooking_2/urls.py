from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),  # Admin site
    path('hotels', include('hotels.urls')),  # Include the URLs from the hotels app
    path('', include('hotels.urls')),            # Optional: Redirect empty path to hotels
]

