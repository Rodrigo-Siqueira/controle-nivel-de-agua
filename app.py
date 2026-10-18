from colorama import Fore, Style, init

init(autoreset=False)

# Níveis do reservatório
mensagens_reservatorio = [
    'MUITO BAIXO (CRÍTICO) - Reabasteça imediatamente!',
    'BAIXO - Atenção ao nível do reservatório.',
    'MÉDIO - Nível adequado.',
    'ALTO - Nível elevado, monitore o reservatório.',
    'MUITO ALTO (ALERTA) - Risco de transbordamento!'
]

# Simulação de leituras do reservatório
leituras_simuladas = [1, 2, 3, 4, 5]


# Define a cor da mensagem conforme o nível informado
def definir_cor(nivel):
    if nivel == 1:
        return Fore.RED
    elif nivel == 2:
        return Fore.YELLOW
    elif nivel == 3:
        return Fore.GREEN
    elif nivel == 4:
        return Fore.CYAN
    elif nivel == 5:
        return Fore.BLUE
    else:
        return Fore.WHITE


# Painel
print('*' * 60)
print("Monitoramento do Reservatório de Água".upper())
print('*' * 60)

# Exibe a situação de cada leitura com a cor correspondente
for nivel in leituras_simuladas:
    cor = definir_cor(nivel)
    mensagem = mensagens_reservatorio[nivel - 1]

    print(f"{cor}Nível {nivel}: {mensagem}{Style.RESET_ALL}")

print('*' * 60)

# Restaura o estilo padrão do terminal
print(Style.RESET_ALL, end='')
