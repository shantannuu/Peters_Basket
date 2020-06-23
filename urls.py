from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="HOME"),
    path("About/", views.About, name="AboutUs"),
    path("Contact/", views.Contact, name="ContactUs"),
    path("Tracker/", views.Tracker, name="Tracker"),
    path("search/", views.search, name="Search"),
    path("products/<int:myid>", views.ProductView, name="ProductView"),
    path("Checkout/", views.Checkout, name="Checkout"),
    path("handlerequest/", views.handlerequest, name="handlerequest")
    ]