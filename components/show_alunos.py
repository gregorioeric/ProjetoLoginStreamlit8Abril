import streamlit as st
from controllers.alunos_controllers import load_alunos

def show_alunos():
  st.subheader("Lista de Alunos Cadastrados!")

  alunos = load_alunos()

  if not alunos:
    return st.error("Nenhum Aluno Cadastrado. Clique no botão acima para cadatrar aluno.")
  
  tabs = st.tabs(["Alunos", "Pesquisar"])

  with tabs[0]:
    colunas = st.columns([3, 2, 3, 2, 2])

    colunas[0].subheader("Nome")
    colunas[1].subheader("Email")
    colunas[2].subheader("CPF")
    colunas[3].subheader("Visualizar")
    colunas[4].subheader("Deletar")