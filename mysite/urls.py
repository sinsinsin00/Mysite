from django.contrib             import admin
from django.urls                import path, include
from django.views.generic       import RedirectView
from django.conf                import settings
from django.conf.urls.static    import static


urlpatterns = [
    path('',include('blog.urls')),
    path('',include('shinstagram.urls')),
    path('content/',include('content.urls')),
    path('user/',include('user.urls')),
    path('blog/',include('blog.urls')),
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)