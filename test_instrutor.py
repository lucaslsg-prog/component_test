#Testes da classe Instcontroller

from instcontroller import Instcontroller

new_inst = Instcontroller()

########## TESTES DO METODO salvar instrutor ################################
def test_salvar_inst_success():
    success_msg = "Instrutor salvo com sucesso"
    resultado = new_inst.salvar("Maria","maria@test.com","analista de sistemas","teste", True)
    assert(resultado==success_msg)

def test_salvar_inst_email_sem_arroba():
    success_msg = "E-mail inválido"
    resultado = new_inst.salvar("Maria","maritest.com","analista de sistemas","teste", True)
    assert(resultado==success_msg)

def test_salvar_inst_email_sem_pontocom():
    success_msg = "E-mail inválido"
    resultado = new_inst.salvar("Maria","mari@test","analista de sistemas","teste", True)
    assert(resultado==success_msg)

def test_salvar_inst_email_sem_ponto():
    success_msg = "E-mail inválido"
    resultado = new_inst.salvar("Maria","mari@testcom","analista de sistemas","teste", True)
    assert(resultado==success_msg)

def test_salvar_inst_email_maiusculo():
    success_msg = "E-mail inválido"
    resultado = new_inst.salvar("Maria","MARI@test.com","analista de sistemas","teste", True)
    assert(resultado==success_msg)

def test_salvar_inst_email_comespaco():
    success_msg = "E-mail inválido"
    resultado = new_inst.salvar("Maria","ma ri@test.com","analista de sistemas","teste", True)
    assert(resultado==success_msg)

def test_salvar_inst_sem_nome():
    success_msg = "Os campos nome, e-mail e formação não podem ser vazios"
    resultado = new_inst.salvar("", "qa@test.com", "eng", "teste",True)
    assert(resultado==success_msg)

def test_salvar_inst_sem_email():
    success_msg = "Os campos nome, e-mail e formação não podem ser vazios"
    resultado = new_inst.salvar("lucas", "", "eng", "teste",True)
    assert(resultado==success_msg)

def test_salvar_inst_sem_formacao():
    success_msg = "Os campos nome, e-mail e formação não podem ser vazios"
    resultado = new_inst.salvar("thiago", "qa@test.com", "", "motorola",True)
    assert(resultado==success_msg)

def test_salvar_inst_sem_parametros():
    success_msg = "Os campos nome, e-mail e formação não podem ser vazios"
    resultado = new_inst.salvar("", "", "", "",True)
    assert(resultado==success_msg)

def test_salvar_inst_duplicado():
    success_msg = "e-mail duplicado"
    resultado = new_inst.salvar("João", "joao@test.com", "eng", "fit",True)
    assert(resultado==success_msg)



########## TESTES DO METODO remover instrutor ################################
def test_remove_inst():
  msg = "instrutor removido com sucesso"
  resultado = new_inst.remover("João")
  assert(resultado==msg)

def test_remove_inst_nao_encontrado():
    success_msg = "instrutor não encontrado"
    resultado = new_inst.remover("lucas")
    assert(resultado==success_msg)


########## TESTES DO METODO editar instrutor ################################
def test_edit_inst_success():
    success_msg = "Dados do InstrutorJoãojoao@test.comengenheiro de softwareteste"
    resultado = new_inst.editar("João", "joao@test.com", "engenheiro de software", "teste",True)
    assert(resultado==success_msg)

def test_edit_inst_nao_encontrado():
    success_msg = "instrutor não encontrado"
    resultado = new_inst.editar("Lucas", "joao@test.com", "engenheiro de software", "teste",True)
    assert(resultado==success_msg)


########## TESTES DO METODO buscar instrutor ################################
# def test_busca_inst_success():
#     success_msg = "InstrutorJoãojoao@test.com"
#     resultado = new_inst.buscar("João")
#     assert(resultado==success_msg)

def test_busca_inst_nao_encontrado():
    success_msg = "instrutor não encontrado"
    resultado = new_inst.buscar("Lucas")
    assert(resultado==success_msg)