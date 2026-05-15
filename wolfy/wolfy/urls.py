from django.contrib import admin
from django.urls import path, include # <--- IMPORTANTE EL 'include'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('inicio.urls')), # <--- ESTA ES LA CONEXIÓN
]