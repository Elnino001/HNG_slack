from django.urls import path
from .views import HngDetailsList
urlpatterns = [
    path('details/', HngDetailsList.as_view())
]