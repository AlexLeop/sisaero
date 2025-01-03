from django.urls import path
from .views import SaidasAeroListView

urlpatterns = [
    path('saidas-aero/', SaidasAeroListView.as_view(), name='saidas_aero_list'),
]
