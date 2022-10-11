"""src URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# Importar settings para poder usar imagenes en el proyecto:
from django.conf import settings


urlpatterns = [
    path('', include('core.urls')),
    # Rutas de administracion
    path('admin/', admin.site.urls),
    # Rutas de registration:
    path('accounts/', include('django.contrib.auth.urls')),      # Ruta de sobreescritura de login
    path('accounts/', include('registration.urls')),
]

# Mostrar imagenes en modo DEBUG:
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

# Cambiar el titulo del administrador de DJANGO:
admin.site.site_header = "Eder's Rules"