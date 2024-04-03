from django.db import models


class QueryData(models.Model):
    #user = 
    location = models.TextField(null=False, blank=False)
    duration = models.IntegerField(null=True, blank=True)
    budget = models.DecimalField(null=True, blank=True, max_digits=10, decimal_places=2)
    queryTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.location)
    
class ResultData(models.Model):
    query = models.ForeignKey(QueryData, on_delete=models.CASCADE)
    location = models.TextField(null=False, blank=False)
    day_of_travel = models.IntegerField(null=True, blank=True)
    time_of_day = models.TextField(null=True, blank=True)
    description = models.TextField(null=False, blank=False)
    image = models.TextField(null=False, blank=False)
    min_spend = models.DecimalField(null=True, blank=True, max_digits=10, decimal_places=2)
    max_spend = models.DecimalField(null=True, blank=True, max_digits=10, decimal_places=2)
    queryTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.location)