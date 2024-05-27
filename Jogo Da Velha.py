class Jogo:
    def __init__(self):
        self.tabuleiro = [["1", "2", "3"],
                          ["4", "5", "6"],
                          ["7", "8", "9"]]
        self.turno = 0

    def print_tabuleiro(self):
        for row in self.tabuleiro:
            print(" | ".join(row))
            print("-" * 5)

    def verificar_vencedor(self):
        combinacoes_vencedoras = [
            # Linhas
            [self.tabuleiro[0][0], self.tabuleiro[0][1], self.tabuleiro[0][2]],
            [self.tabuleiro[1][0], self.tabuleiro[1][1], self.tabuleiro[1][2]],
            [self.tabuleiro[2][0], self.tabuleiro[2][1], self.tabuleiro[2][2]],
            # Colunas
            [self.tabuleiro[0][0], self.tabuleiro[1][0], self.tabuleiro[2][0]],
            [self.tabuleiro[0][1], self.tabuleiro[1][1], self.tabuleiro[2][1]],
            [self.tabuleiro[0][2], self.tabuleiro[1][2], self.tabuleiro[2][2]],
            # Diagonais
            [self.tabuleiro[0][0], self.tabuleiro[1][1], self.tabuleiro[2][2]],
            [self.tabuleiro[0][2], self.tabuleiro[1][1], self.tabuleiro[2][0]],
        ]

        for combinacao in combinacoes_vencedoras:
            if combinacao[0] == combinacao[1] == combinacao[2]:
                return True
        return False

    def jogar(self):
        jogador_atual = "X"

        while True:
            self.print_tabuleiro()
            print(f"Jogador {jogador_atual}, escolha a posição (1-9):")
            escolha = input()

            if not escolha.isdigit() or not 1 <= int(escolha) <= 9:
                print("Escolha inválida. Tente novamente.")
                continue

            escolha = int(escolha) - 1
            linha, coluna = divmod(escolha, 3)

            if self.tabuleiro[linha][coluna] in ["X", "O"]:
                print("Posição já ocupada. Tente novamente.")
                continue

            self.tabuleiro[linha][coluna] = jogador_atual

            if self.verificar_vencedor():
                self.print_tabuleiro()
                print(f"Parabéns, jogador {jogador_atual}! Você venceu!")
                break

            if all(cell in ["X", "O"] for row in self.tabuleiro for cell in row):
                self.print_tabuleiro()
                print("O jogo empatou!")
                break

            jogador_atual = "O" if jogador_atual == "X" else "X"


if __name__ == "__main__":
    jogo = Jogo()
    jogo.jogar()
