import streamlit as st

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