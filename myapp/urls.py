from django.urls import path

from .views import home, root_page, temp_inherit_home, portfolio, classroom, student, classroom_qs

urlpatterns = [
    path('home/', home),
    path("temp-inherit-home/", temp_inherit_home, name="temp_inherit_home"),
    path("portfolio/", portfolio, name="portfolio"),
    path("classroom/", classroom, name="classroom"),
    path("student/", student, name="student"),
    path('classroom_qs/',classroom_qs, name="classroom_qs"),
    path('', root_page, name="root_page"),
]
