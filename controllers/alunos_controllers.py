import json
import os

ALUNOS = "data/alunos.json"

def load_alunos():
  if os.path.exists(ALUNOS):
    with open(ALUNOS, "r", encoding="utf-8") as arq_json:
      return json.load(arq_json)
  else:
    return []
  
def select_todos_alunos():
  alunos = load_alunos()

  for aluno in alunos:
    return aluno

def select_aluno_por_email(email):
  alunos = load_alunos()

  for aluno in alunos:
    if aluno["email_aluno"] == email:
      return True
  else:
    return False
  
def select_aluno_por_cpf(cpf):
  alunos = load_alunos()

  for aluno in alunos:
    if aluno["cpf_aluno"] == cpf:
      return True
  else:
    return False