from django.shortcuts import render, redirect
from .models import QueryData, ResultData
from .forms import QueryForm

def home(request):
    queryForm = QueryForm()

    if request.method == 'POST':
        form = QueryForm(request.POST)
        if form.is_valid():
            print(request.POST)
            form.save()
            return redirect('query-result')

    data = {'QueryForm': queryForm}

    return render(request, 'base/home.html', data)

def queryResult(request):
    queryData = QueryData.objects.last()
    resultsData = ResultData.objects.filter(query=queryData)

    data = {'QueryData': queryData,'ResultsData': resultsData}
    return render(request, 'base/queryresult.html', data)