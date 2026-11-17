# Roteiro da Aula — Air Fryer Quebrada (1h30–2h)

## Bloco 0 — Abertura (5 min)

Equipe se apresenta como estudantes de Engenharia Mecatrônica do IFSC. Mostra a air fryer ligada na tomada, mas sem funcionar. Pergunta gancho: "quem topa o desafio de consertar isso de verdade, hoje, aqui?" Divide a turma em grupos (4-6 pessoas, conforme os 6-8 kits do orçamento).

## Bloco 1 — Conceitos elétricos fundamentais (20-25 min)

- **A Analogia da Água no Cano (Modelo Hidráulico):**
  - **Tensão ($V$ / Volts):** É a **pressão** da água — a força da caixa d'água empurrando o fluxo pela tubulação.
  - **Corrente ($I$ / Amperes):** É a **vazão** — o quantidade de água (elétrons) que atravessa o cano a cada segundo.
  - **Resistência ($R$ / Ohms):** É o **estreitamento** ou o registro/torneira — um obstáculo físico que estrangula o cano, diminuindo a vazão para proteger os componentes seguintes contra excesso de fluxo.
  - **Circuito Fechado vs. Aberto:** Se o cano for quebrado ou a tubulação interrompida, a água para de circular imediatamente. A eletricidade exige um caminho contínuo de ida e volta à fonte; sem malha fechada, corrente é zero.

> 💡 **Dica:** Projete o **Slide 3 da [`03-apresentacao/apresentacao-alunos-fios-e-fritas.html`](../03-apresentacao/apresentacao-alunos-fios-e-fritas.html)** (*"Eletricidade é Igual à Água no Cano!"*) que conta com um simulador visual interativo onde você pode clicar em *"Fluxo Livre"*, *"Cano Apertado (Resistor)"* e *"Cano Quebrado (Circuito Aberto)"* para demonstrar na prática cada grandeza antes de mostrar os componentes reais.

- **Corrente Contínua (DC) vs. Alternada (AC):** O que eles vão tocar na bancada (**12V DC**, seguro ao toque humano) vs. o que nunca vão tocar (**220V AC**, confinado na caixa de potência).

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
| Resistor       | Limita a corrente que passa                                                                             | Está em praticamente toda placa eletrônica que existe, protegendo outros componentes                                                            |
| LED            | Acende com polaridade certa                                                                             | Toda luz indicadora, telas de celular/TV, semáforos modernos, iluminação de casa                                                                |
| Interruptor    | Fica ligado ou desligado até ser acionado de novo (mantém o estado, diferente de um botão de campainha) | Interruptor de luz de parede, chave liga/desliga de aparelhos, disjuntores residenciais                                                         |
| Multímetro     | Mede tensão/continuidade                                                                                | Ferramenta de trabalho de eletricistas, técnicos de manutenção industrial e engenheiros — é o "estetoscópio" de quem mexe com eletrônica        |


## Bloco 4 — Desafio em grupos (35-40 min)

Entrega do Manual da Equipe de Manutenção e do kit com um defeito sorteado. Enquadramento: "engenharia é resolver problema com informação incompleta" — ninguém vai dizer o que está errado, o grupo precisa descobrir.

Monitores circulam entre os grupos, ajudando só com perguntas guiadas ("o que o multímetro está te dizendo?"), não entregando a resposta.

> - O esquemático elétrico, a lista de materiais (BOM) e o guia passo a passo dos 4 defeitos injetados com coordenadas na protoboard e roteiro de diagnóstico estão em [`hardware/explicacao-proposta-circuitos.md`](hardware/explicacao-proposta-circuitos.md).
> - Os manuais impressos de manutenção entregues aos alunos estão disponíveis para impressão em [`materiais-didaticos/manual-do-aluno/manual-conserto-air-fryer.pdf`](materiais-didaticos/manual-do-aluno/manual-conserto-air-fryer.pdf) (ou na versão web em [`manual-conserto-air-fryer.html`](materiais-didaticos/manual-do-aluno/manual-conserto-air-fryer.html)).

## Bloco 5 — Teste final e revelação do relé (15 min)

Cada grupo testa e vê a air fryer ligar. Só então é revelado o que estava por trás: o interruptor deles não liga a air fryer diretamente — ele aciona um relé de estado sólido, que funciona como uma chave controlada: um sinal pequeno (12V) liga ou desliga uma carga grande (220V) sem que os dois circuitos se toquem fisicamente.

Conexão com o mundo real: é assim que máquina de lavar, ar-condicionado e portão eletrônico ligam seus motores; é assim que um CLP (controlador industrial) liga uma máquina inteira numa fábrica; é a base de qualquer automação — inclusive a área de mecatrônica que a equipe estuda.

## Bloco 6 — Fechamento: carreira e roda de conversa (10-15 min)

Conversa aberta: o que é engenharia mecatrônica, como o que eles acabaram de fazer se conecta com robótica, automação industrial e produtos do dia a dia. Formulário curto de avaliação (interesse despertado, o que gostaram, o que não entenderam).

> 📘 **Material de Apoio para a Roda de Conversa:**
> Consulte o [`guia-carreira-mecatronica-ifsc.md`](guia-carreira-mecatronica-ifsc.md). Este documento traz dados sobre o curso de Engenharia Mecatrônica, a ponte direta entre a oficina e a robótica/indústria 4.0, além das opções de **Cursos Técnicos Integrados ao Ensino Médio e Graduação 100% Gratuitos** no IFSC (Câmpus Florianópolis). No **Slide 11** da apresentação para os alunos há um botão com link para o portal do IFSC.