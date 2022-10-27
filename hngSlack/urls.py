from django.urls import path
from .views import HngDetailsList
urlpatterns = [
    path('', HngDetailsList.as_view())
]