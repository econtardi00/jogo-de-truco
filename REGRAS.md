# 🃏 Regras do Truco Paulista

O **Truco Paulista** é um jogo de cartas disputado individualmente (1x1 contra o computador). 
O objetivo é ser o primeiro a atingir **12 pontos**.

---

## 1. Preparação e Baralho `(Funcionando)`
* **Baralho:** 40 cartas (baralho tradicional sem os `8`, `9`, `10` e `Curingas`).
* **Distribuição:** Cada jogador recebe **3 cartas** por rodada (mão).
* **O Vira:** Após a distribuição, 1 carta do monte é virada na mesa para definir as manilhas daquela rodada.

---

## 2. Hierarquia das Cartas **(A fazer)**
Da **mais forte** para a **mais fraca**:
`3 > 2 > A > K > J > Q > 7 > 6 > 5 > 4`

### Manilhas (Cartas mais fortes da rodada)
* **Definição:** São as 4 cartas do valor imediatamente superior ao **Vira** na ordem de força acima (ex: se o Vira for `7`, as manilhas são todos os `Q`; se o Vira for `3`, as manilhas são todos os `4`).
* **Desempate por Naipe:** `♣ Paus (Zap) > ♥ Copas > ♠ Espadas > ♦ Ouros`

---

## 3. Dinâmica da Rodada (Mão) **(A fazer)**
Cada rodada vale inicialmente **1 ponto** e é decidida em uma melhor de **3 vazas** (turnos).

* **Vencedor da Vaza:** Quem jogar a carta mais forte vence o turno e inicia o próximo.
* **Carta Encoberta:** A partir da 2ª vaza, o jogador pode descartar uma carta virada para baixo (sem valor) para blefar ou esconder o jogo.

### Critérios de Empate (Cangou / Melou)

| Situação | Regra de Desempate |
| :--- | :--- |
| **Empate na 1ª vaza** | Vence quem ganhar a 2ª vaza. Se empatar a 2ª, decide na 3ª. Se empatar todas, ninguém pontua. |
| **Empate na 2ª vaza** | Vence a rodada quem ganhou a 1ª vaza. |
| **Empate na 3ª vaza** | Vence a rodada quem ganhou a 1ª vaza. |

---

## 4. Sistema de Apostas **(A fazer)**
Na sua vez de jogar, qualquer jogador pode pedir **Truco** para aumentar o valor da rodada.

* **Escala:** `Normal (1 pt)` ➔ `Truco (3 pts)` ➔ `Seis (6 pts)` ➔ `Nove (9 pts)` ➔ `Doze (12 pts)`
* **Ações do Adversário:**
  * **Correr:** O jogador que pediu ganha os pontos atuais antes do aumento.
  * **Aceitar:** Valida o novo valor e o jogo continua.
  * **Aumentar:** Aceita e já eleva para o próximo nível da escala.
* **Restrição:** Um jogador não pode aumentar a própria aposta consecutivamente.

---

## 5. Regras de Reta Final (11 Pontos) **(A fazer)**
* **Mão de 11:** Quando apenas um jogador atinge 11 pontos, ele olha as próprias cartas antes de jogar para decidir se disputa a rodada (que passa a valer **3 pontos**) ou se corre (cedendo **1 ponto** ao adversário).
  * *Nota:* É proibido pedir truco na Mão de 11.
* **Mão de Ferro (`11 x 11`):** Quando ambos os jogadores empatam em 11 pontos, a rodada decisiva é jogada "no escuro" (nenhum jogador pode olhar suas próprias cartas).