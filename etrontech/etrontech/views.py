from django.http import HttpResponse
from django.shortcuts import render


def homePage(request):
    data={
        'title':'Home Page',
        'bdata':'welcome to etron',
        'clist':{'a','b','c'},
        'numbers':[10,20,30,40],
        'student_details':[
            {'name':'vrajesh','phone':9265864747},
            {'name':'dako','phone':9568686865}
        ]
    }
    return render(request,"index.html",data)

def aboutUS(request):
    return HttpResponse("welcome to etrontech")

def course(request):
    return HttpResponse("welcome to course")

def courseDetails(request,courseid):
    return HttpResponse(courseid)