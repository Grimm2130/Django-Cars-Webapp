from django.urls import path
from . import views

'''For mapping to main url page'''
app_name= "myApp"

urlpatterns = [
    path("", views.CarPage),         #Displays general car page
    path("Toyota/", views.Toyota, name ="Toyota"),   #Displays details on each car
    path("Honda/", views.Honda, name="Honda"),   #Displays details on each car
    path("Mercedes/", views.Mercedes, name="Mercedes"),   #Displays details on each car
    path("", views.Mazda, name="Mazda"),   #Displays details on each car
    path("", views.Lexus, name="lexus"),   #Displays details on each car
    path("", views.Hyundai, name="Hyundai")   #Displays details on each car
]
