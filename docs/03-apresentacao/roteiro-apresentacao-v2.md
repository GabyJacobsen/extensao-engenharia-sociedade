# Roteiro da Aula — Air Fryer Quebrada (1h30–2h)

## Bloco 0 — Abertura (5 min)

Equipe se apresenta como estudantes de Engenharia Mecatrônica do IFSC. Mostra a air fryer ligada na tomada, mas sem funcionar. Pergunta gancho: "quem topa o desafio de consertar isso de verdade, hoje, aqui?" Divide a turma em grupos (4-6 pessoas, conforme os 6-8 kits do orçamento).

## Bloco 1 — Conceitos elétricos fundamentais (20-25 min)

- Tensão, corrente, resistência — analogia da água no cano (pressão / vazão / estreitamento).
- Circuito fechado vs aberto — sem caminho completo, nada flui.
- Corrente contínua (DC) vs alternada (AC) — o que eles vão tocar (12V DC) vs o que nunca vão tocar (220V AC, na tomada).

Conexão com o mundo real (citar rápido, sem aprofundar): toda bateria é DC — celular, carro elétrico, pilha. A tomada de casa é AC. Todo carregador de celular tem, escondido dentro dele, um circuito que converte AC em DC — é por isso que ele esquenta e é "pesado" pro tamanho.

## Bloco 2 — Segurança elétrica (5-10 min)

- Regra de ouro: só encostam no lado de 12V.
- Por que a caixa de 220V fica fechada e isolada por um relé.

Conexão com o mundo real: painéis industriais de automação funcionam exatamente assim — um circuito de comando de baixa tensão (o que um operador humano toca) fica sempre separado do circuito de potência que move motores, fornos ou máquinas grandes. É uma regra de segurança que atravessa toda a engenharia elétrica.

## Bloco 3 — Ferramentas e componentes (15-20 min)

Apresentação prática (mão na massa, não slide) de cada peça do kit, sempre fechando com "onde isso aparece fora daqui":

| **Componente** | **O que é**                                                                                             | **Onde aparece no dia a dia**                                                                                                                   |
| -------------- | ------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| Protoboard     | Base pra montar circuito sem solda; fileiras internas conectadas                                        | É como todo circuito eletrônico começa antes de virar uma placa (PCB) definitiva — de um projeto de robótica até um produto que vai pra fábrica |
| ---            | ---                                                                                                     | ---                                                                                                                                             |
| Resistor       | Limita a corrente que passa                                                                             | Está em praticamente toda placa eletrônica que existe, protegendo outros componentes                                                            |
| ---            | ---                                                                                                     | ---                                                                                                                                             |
| LED            | Acende com polaridade certa                                                                             | Toda luz indicadora, telas de celular/TV, semáforos modernos, iluminação de casa                                                                |
| ---            | ---                                                                                                     | ---                                                                                                                                             |
| Interruptor    | Fica ligado ou desligado até ser acionado de novo (mantém o estado, diferente de um botão de campainha) | Interruptor de luz de parede, chave liga/desliga de aparelhos, disjuntores residenciais                                                         |
| ---            | ---                                                                                                     | ---                                                                                                                                             |
| Multímetro     | Mede tensão/continuidade                                                                                | Ferramenta de trabalho de eletricistas, técnicos de manutenção industrial e engenheiros — é o "estetoscópio" de quem mexe com eletrônica        |
| ---            | ---                                                                                                     | ---                                                                                                                                             |

## Bloco 4 — Desafio em grupos (35-40 min)

Entrega do Manual da Equipe de Manutenção e do kit com um defeito sorteado. Enquadramento: "engenharia é resolver problema com informação incompleta" — ninguém vai dizer o que está errado, o grupo precisa descobrir.

Monitores circulam entre os grupos, ajudando só com perguntas guiadas ("o que o multímetro está te dizendo?"), não entregando a resposta.

## Bloco 5 — Teste final e revelação do relé (15 min)

Cada grupo testa e vê a air fryer ligar. Só então é revelado o que estava por trás: o interruptor deles não liga a air fryer diretamente — ele aciona um relé de estado sólido, que funciona como uma chave controlada: um sinal pequeno (12V) liga ou desliga uma carga grande (220V) sem que os dois circuitos se toquem fisicamente.

Conexão com o mundo real: é assim que máquina de lavar, ar-condicionado e portão eletrônico ligam seus motores; é assim que um CLP (controlador industrial) liga uma máquina inteira numa fábrica; é a base de qualquer automação — inclusive a área de mecatrônica que a equipe estuda.

## Bloco 6 — Fechamento: carreira e roda de conversa (10-15 min)

Conversa aberta: o que é engenharia mecatrônica, como o que eles acabaram de fazer se conecta com robótica, automação industrial e produtos do dia a dia. Formulário curto de avaliação (interesse despertado, o que gostaram, o que não entenderam).