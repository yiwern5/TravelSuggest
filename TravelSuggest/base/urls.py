from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('query-result/', views.queryResult, name="query-result"),
]
