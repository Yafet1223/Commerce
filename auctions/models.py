from django.contrib.auth.models import AbstractUser
from django.db import models
from django import forms
#auction listing
#comments
#for bids
class User(AbstractUser):
    pass
class AuctionListing(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    starting_bid=models.DecimalField(max_digits=10, decimal_places=2)
    current_bid=models.DecimalField(max_length=10, decimal_places=2, blank=True, null=True)

owner=models.ForeignKey(
    User,
    on_delete=models.CASCADE
    related_name="listings"
)
created_at=models.DateTimeField(auto_now_add=True)
is_active=models.BooleanField(default=True)
def __str__(self):
    return self.title
#comments
class Comments(models.model):
    text=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    
def __str__(self):
    return self.text
#forbids
class Forbids(models.model):
    text=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
def __str__(self):
  return self.text
class Forbids(models.model):
    text=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
def __str__(self):
    return self.text   
class Catagory(models.model):
    name=models.CharField()
def __str__(self):
    return self.name
class Listing(models.model):
    title=models.CharField()
    description=models.TextField()
    image_url=models.URLField(blank=True) 
    owner=models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="listings"
    )      
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
class ActiveLisitng(models.model):
    title=models.TextField()
    description=models.TextField()
    CurrentPrice=models.DecimalField()
    photo=models.URLfield(blank=True)
    owner=models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        name="ActiveListings"
    )
created_at=models.DateTimeField(auto_now_add=True)
def __str__(self):
    return self.title
class ListingPage(models.model):
    title=models.TextField()
    CurrentPrice=models.DecimalField()
    bidding_price=models.DecimalField()
    owner=models.ForeignKey(User, on_delete=models.CASCADE)
    watchlist=models.ManyToManyField(
        User,
        related_name="watching"
        blank=True

    )
    def __str__(self):
        return self.title
