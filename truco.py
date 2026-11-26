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

    def jogar_carta(self, carta_escolhida):
        if not (1 <= carta_escolhida <= len(self.mao)):
            raise IndexError(f'Digite um índice de 1 a {len(self.mao)}')
        
        return self.mao.pop(carta_escolhida - 1)

class Bot(Jogador):
    def jogar_carta(self, carta_escolhida=None):
        indice_aleatorio = random.randrange(len(self.mao))
        return self.mao.pop(indice_aleatorio)


# ==========================================
# FUNÇÕES DE INTERFACE E EXECUÇÃO
# ==========================================


def exibir_mao(mao):
    cartas_formatadas = [f"{i} - {carta}" for i, carta in enumerate(mao, start=1)]
    print('Sua mão:'," | ".join(cartas_formatadas))

def pedir_carta_usuario(jogador):
    while True:
        exibir_mao(jogador.mao)
        try:
            escolha = int(input('Digite o índice da carta para jogar: '))
            carta_escolhida = jogador.jogar_carta(escolha)
            break

        except ValueError:
            print('Entrada inválida! Digite apenas números inteiros.\n')
        except IndexError as erro:
            print(f'{erro}\n')

    return carta_escolhida

def iniciar_jogo():
    jogador = Jogador()
    baralho = Baralho()
    bot = Bot()
    baralho.embaralhar()


    jogador.receber_mao(baralho.distribuir())
    bot.receber_mao(baralho.distribuir())

    vira = baralho.virar_carta()
    print(f'Vira: {vira}\n')


    while jogador.mao:
        carta_jogador = pedir_carta_usuario(jogador)      
        print(f'Você jogou: {carta_jogador}. \n')

        carta_bot = bot.jogar_carta()
        print(f'O oponente jogou: {carta_bot}\n')

    print('Fim da mão!')


if __name__ == '__main__':
    iniciar_jogo()