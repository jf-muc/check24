from django.urls import path

from . import views

app_name = 'searchengine'
urlpatterns = [
    path('', views.serachView, name='index'),
    path('results/<str:searchURL>', views.resultView, name='results'),
    path('booking/<str:bookingHotelID>', views.bookingView, name='booking')
]
