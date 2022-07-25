from django.urls import path
from blog import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("projects/", views.projects, name="projects"),
    path("skills/", views.skills, name="skills"),
    path("post/<int:pk>", views.PostDetailView.as_view(), name="post"),
]


