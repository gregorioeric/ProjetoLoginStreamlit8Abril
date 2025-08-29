import streamlit as st

@st.dialog("Deletar dados do Aluno")
def modal_deletar(id_aluno):
  st.write(id_aluno)