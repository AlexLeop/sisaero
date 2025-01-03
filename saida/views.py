from django.views.generic import ListView
from .models import SaidasAero


class SaidasAeroListView(ListView):
    model = SaidasAero
    template_name = 'saida/saidas_aero_list.html'  # Nome do template HTML
    context_object_name = 'saidas_aero'  # Nome da variável no template
    paginate_by = 10  # Número de registros por página
