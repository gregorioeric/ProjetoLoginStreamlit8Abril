import streamlit as st

@st.dialog("Visualizar Dados do Aluno", width="large")
def visualizar_aluno(aluno):
  colunas = st.columns([2, 3])

  with colunas[0]:
    st.caption("Nome")
    st.subheader("Email")
    st.subheader("Data de Nascimento")
    st.subheader("CPF")
    st.subheader("Telefone")

  with colunas[1]:
    st.subheader(aluno["nome_aluno"])
    st.subheader(aluno["email_aluno"])
    st.subheader(aluno["dataNasc_aluno"])
    st.subheader(aluno["cpf_aluno"])
    st.subheader(aluno["telefone_aluno"])

  colunas_btn = st.columns(2)

  with colunas_btn[0]:
    editar = st.button("Editar", use_container_width=True)

  with colunas_btn[1]:
    cancelar = st.button("Cancelar", use_container_width=True)

  if editar:
    st.session_state.modal_editar = True
    st.session_state.id_aluno = aluno["id_aluno"]
    st.rerun()

  if cancelar:
    st.rerun()