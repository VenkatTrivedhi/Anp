from django.db import models


class Output(models.Model):
    precision = models.FloatField()
    recall = models.FloatField()
    accurancy = models.FloatField()



class Input(models.Model):
    file = models.FileField()
    output = models.OneToOneField(Output,on_delete=models.CASCADE,null=True,blank=True)
