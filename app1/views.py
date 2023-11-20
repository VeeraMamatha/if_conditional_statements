from django.shortcuts import render

# Create your views here.
def number(request):
    d={'a':100,'b':30,'c':500}
    return render(request,'number.html',d)