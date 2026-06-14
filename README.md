# Trabalho_Inicial_Bootcamp2-GerenciadordeEventos-
Desafio inicial do Bootcamp 2 - Aplicação para organização e controle da rotina diária
=======

## Integrantes:
João Henrique Freire de Souza (joao.fsouza@sempreceub.com) e Arthur Sant'Anna da Silveira (arthur.silveira@sempreceub.com)

# Gerenciador de Rotina

![CI](https://github.com/Arthur-Sant-Anna/Trabalho_Inicial_Bootcamp2-GerenciadordeEventos-/actions/workflows/ci.yml)

## Descrição do Problema

Muitas pessoas têm dificuldade em organizar sua rotina diária, lembrar compromissos importantes e manter consistência em atividades recorrentes. Isso pode gerar esquecimentos, atrasos e falta de produtividade no dia a dia.

## Proposta de Solução

Esta aplicação permite cadastrar e gerenciar eventos com diferentes ciclos (único, diário, semanal, mensal e anual), facilitando a organização pessoal e o acompanhamento de compromissos. Além disso, possibilita definir eventos de dia inteiro ou com horário específico.

## Público-alvo

- Estudantes
- Profissionais
- Pessoas que desejam melhorar a organização pessoal
- Qualquer usuário que precise gerenciar compromissos e rotinas

## Funcionalidades

- Listar eventos
- Adicionar eventos
- Editar eventos
- Excluir eventos
- Filtrar por ciclo
- Definir eventos como “dia inteiro”
- Definir eventos com data e horário

## Tecnologias Utilizadas

- Python 3.13
- Django 4.2
- SQLite
- pytest / pytest-django
- ruff
- GitHub Actions
- Bootstrap 5
- Banco de Dados Supabase

## Instalação

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio

# Crie e ative o ambiente virtual
python -m venv .venv
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Linux/Mac

# Instale as dependências
pip install -r requirements.txt

# Execute as migrações
python manage.py makemigrations
python manage.py migrate

# Execute a aplicação
python manage.py runserver
