from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('core.urls', namespace="mischief")), 
    path('', include('users.urls', namespace="users")), 
    path('nibble/', include('nibble.urls', namespace="nibble")), 
    path('squeak/', include('squeak.urls', namespace="squeak")), 
    path('scuffle/', include('scuffle.urls', namespace="scuffle"))
]
