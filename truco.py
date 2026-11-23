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

class Jogador:
    ...
        


if __name__ == '__main__':
    b = Baralho()
    print('Cartas no baralho:', len(b.cartas))   # tem que dar 40

    b.embaralhar()
    mao = b.distribuir()
    print(f'Mão:', *mao, sep='  | ')             # 3 cartas
    print('Cartas na mão:', len(mao))            # tem que dar 3
    print('Cartas no monte:', len(b.cartas))     # tem que dar 37