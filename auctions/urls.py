from django.urls import path
from .views import Forbids

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("Forbids/", Forbids, name="Forbids"),
    path("watch/<int:listing_id>/", views.toggle_watchlist, name="toggle_watchlist"),
    path("watch/<int:listing_id>/", views.toggle_watchlist, name="toggle_watchlist"),

]
