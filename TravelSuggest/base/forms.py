from django.forms import ModelForm
from .models import QueryData

class QueryForm(ModelForm):
    class Meta:
        model = QueryData 
        fields = '__all__'