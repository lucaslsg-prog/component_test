# Objeto Instrutor
class Instrutor:
    def __init__(self, nome, email, formacao, empresa, ativo):
        self.__nome = nome
        self.__email = email
        self.__formacao = formacao
        self.__empresa = empresa
        self.__ativo = ativo
        
    def desativar(self):
        self.__ativo = False
        print("A pessoa foi desativada com sucesso")
    
    def get_nome(self):
        return self.__nome

    def get_email(self):
        return self.__email
    
    def get_formacao(self):
        return self.__formacao
    
    def get_empresa(self):
        return self.__empresa
    
    def set_nome(self, nome):
        self.__nome = nome
    
    def set_email(self,email):
      self.__email = email
    
    def set_formacao(self, formacao):
      self.__formacao = formacao
    
    def set_empresa(self,empresa):
      self.__empresa = empresa

    @property
    def nome(self):
        return self.__nome
    
    @property
    def email(self):
        return self.__email
    
    @property
    def formacao(self):
        return self.__formacao
    
    @property
    def empresa(self):
        return self.__empresa
    
    @property
    def ativo(self):
        return self.__ativo
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @email.setter
    def email(self, email):
        self.__email = email

    @formacao.setter
    def formacao(self, formacao):
        self.__formacao = formacao
        
    @empresa.setter
    def empresa(self, empresa):
        self.__empresa = empresa

    @ativo.setter
    def ativo(self, ativo):
        self.__ativo = ativo