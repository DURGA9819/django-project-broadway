from django.shortcuts import render
from django.http import HttpResponse

from .models import ClassRoom

def home(request):
    return HttpResponse("""

<html>
                        <head>
                        <title>My project</title>
                        </head>
                        <body>
                        <h1>This is the home page</h1>
                        </body>

</html>


""")

def root_page(request):
    return render(request, template_name="myapp/root_page.html")


def temp_inherit_home(request):
    return render(request, template_name="myapp/temp_inherit_home.html")

def portfolio(request):
    return render(request, template_name="myapp/portfolio.html")

def classroom(request):
    classrooms=[
        {"name": "one", "address":"KTM"},
        {"name": "two", "address":"BTM"},
        {"name": "three", "address":"TTM"},
        {"name": "four", "address":"RTM"},
        {"name": "five", "address":"SPT"},
    ]
    return render(request, template_name="myapp/classroom.html", context={"classroom_name": "one", "location":"ktm", "classrooms":classrooms})

def student(request):
    students = [
    {"name": "Jon", "age": 21, "address": "KTM", "email": "jon@email.com"},
    {"name": "Jane", "age": 22, "address": "PKR", "email": "jane@email.com"},
    {"name": "Hary", "age": 23, "address": "BKT", "email": "hary@email.com"},
    {"name": "Ken", "age": 34, "address": "LTP", "email": "ken@email.com"},
]
    return render(request, template_name="mapp/student.html", context= {"students":students})

def classroom_qs(request):
    classrooms=ClassRoom.objects.all()
    return render(request, template_name="myapp/classroom_qs.html",context={"classrooms":classrooms})