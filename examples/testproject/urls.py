from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/', include('contact_form.urls')),
    path('simple/', include('simple.urls')),
]
