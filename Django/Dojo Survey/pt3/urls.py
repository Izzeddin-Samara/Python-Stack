from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dojosurvey/', include('newapp.urls')),  # Reference the URLs of newapp
    path('', include('newapp.urls')),  # Redirect the root URL to newapp
]
