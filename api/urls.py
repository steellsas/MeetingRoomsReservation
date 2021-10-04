
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('rooms.urls')),
    path('', include('employees.urls')),
    path('', include('reservations.urls')),
    path('rest-auth/', include('rest_auth.urls')),
]
