from django.urls                import path, include
from django.views.generic       import RedirectView
from django.conf                import settings
from django.conf.urls.static    import static
from .views                     import Join, Login



urlpatterns = [
    path('user/join/',  Join.get  , name="get"),
    path('user/login/', Login.get , name="get"),
]

urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)