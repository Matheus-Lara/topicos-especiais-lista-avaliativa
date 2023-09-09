def imprimir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("-" * 14)

def ganhou_jogo(tabuleiro, jogador):
    for linha in tabuleiro:
        if all(casa == jogador for casa in linha):
            return True

    for coluna in range(4):
        if all(tabuleiro[linha][coluna] == jogador for linha in range(4)):
            return True

    if all(tabuleiro[i][i] == jogador for i in range(4)) or all(tabuleiro[i][3 - i] == jogador for i in range(4)):
        return True

    return False

def empatou(tabuleiro):
    return all(casa != " " for linha in tabuleiro for casa in linha)

def iniciar_jogo():
    tabuleiro = [[" " for _ in range(4)] for _ in range(4)]
    jogador = "O"

    while True:
        imprimir_tabuleiro(tabuleiro)
        linha = int(input(f"Jogador {jogador}, informe a linha (1-4): "))
        coluna = int(input(f"Jogador {jogador}, informe a coluna (1-4): "))

        linha = linha - 1
        coluna = coluna - 1

        if 0 <= linha <= 3 and 0 <= coluna <= 3 and tabuleiro[linha][coluna] == " ":
            tabuleiro[linha][coluna] = jogador

            if ganhou_jogo(tabuleiro, jogador):
                imprimir_tabuleiro(tabuleiro)
                print(f"Jogador {jogador} venceu!")
                break
            elif empatou(tabuleiro):
                imprimir_tabuleiro(tabuleiro)
                print("O jogo empatou!")
                break
            else:
                if jogador == "X":
                    jogador = "O"
                else:
                    jogador = "X"
        else:
            print("Esta casa não existe, informe uma válida")

if __name__ == "__main__":
    iniciar_jogo()
