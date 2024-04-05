from django.shortcuts import render, redirect
from .models import QueryData, ResultData
from .forms import QueryForm

def home(request):
    queryData = QueryData.objects.last()
    resultsData = ResultData.objects.filter(query=queryData)

    queryForm = QueryForm(instance=queryData)

    if request.method == 'POST':
        form = QueryForm(request.POST)                          # form = QueryForm(request.POST, instance=queryData) to repplace existing query
        if form.is_valid():
            form.save()

    data = {'QueryForm': queryForm, 
            'QueryData': queryData,
            'ResultsData': resultsData}

    return render(request, 'base/home.html', data)