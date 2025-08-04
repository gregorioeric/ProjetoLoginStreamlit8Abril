import streamlit as st
import time
from controllers.load_usuarios import load_usuarios

st.title("Projeto Streamlit")

if "email" not in st.session_state:
  st.session_state.email = None

if "nome" not in st.session_state:
  st.session_state.nome = None

def login():
  usuarios = load_usuarios()

  email = st.text_input("Email", placeholder="Email")
  senha = st.text_input("Senha", placeholder="Senha", type="password")
  login = st.button("Login")

  if login:
    for user in usuarios:
      if user["email"] == email and user["senha"] == senha:
        st.session_state.email = user["email"]
        st.session_state.nome = user["nome"]
        st.success("login efetuado com sucesso!")
        time.sleep(3)
        st.rerun()
    else:
      st.error("Email e senha invalidos!")

def logout():
  if st.button("Logout"):
    st.session_state.clear()
    st.success("Finalizando o Sistema!")
    time.sleep(3)
    st.rerun()

@st.dialog("Formulário de Cadastro de Alunos")
def cadastrar_aluno():
  nome_aluno = st.text_input("Nome do Aluno", placeholder="Nome do Aluno")
  email_aluno = st.text_input("Email do Aluno", placeholder="Email do Aluno")
  cpf_aluno = st.text_input("CPF do Aluno", placeholder="CPF do Aluno")
  dataNasc_aluno = st.date_input("Data de Nascimento do Aluno")
  telefone_aluno = st.text_input("Telefone do Aluno", placeholder="Telefone do Aluno")

  btn_cadastrar = st.button("Cadastrar")

def main_page():
  tabs = st.tabs(["Dashboard", "Cadastro", "Logout"])
  nome = st.session_state.nome

  with tabs[0]:
    st.subheader("Dashboard")
    st.write(f"**Usuário Logado:** {nome}")

  with tabs[1]:
    st.subheader("Cadastro")
    if st.button("Abrir Formulário de Cadastro"):
      cadastrar_aluno()

  with tabs[2]:
    st.subheader("Logout")
    logout()

if st.session_state.email:
  main_page()
else:
  login()



# if st.session_state.email:
#   tabs = st.tabs(["Dashboard", "Cadastro", "Logout"])

#   with tabs[0]:
#     nome = st.session_state.nome
#     st.subheader("Dashboard")
#     st.write(nome)

#   with tabs[1]:
#     st.subheader("Cadastro")

#   with tabs[2]:
#     st.subheader("Logout")
# else:
# login()

# if "contador" not in st.session_state:
#   st.session_state.contador = 0

# if st.button("Adicionar"):
#   st.session_state.contador += 1

# if st.button("Diminuir"):
#   if st.session_state.contador > 0:
#     st.session_state.contador -= 1

st.write(st.session_state)



















# if "contador" not in st.session_state:
#   st.session_state.contador = 0


# # teste = ""

# # if not teste:
# #   st.error("A variavel está vazia")
# # else:
# #   st.success("A variavel tem informação.")

# if st.button("Somar"):
#   st.session_state.contador += 1


# if st.button("Diminuir"):
#   if st.session_state.contador > 0:
#     st.session_state.contador -= 1

# st.write(st.session_state.contador)