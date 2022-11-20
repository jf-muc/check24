from django.db import models


class Offer(models.Model):
    Hotelid = models.IntegerField(name="Hotel_ID", primary_key=True)
    depaturedate = models.DateTimeField(name="depatureDate")
    returndate = models.DateTimeField(name="returnDate")
    countadults = models.IntegerField(name="countAdults")
    countchildren = models.IntegerField(name="countChildren")
    price = models.IntegerField(name="price")
    inbounddepartureairport = models.TextField(
        max_length=3, name="inbounddepartureairport")
    inboundarrivalairport = models.TextField(
        name="inboundarrivalairport", max_length=3)
    inboundairline = models.TextField(name="inboundairline", max_length=3)
    inboundarrivaldatetime = models.DateTimeField(
        name="inboundarrivaldatetime")
    outbounddepartureairport = models.TextField(
        name="outbounddepartureairport", max_length=3)
    outboundarrivalairport = models.TextField(
        name="outboundarrivalairport", max_length=3)
    outboundairline = models.TextField(name="outboundairline", max_length=3)
    outboundarrivaldatetime = models.DateTimeField(
        name="outboundarrivaldatetime")
    mealtype = models.TextField(name="mealtype", max_length=9)
    oceanview = models.BooleanField(name="oceanview")
    roomtype = models.TextField(name="roomtype", max_length=11)

class Hotel(models.Model):
    Hotelid = models.IntegerField(name="Hotel_ID", primary_key=True)
    hotelname = models.TextField(name="hotelname", max_length=50)
    latitude = models.DecimalField(name="latitude", max_digits=12, decimal_places=10)
    longitude = models.DecimalField(name="longitude", max_digits=12, decimal_places=10)
    hotelstars = models.IntegerField(name="hotelstars")