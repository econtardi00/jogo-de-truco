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

if __name__ == '__main__':
    b = Baralho()
    print(len(b.cartas))  
    print(*b.cartas[:4], sep=' , ')   