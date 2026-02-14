from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import render, redirect
from .models import Forbids
from .models import Listing, Category
from .models import ActiveLisitng
from .models import ListingPage


from .models import User


def index(request):
    return render(request, "auctions/index.html")


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
def Forbids(request):
    if request.method=="POST":
        text=request.POST.get("text")
        if text:
            Forbids.objects.create(text=text)
            return redirect("Forbids")
   
        return render(request,"Forbids.html")
def create_listing(request):
      if request.method=="POST":
         title=request.POST.get("title")
         description=request.POST.get("description")
         image_url=request.POST.get("image_url")

      Listing.objects.create(
            title=title,
            description=description,
            image_url=image_url,
            owner=request.user
        )  
      return render(request, "create_listing.html", {
    })   
def ActiveLisitng(request):
     if request.method=="POST":
         title=request.POST.get("title")
         description=request.POST.get("description")
         currentprice=request.POST.get("currentprice")
         photo=request.POST.get("photo")

def toggle_watchlist(request, listing_id):
    listing = get_object_or_404(Listing, id=listing_id)
    if request.user in listing.watchlist.all():
        listing.watchlist.remove(request.user)
    else:
        listing.watchlist.add(request.user)   
    return redirect("listing_detail", listing_id=listing.id) 
def my_watchlist(request):
    listings=request.user.watching.all()
    return render(request,"watchlist.html",{
           "listings":listings
    })

         

