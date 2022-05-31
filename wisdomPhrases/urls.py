from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/docs/', include('django.contrib.admindocs.urls')), #como cualquier otra app, tiene su urls. 
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('phrases/', include('phrases.urls')),
]
