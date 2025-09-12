import streamlit as st
from controllers.alunos_controllers import load_alunos
from utils.cpf_utils import cpf_utils
from components.modal_visualizar import visualizar_aluno
from components.modal_deletar import modal_deletar
from controllers.pesquisar_controllers import pesquisar

def show_alunos():
  st.subheader("Lista de Alunos Cadastrados!")

  alunos = load_alunos()

  if not alunos:
    return st.error("Nenhum Aluno Cadastrado. Clique no botão acima para cadatrar aluno.")
  
  tabs = st.tabs(["Alunos", "Pesquisar"])

  with tabs[0]:
    colunas = st.columns([3, 3, 2, 2, 2])

    colunas[0].subheader("Nome")
    colunas[1].subheader("Email")
    colunas[2].subheader("CPF")
    colunas[3].subheader("Visualizar")
    colunas[4].subheader("Deletar")
  
    for aluno in alunos:
      colunas_aluno = st.columns([3, 3, 2, 2, 2])

      cpf_formatado = cpf_utils(aluno["cpf_aluno"])

      colunas_aluno[0].write(aluno["nome_aluno"])
      colunas_aluno[1].write(aluno["email_aluno"])
      colunas_aluno[2].write(cpf_formatado)

      if colunas_aluno[3].button("Visualizar", key=f"view_{aluno['id_aluno']}", use_container_width=True):
        visualizar_aluno(aluno)

      if colunas_aluno[4].button("Deletar", key=f"deletar_{aluno["id_aluno"]}", use_container_width=True):
        modal_deletar(aluno["id_aluno"], aluno["nome_aluno"])

  with tabs[1]:
    st.subheader("Pesquisar alunos")
    
    with st.form("from_pesquisar", clear_on_submit=True):
      pesquisar_aluno = st.text_input("Pesquisar Aluno", placeholder="Pesquisar Aluno")

      colunas_pesquisar = st.columns(2)

      with colunas_pesquisar[0]:
        btn_pesquisar = st.form_submit_button("Pesquisar", use_container_width=True)
      
      with colunas_pesquisar[1]:
        btn_limpar = st.form_submit_button("Limpar Pesquisa", use_container_width=True)
      
      if btn_pesquisar:
        if not pesquisar_aluno:
          return st.warning("Campo pesquisa está vazio, preencha um Nome ou email do aluno para localizar os dados!")
        st.session_state.result_pesquisa = None

        result_pesquisa = pesquisar(pesquisar_aluno)

        if not result_pesquisa:
          return st.info(f"Nenhum aluno foi encontrado com o nome {pesquisar_aluno}")

        st.session_state.result_pesquisa = result_pesquisa

      if btn_limpar:
        st.session_state.result_pesquisa = None
        st.rerun()
    
    get_pesquisa = st.session_state.result_pesquisa

    if get_pesquisa:
      colunas_resultado_header = st.columns([3, 3, 2, 2, 2])

      colunas_resultado_header[0].subheader("Nome")
      colunas_resultado_header[1].subheader("Email")
      colunas_resultado_header[2].subheader("CPF")
      colunas_resultado_header[3].subheader("Visualizar")
      colunas_resultado_header[4].subheader("Deletar")

      for alunos_encontrados in get_pesquisa:
        colunas_resultado = st.columns([3, 3, 2, 2, 2])

        cpf_formatado = cpf_utils(alunos_encontrados["cpf_aluno"])

        colunas_resultado[0].write(alunos_encontrados["nome_aluno"])
        colunas_resultado[1].write(alunos_encontrados["email_aluno"])
        colunas_resultado[2].write(cpf_formatado)

        if colunas_resultado[3].button("Visualizar", key=f"view_pesquisa_{alunos_encontrados['id_aluno']}", use_container_width=True):
          visualizar_aluno(alunos_encontrados)

        if colunas_resultado[4].button("Deletar", key=f"deletar_pesquisa_{alunos_encontrados["id_aluno"]}", use_container_width=True):
          modal_deletar(alunos_encontrados["id_aluno"], alunos_encontrados["nome_aluno"])