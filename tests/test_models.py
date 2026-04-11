import pytest
from django.utils import timezone
from django.core.exceptions import ValidationError
from eventos.models import Eventos


@pytest.mark.django_db
def test_criar_evento():
    evento = Eventos.objects.create(
        descricao="Reunião",
        ciclo="unico",
        data_hora=timezone.now() + timezone.timedelta(days=1),
        dia_inteiro=False,
    )
    assert evento.pk is not None


@pytest.mark.django_db
def test_str_evento():
    evento = Eventos(descricao="Aniversário")
    assert str(evento) == "Aniversário"


@pytest.mark.django_db
def test_listagem_eventos():
    Eventos.objects.create(
        descricao="Evento 1",
        ciclo="diario",
        data_hora=timezone.now() + timezone.timedelta(days=1),
        dia_inteiro=False,
    )
    Eventos.objects.create(
        descricao="Evento 2",
        ciclo="mensal",
        data_hora=timezone.now() + timezone.timedelta(days=2),
        dia_inteiro=True,
    )

    assert Eventos.objects.count() == 2


@pytest.mark.django_db
def test_data_no_passado_deve_falhar():
    evento = Eventos(
        descricao="Evento inválido",
        ciclo="unico",
        data_hora=timezone.now() - timezone.timedelta(days=1),
        dia_inteiro=False,
    )

    with pytest.raises(ValidationError):
        evento.full_clean()


@pytest.mark.django_db
def test_dia_inteiro_zera_horario():
    data = timezone.now() + timezone.timedelta(days=1)

    evento = Eventos(
        descricao="Dia inteiro",
        ciclo="unico",
        data_hora=data,
        dia_inteiro=True,
    )

    evento.full_clean()
    evento.save()

    assert evento.data_hora.hour == 0
    assert evento.data_hora.minute == 0


@pytest.mark.django_db
def test_filtro_por_ciclo():
    Eventos.objects.create(
        descricao="Diário",
        ciclo="diario",
        data_hora=timezone.now() + timezone.timedelta(days=1),
        dia_inteiro=False,
    )
    Eventos.objects.create(
        descricao="Mensal",
        ciclo="mensal",
        data_hora=timezone.now() + timezone.timedelta(days=2),
        dia_inteiro=False,
    )

    eventos_diarios = Eventos.objects.filter(ciclo="diario")
    assert eventos_diarios.count() == 1