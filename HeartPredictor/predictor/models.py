from django.db import models

# Create your models here.


class prediction_data(models.Model):
    gender = models.CharField(max_length=200)
    age = models.CharField(max_length=200)
    cigsPerDay = models.CharField(max_length=200)
    currentSmoker = models.CharField(max_length=200)
    prevalentHyp = models.CharField(max_length=200)
    totChol = models.CharField(max_length=200)
    sysBP = models.CharField(max_length=200)
    diaBP = models.CharField(max_length=200)
    bmi = models.CharField(max_length=200)
    heartRate = models.CharField(max_length=200)
    glucose = models.CharField(max_length=200)
    prediction = models.CharField(max_length=200)
