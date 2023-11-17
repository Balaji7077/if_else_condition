from django.shortcuts import render

# Create your views here.
def condition(request):
    d={'a':100,'b':200,'c':300}
    return render(request,'condition.html',d)

def if_elif_else(request):
    d={'a':100,'b':2000,'c':300}
    return render(request,'if_elif_else.html',d)

def if_else(request):
    d={'a':100,'b':2000,'c':300}
    return render(request,'if_else.html',context=d)

def neastedif(request):
    d={'a':100,'b':2000,'c':3000}
    return render(request,'neastedif.html',context=d)
