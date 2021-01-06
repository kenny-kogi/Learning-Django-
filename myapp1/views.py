from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.
def myfunctioncall(request):
    return HttpResponse("Hello World keny")

def math1(request):
    return HttpResponse("math is interesting")

def subtract(request, a,b):
    return HttpResponse(a - b)

def year(request, name, yob):
    myfirstDict = {
        'name' : name, 
        'year of birth' : yob
    }
    return JsonResponse(myfirstDict)

def app(request):
    return render(request, 'index.html')

def app2(request):
    return render(request, 'second.html')

def app3(request):
    var = 'Hello world'
    num1, num2 = 7, 7
    mydict = {
        "var" : var,
        "num1" : num1,
        "num2" : num2

    }

    return render(request, 'third.html',  context = mydict )


def app4(request):
    return render(request, 'firstimage.html')

def app5(request):
    return render(request, 'secondimage.html')

def app6(request, name):
    argname = str(name)
    namy = argname.lower()

    if (namy == 'django'):
        var = True
    elif (namy == 'python'):
        var = False

    mydicto = {
        'var' : var
    }    


    return render(request, 'thirdimage.html', context = mydicto)