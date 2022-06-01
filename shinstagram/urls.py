from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from shinstagram.views import  Main

urlpatterns = [
    path("shinstagram/", Main.shinstagram, name="Main.shinstagram"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)