from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),	  
    path('destroy_session', views.destroy),
    path('add_two', views.add_2),
    path('add', views.add_by),
]