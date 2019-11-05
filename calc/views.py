from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html', {'name': 'Kiran'})
    #return HttpResponse("Hello world")

def add(req):
    val1 = req.POST['num1']
    val2 = req.POST['num2']
    res = int(val1) + int(val2)
    return render(req, 'result.html', {'result': res})