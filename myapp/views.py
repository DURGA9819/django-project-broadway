from django.shortcuts import render
from django.http import HttpResponse

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