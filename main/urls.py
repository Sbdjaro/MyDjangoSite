from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about", views.about, name="about"),
    path("workers", views.about_workers, name="about_workers"),
    path("workers/<int:employee_id>", views.about_workers_id, name="about_workers_id"),
    path("cases", views.about_cases, name="about_cases"),
]
