from django.urls import path
from .views import arithmeticApi

urlpatterns = [
    path('', arithmeticApi),
]