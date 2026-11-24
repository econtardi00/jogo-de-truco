import random

class Carta:
    VALORES = ['4', '5', '6', '7', 'Q', 'J', 'K', 'A', '2', '3']
    NAIPES = ['♦️', '♠️', '♥️', '♣️']
    
    def __init__(self, valor, naipe):
        self.valor = valor      
        self.naipe = naipe   

    def __repr__(self) -> str:
        return f'{self.valor} {self.naipe}'


class Baralho:
    def __init__(self):
        self.cartas = [Carta(v, n) for v in Carta.VALORES for n in Carta.NAIPES]

    def embaralhar(self):
        random.shuffle(self.cartas)

    def distribuir(self):
        mao_jogador = []

        for _ in range(3):
            carta_retirada = self.cartas.pop()
            mao_jogador.append(carta_retirada)

        return mao_jogador

    def virar_carta(self):
        vira = self.cartas.pop()

        return vira


class Jogador():
    def __init__(self):
        self.mao = []

    def receber_mao(self, cartas):
        self.mao = cartas

        return self.mao

    def jogar_carta(self, carta_escolhida):
        if not (1 <= carta_escolhida <= len(self.mao)):
            raise ValueError(f'Digite um índice de 1 a {len(self.mao)}')
        
        return self.mao.pop(carta_escolhida - 1) # Começar a lista pelo indice 1.


# ==========================================
# FUNÇÕES DE INTERFACE E EXECUÇÃO(em andamento)
# ==========================================


def exibir_mao(mao): 
    cartas_formatadas = [f"{i} - {carta}" for i, carta in enumerate(mao, start=1)]
    print('Sua mão:'," | ".join(cartas_formatadas))

def pedir_carta(jogador):
    ...

    
def main():
    j = Jogador()
    b = Baralho()

    b.embaralhar()
    cartas = b.distribuir()
    j.receber_mao(cartas)

    exibir_mao(j.mao)

if __name__ == '__main__':
    main()