import streamlit as st
from utils.validar_email import validar_email
import re

@st.dialog("Editar dados do Aluno")
def modal_editar(id_aluno):
  st.write(id_aluno)

  with st.form("form_editar"):
    nome_aluno = st.text_input("Nome do Aluno", placeholder="Nome do Aluno")
    email_aluno = st.text_input("Email do Aluno", placeholder="Email do Aluno")
    cpf_aluno = st.text_input(
      "CPF do Aluno",
      placeholder="CPF do Aluno",
      max_chars=11
    )
    dataNasc_aluno = st.date_input(
      "Data de Nascimento do Aluno"
    )
    telefone_aluno = st.text_input(
      "Telefone do Aluno",
      placeholder="Telefone do Aluno",
      max_chars=11
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
    pass

  if btn_cancelar:
    st.session_state.modal_editar = False
    st.session_state.id_aluno = 0
    st.rerun()