from django.shortcuts import render
from .models import QueryData, ResultData
from .forms import QueryForm

def home(request):
    queryForm = QueryForm()
    queryData = QueryData.objects.last()
    resultsData = ResultData.objects.filter(query=queryData)
    data = {'QueryForm': queryForm, 'QueryData': queryData,'ResultsData': resultsData}
    return render(request, 'base/home.html', data)