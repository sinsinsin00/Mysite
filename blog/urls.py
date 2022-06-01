from django.urls import path
from blog import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("postlist/", views.postlist, name="postlist"),
    path("post/<int:pk>", views.PostDetailView.as_view(), name="post"),
]