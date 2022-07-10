from django.db import models

# Create your models here.

class Cars(models.Model):
    '''The Car model class. This will be used to Fill in tables with relevant class data '''
    Brand = models.CharField(max_length=10)
    MPG = models.IntegerField()
    Durability = models.FloatField()     #scale of 5
    Weight = models.FloatField()         #in Tons
    TrunkSize = models.IntegerField()    #in gallons
    AestheticsRating = models.FloatField()#scale of 5
    OverallRating = models.FloatField()  #scale of 5

    def __str__(self):
        return f"{self.Brand} with an MPG of {self.MPG}. "