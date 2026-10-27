from contabancaria import ContaBancaria

conta1 = ContaBancaria(numero = "123", titular = "Ana Lima")
conta2 = ContaBancaria(numero = "002", titular = "Décio Lima")
print(conta1)

conta1.depositar(100)
print(conta1.get_saldo())

conta1.sacar(40)
print(conta1.get_saldo())

conta2.depositar(200)
# após método transferir
conta2.transferir(173, conta1)
print(conta1.get_saldo())