from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import  Main, Profile, UploadProfile

urlpatterns = [
    path("shinstagram/", Main.shinstagram, name="Main.shinstagram"),
    path('profile/', Profile.as_view()),
    path('profile/upload/', UploadProfile.as_view())
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)