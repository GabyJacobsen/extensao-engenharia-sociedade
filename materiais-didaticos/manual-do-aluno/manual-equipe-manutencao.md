# Manual da Equipe de Manutenção — Operação Air Fryer

## Página 1 — Missão e Regra de Ouro

**Sua missão:** a air fryer da bancada está com defeito. O circuito de controle dela foi montado numa protoboard e algo está errado ou faltando. Sua equipe precisa diagnosticar o problema, consertar a montagem e testar — se acertar, ela liga de verdade.

**Regra de ouro (leia antes de tocar em qualquer coisa):** Vocês só encostam no lado de 12V (a protoboard). O lado da tomada (220V) já está fechado numa caixa e nunca deve ser aberto ou tocado. Se um monitor não autorizou, não mexe.

**Lembrete rápido — o que é o quê:**

- Tensão (V): a "pressão" que empurra a corrente elétrica.
- Corrente (A): o "fluxo" que passa pelo fio.
- Resistência (Ω): o quanto um componente dificulta essa passagem.
- Circuito fechado: caminho completo, sem interrupção, do positivo até o negativo. Se faltar um pedaço, nada funciona.

## Página 2 — Ferramentas e Componentes do Kit

**Protoboard:** por dentro, ela é dividida em fileiras curtas conectadas entre si. Encaixar dois componentes na mesma fileira é o mesmo que ligá-los com um fio. Encaixar na fileira errada = circuito não fecha (ou fecha errado).

**Componentes que vocês vão encontrar:**

| **Componente** | **O que verificar**                                                                                                                                                                       |
| -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Resistor       | Não tem polaridade (pode ir em qualquer direção), mas precisa estar na fileira certa                                                                                                      |
| ---            | ---                                                                                                                                                                                       |
| LED            | Tem polaridade! Perna mais longa = positivo. Invertido, não acende (mas também não queima nada)                                                                                           |
| ---            | ---                                                                                                                                                                                       |
| Interruptor    | Ao contrário de um botão de campainha, ele fica ligado ou desligado até ser acionado de novo — não precisa ficar segurando. Confira se os dois terminais usados estão nas fileiras certas |
| ---            | ---                                                                                                                                                                                       |
| Jumper (fio)   | Só faz a ponte entre duas fileiras. Confira início e fim                                                                                                                                  |
| ---            | ---                                                                                                                                                                                       |

**Multímetro — uso rápido:**

1. Selecione o modo de continuidade (símbolo de onda sonora) ou tensão DC conforme o monitor indicar.
2. Para continuidade: encoste as duas pontas nos dois pontos que quer testar. Apitou = está conectado.
3. Para tensão: ponta vermelha no positivo, preta no negativo (ou referência), leia o valor no visor.
4. Nunca meça continuidade num circuito energizado.

## Página 3 — Diagnóstico

**Método (siga nessa ordem):**

1. Observe a protoboard: compare com o esquema entregue. Falta algum componente? Algum está em fileira diferente da indicada?
2. Confira a polaridade do LED.
3. Use o multímetro em continuidade para testar se cada trecho do circuito está realmente fechado.
4. Corrija um problema por vez e reteste — não troque tudo de uma vez.
5. Quando o grupo achar que consertou, chame um monitor para autorizar o teste com a air fryer.

**Ficha de sintomas (marque o que você observa):**

| **Sintoma**                              | **Possível causa a investigar**                                    |
| ---------------------------------------- | ------------------------------------------------------------------ |
| Nada acontece, nenhum LED acende         | Circuito aberto — falta jumper ou componente fora da fileira       |
| ---                                      | ---                                                                |
| LED não acende, mas o resto parece certo | Confira a polaridade do LED                                        |
| ---                                      | ---                                                                |
| Interruptor não faz efeito nenhum        | Confira se os terminais do interruptor estão nas fileiras corretas |
| ---                                      | ---                                                                |
| Parece tudo certo mas não liga           | Peça ajuda de um monitor para medir tensão ponto a ponto           |
| ---                                      | ---                                                                |

**Registro do seu grupo:**

- Defeito identificado: \_**\_**\_**\_**\_**\_**\____
- Solução aplicada: \_**\_**\_**\_**\_**\_**\____
- Testado e aprovado por (monitor): \_**\_**\_**\_**\_**\_**\____