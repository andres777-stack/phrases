from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #admin
    path('admin/docs/', include('django.contrib.admindocs.urls')), #como cualquier otra app, tiene su urls. 
    path('admin/', admin.site.urls),
    #User management
    path('account/', include('users.urls')),
    path('account/', include('allauth.urls')),
    #Local apps
    path('', include('pages.urls')),
    path('phrases/', include('phrases.urls')),
    path('jobs/', include('jobs.urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
