from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .forms import *
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


#def app7(request):
    #Sreturn render(request, 'forms.html')

def submitmyform(request):
    mydictionary = {
        "var1" : request.POST['mytext'],
        "var2" : request.POST['mytextarea'],
        "method" : request.method
    }
    return JsonResponse(mydictionary)


def myform2(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            title = request.POST['title']
            subject = request.POST['subject']
            email = request.POST['email']
            mydictionary1 = {
                "form" : FeedbackForm()
            }
            errorflag = False
            Errors = []
            if title != title.upper():
                errorflag = True
                errormsg = "Title should be in Capital"
                Errors.append(errormsg)
            import re
            regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
            if not re.search(regex,email):
                errorflag = True
                errormsg = "Not a Valid Email address"
                Errors.append(errormsg)
            if errorflag != True:
                mydictionary1["success"] = True
                mydictionary1["successmsg"] = "Form Submitted"
            mydictionary1["error"] = errorflag
            mydictionary1["errors"] = Errors
            print(mydictionary1)
            return render(request,'myform2.html',context=mydictionary1)

