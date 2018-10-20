from django.urls import path
from .views import VenuesView

urlpatterns = [
    path('best-venues/', VenuesView.as_view(), name="venues")
]