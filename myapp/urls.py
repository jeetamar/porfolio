from django.urls import path
from myapp import views
from .views import *

urlpatterns = [
    path('',views.home,name='home'),
]