# Função validarCPF 

def validarCPF(cpf):
    
    #Valida se tem caracter (. ou -) 
    if len(cpf) == 14:
        cpf = cpf.replace(".", "").replace("-", "")
    
    #Valida se CPF tem 11 digitos e se é números iguais (inválidos)
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False
    
    #Verifica primeiro digito
    soma_num_cpf = 0 

    for i in range(0,9):
        soma_num_cpf += int(cpf[i]) * (10 - i)

    resto_one = (soma_num_cpf * 10) % 11
    if resto_one == 10:
        resto_one = 0

    if resto_one != int(cpf[9]):
        return False
    
    #Verifica segundo digito
    soma_num_cpf = 0

    for i in range(0,10):
        soma_num_cpf += int(cpf[i]) * (11 - i)
    
    resto_two = (soma_num_cpf * 10) % 11
    if resto_two == 10:
        resto_two = 0

    if resto_two != int(cpf[10]):
        return False    
        
    return True

# Pede CPF do Usuário e valida a Função Validadar CPF
print("VALIDADOR CPF")
print()
cpf = input("DIGITE O SEU CPF (000.000.000-00): ")

if validarCPF(cpf) == True:
    print(f"CPF: {cpf} É VÁLIDO!")
else:
    print(f"CPF: {cpf} NÃO É VÁLIDO!")
