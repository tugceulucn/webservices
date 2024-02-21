from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.
def index(request):
    return render(request, "HomePage/homepage.html")

def param_details(request):
    return render(request, "HomePage/parametre_details.html")
    