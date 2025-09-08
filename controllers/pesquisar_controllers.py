from controllers.alunos_controllers import load_alunos

def pesquisar(aluno_pesquisar):
  alunos = load_alunos()
  pesquisar = aluno_pesquisar.lower()

  alunos_encontrados = []

  for aluno in alunos:
    nome_aluno = aluno["nome_aluno"].lower()
    email_aluno = aluno["email_aluno"].lower()

    if pesquisar in nome_aluno or pesquisar in email_aluno or pesquisar in aluno["cpf_aluno"]:
      alunos_encontrados.append(aluno)
  
  return alunos_encontrados