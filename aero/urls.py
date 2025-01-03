from django.contrib.auth.views import LoginView
from django.urls import path
from . import views
from .views import ImportarPDFView, custom_logout

urlpatterns = [
    path("", views.cadastros_list, name="cadastros_list"),
    path('importar-pdf/', ImportarPDFView.as_view(), name='importar_pdf'),
    path('login/', LoginView.as_view(template_name='home/login.html'), name='login'),
    path('logout/', custom_logout, name='logout'),
]
