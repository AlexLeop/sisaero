from entrada.models import EntradasAero
from django.views.generic import ListView


class EntradaAeroListView(ListView):
    model = EntradasAero
    template_name = 'entrada/entrada_aero_list.html'  # Nome do template HTML
    context_object_name = 'entrada_aero'  # Nome da variável no template
    paginate_by = 10  # Número de registros por página

