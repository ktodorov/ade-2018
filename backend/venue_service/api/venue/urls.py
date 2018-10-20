from django.urls import path
from .views import ListVenuesView

urlpatterns = [
    path('venues/', ListVenuesView.as_view(), name="venues-all")
]