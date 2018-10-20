from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url(r'^$', views.map, name='map'),
    # path('', views.map.as_view(), name='map'),
    path('create/', views.AddSupplierView.as_view(), name='add_supplier'),
]