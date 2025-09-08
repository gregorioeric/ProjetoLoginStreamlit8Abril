import streamlit as st
from controllers.alunos_controllers import deletar_aluno
import time

@st.dialog("Deletar dados do Aluno")
def modal_deletar(id_aluno, nome_aluno):
  st.subheader(f"""
    Você deseja DELETAR o Aluno {nome_aluno}, se sim clique em Deletar se não clique em Cancelar!
  """)

  colunas = st.columns(2)

  with colunas[0]:
    btn_deletar = st.button("Deletar", use_container_width=True)
  
  with colunas[1]:
    btn_cancelar = st.button("Cancelar", use_container_width=True)

  if btn_deletar:
    result_deletar = deletar_aluno(id_aluno)
    
    if result_deletar:
      st.success("Aluno deletado com Sucesso!")
      st.session_state.result_pesquisa = None
      time.sleep(3)
      st.rerun()
    else:
      st.error("Não foi possivel deletar o Aluno!")

  if btn_cancelar:
    st.rerun()