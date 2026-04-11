from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from .forms import EventoForm
from .models import Eventos, CICLOS


def index(request):
    eventos = Eventos.objects.all().order_by("-data_hora")

    ciclo_filtro = request.GET.get("ciclo", "")
    if ciclo_filtro:
        eventos = eventos.filter(ciclo=ciclo_filtro)

    context = {
        "eventos": eventos,
        "ciclo_filtro": ciclo_filtro,
        "mes_atual": timezone.now().strftime("%B de %Y"),
        "CICLOS": CICLOS,
    }
    return render(request, "eventos/index.html", context)


def adicionar(request):
    if request.method == "POST":
        form = EventoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Evento adicionado com sucesso!")
            return redirect("eventos:index")
    else:
        form = EventoForm(initial={"data_hora": timezone.now()})

    return render(request, "eventos/evento_form.html", {"form": form, "titulo": "Adicionar Evento"})


def editar(request, pk):
    evento = get_object_or_404(Eventos, pk=pk)
    if request.method == "POST":
        form = EventoForm(request.POST, instance=evento)
        if form.is_valid():
            form.save()
            messages.success(request, "Evento atualizado com sucesso!")
            return redirect("eventos:index")
    else:
        form = EventoForm(instance=evento)

    return render(request, "eventos/evento_form.html", {"form": form, "titulo": "Editar Evento"})


def excluir(request, pk):
    evento = get_object_or_404(Eventos, pk=pk)
    if request.method == "POST":
        evento.delete()
        messages.success(request, "Evento removido com sucesso!")
        return redirect("eventos:index")

    return render(request, "eventos/confirmar_exclusao.html", {"evento": evento})