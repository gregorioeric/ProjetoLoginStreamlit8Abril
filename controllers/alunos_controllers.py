import json
import os

ALUNOS = "data/alunos.json"

def load_alunos():
  if os.path.exists(ALUNOS):
    with open(ALUNOS, "r", encoding="utf-8") as arq_json:
      return json.load(arq_json)
  else:
    return []

def select_aluno_by_id(id_aluno):
  alunos = load_alunos()

  for aluno in alunos:
    if aluno["id_aluno"] == id_aluno:
      return aluno
  return False
  













# def select_aluno_by_id(id_aluno):
#   alunos = load_alunos()

#   for aluno in alunos:
#     if aluno["id_aluno"] == id_aluno:
#       return aluno
#   return False

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
  
def insert_aluno(data_aluno):
  alunos = load_alunos()

  if not isinstance(data_aluno, dict) or not data_aluno:
    return False
  
  alunos.append(data_aluno)

  with open(ALUNOS, "w", encoding="utf-8") as arq_json:
    json.dump(alunos, arq_json, indent=4, ensure_ascii=False)
  return True
























# def update_aluno_by_id(id, update_aluno):
#   alunos = load_alunos()

#   for aluno in alunos:
#     if aluno["id_aluno"] == id:
#       aluno["nome_aluno"] = update_aluno["nome_aluno"]
#       return alunos
#   return False