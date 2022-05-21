from django.urls import path
from . import views

urlpatterns = [
    path('', views.CourseListViews.as_view(), name="home")
]
