# 💧 Controle de Níveis de Água

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)
![Status](https://img.shields.io/badge/Status-Concluído-success?style=for-the-badge)

## 🎯 Objetivo do Sistema
Este projeto é um **Sistema de Monitoramento de Reservatório de Água** desenvolvido para simular, no terminal, o acompanhamento do nível de um reservatório. O programa exibe mensagens de alerta com **cores diferentes** conforme o nível de água, seguindo a progressão de risco, do nível crítico ao nível de alerta máximo.

## 💻 Linguagem Utilizada
- **Python 3**
- Biblioteca **colorama** (cores no terminal)

## 📊 Regras de Negócio
O sistema trabalha com cinco níveis, armazenados em uma lista, cada um associado a uma mensagem e a uma cor:

| Nível | Situação | Cor |
|-------|----------|-----|
| 1 | Muito baixo (crítico) | 🔴 Vermelho |
| 2 | Baixo | 🟡 Amarelo |
| 3 | Médio | 🟢 Verde |
| 4 | Alto | 🔵 Ciano |
| 5 | Muito alto (alerta) | 🔵 Azul |

- A função `definir_cor(nivel)` retorna a cor correspondente ao nível informado.
- Para um nível inválido, a mensagem é exibida em **branco**.
- Após cada mensagem, o estilo padrão do terminal é restaurado com `Style.RESET_ALL`.

## 🧮 Lógica Utilizada
1. **Mensagem do nível:** `mensagens_reservatorio[nivel - 1]` (a lista começa no índice 0, e os níveis, no 1)
2. **Cor do nível:** `definir_cor(nivel)`
3. **Exibição:** `print(f"{cor}Nível {nivel}: {mensagem}{Style.RESET_ALL}")`

## 🚀 Como executar o programa

1. Certifique-se de ter o Python instalado em sua máquina.
2. Clone este repositório ou faça o download dos arquivos.
3. Abra o terminal e navegue até a pasta do projeto.
4. Instale a biblioteca colorama: `pip install colorama`
5. Execute o arquivo principal: `python app.py`

> A simulação usa valores definidos no código (`leituras_simuladas`), então não é necessário digitar nenhum dado.
