from django.urls                import path, include
from django.views.generic       import RedirectView
from django.conf                import settings
from django.conf.urls.static    import static
from content.views              import UploadFeed, UploadReply, TogleLike, TogleBookMark 



urlpatterns = [
    path('upload/', UploadFeed.as_view()),
    path('reply/',  UploadReply.as_view()),
    path('like/',  TogleLike.as_view()),
    path('bookmark/',  TogleBookMark.as_view()),
]

urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
