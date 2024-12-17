from django.shortcuts import render
from django.http import HttpResponse
def runoob(request):
    views_dict = {"name":"菜鸟教程"}
    return render(request, "runoob.html", {"views_dict": views_dict})

def hello(request):
    return HttpResponse("Hello world ! ")