from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("index", views.index, name="index"),
    path("aboutme", views.aboutme, name="aboutme"),
    path("projects", views.projects, name="projects"),
    path("contact", views.contact, name="Contact"),

]