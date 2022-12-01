
from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

app_name = "cargueArchivos"
urlpatterns = [
    path("", views.uploadFile, name = "cargueArchivos"),
    
]

if settings.DEBUG: 
    urlpatterns += static(
        settings.MEDIA_URL, 
        document_root = settings.MEDIA_ROOT
    )


