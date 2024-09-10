def validar_cpf(cpf):
    """
    Valida se o CPF está no formato correto: 999.999.999-99.
    """
    if len(cpf) != 14:
        return False
    if cpf[3] != '.' or cpf[7] != '.' or cpf[11] != '-':
        return False
    return cpf[:3].isdigit() and cpf[4:7].isdigit() and cpf[8:11].isdigit() and cpf[12:].isdigit()

def calcular_soma_digitos(cpf):
    """
    Calcula a soma de todos os dígitos do CPF, ignorando os caracteres não numéricos.
    
    :param cpf: CPF no formato 999.999.999-99
    :return: Soma dos dígitos
    """
    soma = 0
    for char in cpf:
        if char.isdigit():
            soma += int(char)
    return soma

def verificar_par_ou_impar(numero):
    """
    Verifica se um número é par ou ímpar.
    
    :param numero: Número a ser verificado
    :return: "par" se o número for par, "ímpar" caso contrário
    """
    return "par" if numero % 2 == 0 else "ímpar"

def main():
    # Solicita ao usuário que insira o CPF
    cpf = input("Digite o CPF no formato 999.999.999-99: ")
    
    # Valida o formato do CPF
    if not validar_cpf(cpf):
        print("Formato de CPF inválido. Certifique-se de usar o formato 999.999.999-99.")
        return
    
    # Calcula a soma dos dígitos
    soma_digitos = calcular_soma_digitos(cpf)
    
    # Verifica se a soma dos dígitos é par ou ímpar
    tipo = verificar_par_ou_impar(soma_digitos)
    
    # Exibe o resultado para o usuário
    print(f"A soma dos dígitos do CPF é {soma_digitos}, que é {tipo}.")

if __name__ == "__main__":
    main()
