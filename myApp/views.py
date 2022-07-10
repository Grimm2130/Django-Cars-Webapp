from django.shortcuts import render
from . import models

#Helper Functions
def createModels():
    
    pass

def bulkAdd():
    '''A function which Adds a cluster of set values for the Car types listed in index.html'''
    models.Cars.objects.create(Brand="Toyota", MPG = 30, Durability = 4.8, Weight = 1.5, TrunkSize = 30, AestheticsRating=4.5, OverallRating=4.9);

#------------------------------------------------------------------------------------------

# Create your views here.
def CarPage(request):
    '''A basic function to display the main webpage
    *Features: 
            Scrollable;
            Navigation bar showing an option of 10 cars, 
            clicking take the client to the car description page;
            Include images of all the cars in the drop-down list
    '''
    #call model Creation function
    bulkAdd()
    #List of cars to be included in the main page
    myCars = {"CarList":['Toyota', 'Honda', 'Mercedes','Hyundai', 'Mazda', 'Lexus']}
    return render(request, "myApp/index.html", context=myCars)

def Toyota(request):
    '''Displays Specs for the Toyota brand'''
    bulkAdd()
    contextList = {"allCars": models.Cars.objects.all()}
    return render(request,"myApp/Toyota.html", context=contextList)

def Honda(request):
    
    '''This page makes use of contexts to show different descriptions of cars
        It includes images of the car selected in the navigation panel in the 
        it also includes a table of car specs
    '''
    return render(request,"myApp/Honda.html")

def Mercedes(request):
    
    '''This page makes use of contexts to show different descriptions of cars
        It includes images of the car selected in the navigation panel in the 
        it also includes a table of car specs
    '''
    return render(request,"myApp/Mercedes.html")

def Hyundai(request):
    
    '''This page makes use of contexts to show different descriptions of cars
        It includes images of the car selected in the navigation panel in the 
        it also includes a table of car specs
    '''
    return render(request,"myApp/Hyundai.html")

def Mazda(request):
    
    '''This page makes use of contexts to show different descriptions of cars
        It includes images of the car selected in the navigation panel in the 
        it also includes a table of car specs
    '''
    return render(request,"myApp/Mazda.html")


def Lexus(request):
    
    '''This page makes use of contexts to show different descriptions of cars
        It includes images of the car selected in the navigation panel in the 
        it also includes a table of car specs
    '''
    return render(request,"myApp/Lexus.html")




