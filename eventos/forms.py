from django import forms

from .models import Eventos


class EventoForm(forms.ModelForm):

    class Meta:
        model = Eventos
        fields = ["descricao", "ciclo", "dia_inteiro", "data_hora"]

        widgets = {
            "descricao": forms.TextInput(
                attrs={"class": "form-control"}
            ),
            "ciclo": forms.Select(attrs={"class": "form-select"}),

            "dia_inteiro": forms.CheckboxInput(
                attrs={"class": "form-check-input", "id": "diaInteiroCheck"}
            ),

            "data_hora": forms.DateTimeInput(
                attrs={"class": "form-control", "type": "datetime-local", "id": "dataHora"}
            ),
        }
    def clean_descricao(self):
        descricao = self.cleaned_data.get("descricao", "").strip()
        if not descricao:
            raise forms.ValidationError("A descrição não pode estar vazia.")
        return descricao
    
    def clean(self):
        cleaned_data = super().clean()

        data_hora = cleaned_data.get("data_hora")
        dia_inteiro = cleaned_data.get("dia_inteiro")

        if not data_hora:
            raise forms.ValidationError("Informe a data e/ou horário do evento.")

        if dia_inteiro:
            cleaned_data["data_hora"] = data_hora.replace(
                hour=0, minute=0, second=0, microsecond=0
            )

        return cleaned_data