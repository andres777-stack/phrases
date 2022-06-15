from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    #admin
    path('admin/docs/', include('django.contrib.admindocs.urls')), #como cualquier otra app, tiene su urls. 
    path('admin/', admin.site.urls),
    #User management
    path('account/', include('allauth.urls')),
    #Local apps
    path('', include('pages.urls')),
    path('phrases/', include('phrases.urls')),
    path('jobs/', include('jobs.urls')),
]
