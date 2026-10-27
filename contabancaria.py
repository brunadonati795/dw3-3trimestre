class ContaBancaria:

    def __init__(self, numero, titular):

        if not numero or not str(numero).strip():
            raise ValueError("Número obrigatório.")

        if not titular or len(titular.strip()) < 3:
            raise ValueError(
                "Titular deve ter pelo menos 3 caracteres."
            )

        self.numero = str(numero).strip()
        self.titular = titular.strip()
        self.__saldo = 0.0

    def get_saldo(self):
        return self.__saldo


    def depositar(self, valor):

        if valor <= 0:
            raise ValueError(
                "O depósito deve ser positivo."
            )

        self.__saldo += valor


    def sacar(self, valor):

        if valor <= 0:
            raise ValueError(
                "O saque deve ser positivo."
            )

        if valor > self.__saldo:
            raise ValueError(
                "Saldo insuficiente."
            )

        self.__saldo -= valor
        
    def transferir(self, valor, destino):
        if destino is self:
            raise ValueError(
                "Não é possível transferir para mim"
            )
        if not isinstance(destino, ContaBancaria):
            raise ValueError(
                "Conta de destino inválida"
            )
            
        if valor <= 0.0: 
            raise ValueError("O valor deve ser positivo")
        
        if valor > self.__saldo:
            raise ValueError("saldo insuficiente")
        
        self.__saldo -= valor
        destino.__saldo += valor