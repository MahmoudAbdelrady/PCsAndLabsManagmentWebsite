from django.db import models

# Create your models here.
class AddLab(models.Model):
    Laboratory_ID = models.IntegerField(null=True , blank=True)
    Laboratory_Name = models.CharField(max_length=20,null=True , blank=True)
    Laboratory_Number = models.IntegerField(null=True , blank=True)
    Floor_Number = models.IntegerField(null=True , blank=True)
    NumOfPcs = models.IntegerField(null=True, blank=True)
    LabCapacity = models.IntegerField(null=True, blank=True)
    NumOfChairs = models.IntegerField(null=True , blank=True)
    LabStatus = models.CharField(max_length=18,null=True , blank=True) 
    def __str__(self):
        return self.Laboratory_Name

class ReportInfo(models.Model):
    ProblemList = [
        ('Software','software'),('Hardware','hardware')
    ]
    RLaboratory_ID = models.IntegerField(null=True, blank=True)
    RPcNum = models.IntegerField(null=True , blank=True)
    RProblemType = models.CharField(max_length=20,null=True,blank=True,choices=ProblemList)
    RDate = models.DateField()
    RDescription = models.CharField(max_length=200 , null=True , blank=True)
    
class AddNewPC(models.Model):
    PC_ID = models.IntegerField(null=True , blank=True)
    Lab_ID = models.IntegerField(null=True,blank=True)
    PCStatus = models.CharField(max_length=18,null=True , blank=True)
