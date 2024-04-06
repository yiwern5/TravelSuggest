from django.shortcuts import render, redirect
from .models import QueryData, ResultData
from .forms import QueryForm
import google.generativeai as genai

def home(request):
    queryData = QueryData.objects.last()
    resultsData = ResultData.objects.filter(query=queryData)

    queryForm = QueryForm()                                     # QueryForm(instance=queryData)

    if request.method == 'POST':
        form = QueryForm(request.POST)                          # form = QueryForm(request.POST, instance=queryData) to repplace existing query
        if form.is_valid():
            query = form.save()
            return redirect('result', pk=query.id)
    
    data = {'QueryForm': queryForm, 
            'QueryData': queryData,
            'ResultsData': resultsData}

    return render(request, 'base/home.html', data)

def result(request, pk): 
    queryData = QueryData.objects.get(id=pk)
    data = {'QueryData': queryData}
    return render(request, 'base/result.html', data)

def generate_travel_suggestions(travel_query):

    genai.configure(api_key="AIzaSyCmfBtuVVD88DVXwXlJfK6wxz7V1zHsVVg")

    generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
    }

    safety_settings = [
        {
            "category": "HARM_CATEGORY_HARASSMENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_HATE_SPEECH",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
    ]

    model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                        generation_config=generation_config,
                        safety_settings=safety_settings)
    
    prompt_parts = [
    "Given a travel location, corresponding travel duration and requirements."
    + "Generate travel suggestions for that location in a python dictionary format for use in Django( no need for it to be nested )." 
    + " Here are the wanted labels: Day of travel (e.g.1 ), Time of Travel (e.g. Morning, Evening), Description, Expected Spending, Additional Details, Image." 
    + "\n\nThings to take note of: \nIf the the number of days of the travel is greater than a day. Separate suggestions to morning, afternoon, evening and night."
    + "Travel suggestion should satisfy the travel requirements as specified by the query info."
    + "The image provided should be an image url that is callable i.e. from the internet and can be outputted in html using img tags."
        + "\n\nHere is the input in python dictionary format:" + travel_query,
    ]

    response = model.generate_content(prompt_parts)
    print(response.text)