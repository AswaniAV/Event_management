from django.urls import path 
from . import views

urlpatterns = [
    
    path('home/' , views.home , name ='home'),
    path('contact/', views.contact_view, name='contact'),
    path('about/', views.about , name ='about'),
    path('events/', views.events , name = 'events'),
    path('booking/<int:event_id>', views.booking , name = 'booking'),
    path('', views.home , name = 'home'),
]