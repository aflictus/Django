from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("menu", views.menu, name="menu"),
    path("contacts", views.contacts, name="contact"),
    path("delivery", views.delivery, name="delivery"),
    path("about-us", views.about_us, name="about-us"),
]
