from django.urls import path
from . import views

urlpatterns = [
    path('', views.CourseListViews.as_view(), name="home"),
    path('our-restaurant/', views.restaurant_view, name='our-restaurant'),
    path('booking/', views.booking_view, name='booking'),
    path('view-bookings/', views.booking_view_update, name='update-booking'),
    path('menu/', views.menu_list, name='menu'),
    path('team/', views.team_view, name='team'),
    path('gallery/', views.gallery_view, name='gallery'),
    path('faq/', views.faq_view, name='faq'),
    path('events/', views.events_view, name='events'),
    path('edit_booking/<booking_id>', views.edit_booking, name='edit-booking'),
    path(
        'delete_booking/<int:booking_id>/',
        views.delete_booking,
        name='delete_booking'
        ),
]
