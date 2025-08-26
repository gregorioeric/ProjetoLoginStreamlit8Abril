import streamlit as st
from utils.validar_email import validar_email
import re
from controllers.alunos_controllers import select_aluno_by_id

@st.dialog("Editar dados do Aluno")
def modal_editar(id_aluno):
  result_by_id = select_aluno_by_id(id_aluno)

  with st.form("form_editar"):
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
      "Data de Nascimento do Aluno"
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

    colunas_btn = st.columns(2)

    with colunas_btn[0]:
      btn_atualizar = st.form_submit_button("Atualizar")

    with colunas_btn[1]:
      btn_cancelar = st.form_submit_button("Cancelar")
  
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

  if btn_cancelar:
    st.session_state.modal_editar = False
    st.session_state.id_aluno = 0
    st.rerun()