from django.urls import path
from .views import *

urlpatterns = [
    path('calendar/', calendarView, name="calendar-view"),
]