from django.urls import path
from . import views

urlpatterns = [
    path('', views.CourseListViews.as_view(), name="home"),
    path('our-restaurant/', views.restaurant_view, name='our-restaurant'),
    path('booking/', views.booking_view, name='booking'),
    path('menu/', views.menu_view, name='menu'),
    path('team/', views.team_view, name='team'),
    path('gallery/', views.gallery_view, name='gallery'),
    path('faq/', views.faq_view, name='faq'),
    path('events/', views.events_view, name='events'),
    path('member/', views.member_view, name='member'),
]
