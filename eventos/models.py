from django.core.exceptions import ValidationError
from django.utils import timezone
from django.db import models
from datetime import timedelta

CICLOS = [
    ("unico", "Único"),
    ("diario", "Diário"),
    ("semanal", "Semanal"),
    ("mensal", "Mensal"),
    ("anual", "Anual"),
]
@property
def proxima_ocorrencia(self):
    if self.ciclo == "unico":
        return None

    data = self.data_hora

    if self.ciclo == "diario":
        return data + timedelta(days=1)

    if self.ciclo == "semanal":
        return data + timedelta(weeks=1)

    if self.ciclo == "mensal":
        return data.replace(month=data.month % 12 + 1)

    if self.ciclo == "anual":
        return data.replace(year=data.year + 1)
    
def validar_data(value):
    if value < timezone.now():
        raise ValidationError("Data/Horário definidos no passado.")


class Eventos(models.Model):

    descricao = models.CharField("Descrição", max_length=200)

    dia_inteiro = models.BooleanField("Dia inteiro?", default=False)

    data_hora = models.DateTimeField(
        "Data/Horário",
        validators=[validar_data],
        null=True,
        blank=True
    )
    
    ciclo = models.CharField(
        "Ciclo",
        max_length=20,
        choices=CICLOS,
        default="unico",
    )

    class Meta:
        ordering = ["-data_hora"]
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"

    def clean(self):
        if not self.data_hora:
            raise ValidationError("Informe a data e/ou horário do evento.")

        if self.dia_inteiro:
            self.data_hora = self.data_hora.replace(
                hour=0, minute=0, second=0, microsecond=0
        )

    def __str__(self):
        return self.descricao

    def get_ciclo_display_label(self):
        return dict(CICLOS).get(self.ciclo, self.ciclo)