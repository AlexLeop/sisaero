from django.urls import path
from .views import EntradaAeroListView

urlpatterns = [
    path('entrada_aero/', EntradaAeroListView.as_view(), name='entrada_aero_list'),
]