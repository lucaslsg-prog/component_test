# Classe Principal para realizar operações no cadastro de instrutor
import re
from instrutor import Instrutor
class Instcontroller:

    def validar_email(self,email):
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if(re.search(regex,email)): 
            return True
        else:
            return False
       
    def salvar (self, nome, email, formacao,empresa,ativo):
        instrutor1 = Instrutor("João", "joao@test.com", "engenheiro de software", "teste",True)
        valid = True
        if (nome !="" and email !="" and formacao !=""):
        
            if self.validar_email(email)== True:
            
                if (email == instrutor1.email):
                    result = "e-mail duplicado"
                else:
                    instrutor2 = Instrutor(nome,email,formacao,empresa,True)
                    result = "Instrutor salvo com sucesso"
            
            else: 
                result = "E-mail inválido"
            
        else:
            result = "Os campos nome, e-mail e formação não podem ser vazios"

        print(result)
        return result
    
    def remover (self, nome):
        instrutor1 = Instrutor("João", "joao@test.com", "engenheiro de software", "teste",True)
        if (nome == instrutor1.nome):
            instrutor1.desativar()
            msg="instrutor removido com sucesso"
        else:
            msg="instrutor não encontrado"
        return msg

    def editar (self, nome, email, formacao,empresa,ativo):
        instrutor1 = Instrutor("João", "joao@test.com", "engenheiro de software", "teste",True)
        if (nome == instrutor1.nome):
            instrutor1.set_nome(nome)
            instrutor1.set_email(email)
            instrutor1.set_formacao(formacao)
            instrutor1.set_empresa(empresa)
            msg = "Dados do Instrutor"+instrutor1.nome+instrutor1.email+instrutor1.formacao+instrutor1.empresa
        else:
            msg="instrutor não encontrado"
        return msg

    def buscar (self, nome):
        instrutor1 = Instrutor("João", "joao@test.com", "engenheiro de software", "teste",True)
        if (nome == instrutor1.nome):
            nome = instrutor1.get_nome
            email = instrutor1.get_email
            #print ("Instrutor: ="+nome+ " "+email)
            msg = "Instrutor"+nome+email
        else:
            msg="instrutor não encontrado"
        return msg
