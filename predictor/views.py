from django.shortcuts import render
from .models import prediction_data
from django.contrib import messages
from django.core import serializers
from django.http import JsonResponse

# Create your views here.

import sklearn.externals
import joblib
import pandas as pd

modelReload = joblib.load('./models/HeartModel.pkl')




def index(request):
    context = {'a': 'Hello world!'}
    return render(request, 'index.html', context)


def predictMPG(request):
    # print(request)
    if request.method == 'POST':
        # print(request.POST.dict())
        temp = {}
        temp["gender"] = request.POST.get("genderVal")
        temp["age"] = request.POST.get("ageVal")
        temp["cigsPerDay"] = request.POST.get("cigsPerDayVal")
        temp["currentSmoker"] = request.POST.get("currentSmokerVal")
        temp["prevalentHyp"] = request.POST.get("prevalentHypVal")
        temp["totChol"] = request.POST.get("totCholVal")
        temp["sysBP"] = request.POST.get("sysBPVal")
        temp["diaBP"] = request.POST.get("diaBPVal")
        temp['BMI'] = request.POST.get("BMIVal")
        temp['heartRate'] = request.POST.get("heartRateVal")
        temp['glucose'] = request.POST.get("glucoseVal")
        print(temp)
    test_data = pd.DataFrame({'x': temp}).transpose()
    scoreval = modelReload.predict(test_data)[0]
    text1 = "Patient has a ten year risk of heart failure"
    text2 = "Congratulations! patient currently has no risk of heart failure "
    if scoreval == 1:
        context = {'Prediction': text1, 'temp': temp}
    else:
        context = {'Prediction': text2, 'temp': temp}
    return render(request, 'index.html', context)


def updateDataBase(request):
    data = prediction_data()
    data.gender = request.POST.get("genderVal")
    data.age = request.POST.get("ageVal")
    data.cigsPerDay = request.POST.get("cigsPerDayVal")
    data.currentSmoker = request.POST.get("currentSmokerVal")
    data.prevalentHyp = request.POST.get("prevalentHypVal")
    data.totChol = request.POST.get("totCholVal")
    data.sysBP = request.POST.get("sysBPVal")
    data.diaBP = request.POST.get("diaBPVal")
    data.bmi = request.POST.get("BMIVal")
    data.heartRate = request.POST.get("heartRateVal")
    data.glucose = request.POST.get("glucoseVal")

    text1 = "Patient has a ten year risk of heart failure"

    if request.POST.get("predictVal") == text1:
        data.prediction = 0
    else:
        data.prediction = 1

    data.save()
    report = messages.success(request, "Data added successfully")
    context = {'report': report}
    return render(request, 'index.html', context)




def dashboard_with_pivot(request):
    return render(request, 'viewDB.html', {})


def pivot_data(request):
    dataset = prediction_data.objects.all()
    data = serializers.serialize('json', dataset)
    return JsonResponse(data, safe=False)