import streamlit as st
import re
from utils.validar_email import validar_email
from datetime import date

@st.dialog("Formulário de Cadastro de Alunos", width="large")
def cadastrar_aluno():
  data_minima = date(1900, 1, 1)
  data_maxima = date.today()

  with st.form("Fomulario de Cadastro"):
    nome_aluno = st.text_input("Nome do Aluno", placeholder="Nome do Aluno")
    email_aluno = st.text_input("Email do Aluno", placeholder="Email do Aluno")
    cpf_aluno = st.text_input(
      "CPF do Aluno",
      placeholder="CPF do Aluno",
      max_chars=11
    )
    dataNasc_aluno = st.date_input(
      "Data de Nascimento do Aluno",
      value=data_maxima,
      min_value=data_minima,
      max_value=data_maxima
    )
    telefone_aluno = st.text_input(
      "Telefone do Aluno",
      placeholder="Telefone do Aluno",
      max_chars=11
    )

    cpf_aluno_numeros = re.sub(r"\D", "", cpf_aluno)
    telefone_aluno_numeros = re.sub(r"\D", "", telefone_aluno)
    email_isvalid = validar_email(email_aluno)

    colunas = st.columns(2)

    with colunas[0]:
      btn_cadastrar = st.form_submit_button("Cadastrar", use_container_width=True)
    
    with colunas[1]:
      btn_cancelar = st.form_submit_button("Cancelar", use_container_width=True)

  if btn_cadastrar:
    st.write(email_isvalid)

  if btn_cancelar:
    st.rerun()
