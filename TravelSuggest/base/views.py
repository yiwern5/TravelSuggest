from django.shortcuts import render
from .models import QueryData, ResultData

def home(request):
    queryData = QueryData.objects.last()
    resultsData = ResultData.objects.filter(query=queryData)
    data = {'QueryData': queryData,'ResultsData': resultsData}
    return render(request, 'base/home.html', data)