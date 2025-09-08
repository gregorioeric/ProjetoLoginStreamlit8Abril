# importando a biblioteca streamlit e criando um apelido st para facilitar na digitação.
import streamlit as st

# da pasta utils selecionar o arquivo validar_email e importar a função validar_email
from utils.validar_email import validar_email

# importando a função re do proprio python, regular expression
import re

# importando a função time do proprio python
import time

# da pasta controllers selecionar o arquivo alunos_controllers e importar as funções:
# select_aluno_by_id, update_aluno, select_aluno_por_email, select_aluno_por_cpf
from controllers.alunos_controllers import select_aluno_by_id, update_aluno, select_aluno_por_email, select_aluno_por_cpf

# da pasta utils selecionar o arquivo validar_email e importar a função validar_email
from datetime import date, datetime

# st.dialog cria uma janela com janela que irá mostrar as informações 
@st.dialog("Editar dados do Aluno", width="large")
def modal_editar(id_aluno):
  result_by_id = select_aluno_by_id(id_aluno)

  with st.form("form_editar"):
    data_minima = date(1900, 1, 1)
    data_maxima = date.today()
    alunoDN = datetime.strptime(result_by_id["dataNasc_aluno"], "%Y-%m-%d").date()

    nome_aluno = st.text_input(
      "Nome do Aluno",
      placeholder="Nome do Aluno",
      value=result_by_id["nome_aluno"]
    )
    email_aluno = st.text_input(
      "Email do Aluno",
      placeholder="Email do Aluno",
      value=result_by_id["email_aluno"]
    )
    cpf_aluno = st.text_input(
      "CPF do Aluno",
      placeholder="CPF do Aluno",
      max_chars=11,
      value=result_by_id["cpf_aluno"]
    )
    dataNasc_aluno = st.date_input(
      "Data de Nascimento do Aluno",
      value=alunoDN,
      min_value=data_minima,
      max_value=data_maxima
    )
    telefone_aluno = st.text_input(
      "Telefone do Aluno",
      placeholder="Telefone do Aluno",
      max_chars=11,
      value=result_by_id["telefone_aluno"]
    )

    cpf_aluno_numeros = re.sub(r"\D", "", cpf_aluno)
    telefone_aluno_numeros = re.sub(r"\D", "", telefone_aluno)
    email_isvalid = validar_email(email_aluno)

    result_by_email = select_aluno_por_email(email_aluno)
    result_by_cpf = select_aluno_por_cpf(cpf_aluno_numeros)

    colunas_btn = st.columns(2)

    with colunas_btn[0]:
      btn_atualizar = st.form_submit_button("Atualizar", use_container_width=True)

    with colunas_btn[1]:
      btn_cancelar = st.form_submit_button("Cancelar", use_container_width=True)
  
  if btn_atualizar:
    if not nome_aluno:
      return st.error("Campo Nome não pode ser vazio!")
    
    if not email_aluno:
      return st.warning("Campo Email não pode ser vazio")
    
    if not email_isvalid:
      return st.warning("Email invalido!")
    
    if not cpf_aluno:
      return st.warning("Campo CPF não pode ser vazio!")
    
    # funcão len() => conta a quantidade de itens de uma lista ou string
    if len(cpf_aluno_numeros) != 11 or len(cpf_aluno_numeros) < 11:
      return st.warning("CPF invalido")

    if not telefone_aluno:
      return st.warning("Campo Telefone não pode ser vazio!")
    
    # funcão len() => conta a quantidade de itens de uma lista ou string
    if len(telefone_aluno_numeros) != 11 or len(telefone_aluno_numeros) < 11:
      return st.warning("Telefone invalido")

    if result_by_email:
      if result_by_id["email_aluno"] == email_aluno:
        email_aluno = result_by_id["email_aluno"]
      else:
        return st.error("Email está cadastrado com outro aluno!")

    if result_by_cpf:
      if result_by_id["cpf_aluno"] == cpf_aluno:
        cpf_aluno = result_by_id["cpf_aluno"]
      else:
        return st.error("CPF está cadastrado com outro aluno!")

    data_aluno = {
      "nome_aluno": nome_aluno,
      "email_aluno": email_aluno,
      "cpf_aluno": cpf_aluno,
      "dataNasc_aluno": dataNasc_aluno.strftime("%Y-%m-%d"),
      "telefone_aluno": telefone_aluno,
    }

    result_update = update_aluno(result_by_id["id_aluno"], data_aluno)

    if result_update:
      st.success("Dados do Aluno Atualizado com sucesso!")
      st.session_state.modal_editar = False
      st.session_state.id_aluno = 0
      time.sleep(3)
      st.rerun()

  if btn_cancelar:
    st.session_state.modal_editar = False
    st.session_state.id_aluno = 0
    st.rerun()