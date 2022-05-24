from django.urls import path
from . import views

urlpatterns = [
    path('', views.CourseListViews.as_view(), name="home"),
    path('our-restaurant/', views.restaurant_view, name='our-restaurant')
]