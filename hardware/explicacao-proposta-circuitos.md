# 🛠️ Guia de Engenharia da Bancada: Circuitos e Injeção de Falhas

> **Projeto de Extensão:** Entre Fios & Fritas — Desvendando a Eletrônica da Cozinha  
> **Instituição:** Instituto Federal de Santa Catarina (IFSC — Câmpus Florianópolis)  
> **Público-Alvo:** Estudantes do Ensino Médio de Escolas Públicas  
> **Objetivo deste Guia:** Manual de montagem, dimensionamento elétrico, arquitetura de segurança e preparação das 4 bancadas didáticas com defeitos controlados para o facilitador e replicadores da oficina.

---

## 1. Visão Geral e Segurança por Projeto (*Safety by Design*)

A oficina foi concebida sob a metodologia ativa do *"aprender fazendo"* (*hands-on*), onde cada equipe de estudantes assume o papel de técnicos responsáveis por diagnosticar e consertar uma bancada que comanda uma fritadeira elétrica (*Air Fryer*).

```
   ┌────────────────────────────────────────────────────────┐
   │         BANCADA DOS ESTUDANTES (12V DC)                │
   │  [Fonte 12V] ──> [Botão] ──> [Resistor] ──> [LED]      │
   └──────────────────────────┬─────────────────────────────┘
                              │ Sinal de Comando Seguro
                              ▼
   ┌────────────────────────────────────────────────────────┐
   │         BARREIRA DE ISOLAMENTO GALVÂNICO               │
   │      Relé de Estado Sólido (SSR com Fototriac)         │
   │      Isolamento Óptico Total: Luz aciona Chave         │
   └──────────────────────────┬─────────────────────────────┘
                              │ Chaveamento Físico
                              ▼
   ┌────────────────────────────────────────────────────────┐
   │         CIRCUITO DE POTÊNCIA (220V AC)                 │
   │      [Rede 220V] ──> [Fusível 10A] ──> [Air Fryer]     │
   │      CAIXA LACRADA COM PRENSA-CABOS (SEM ACESSO)       │
   └────────────────────────────────────────────────────────┘
```

### Princípios Fundamentais de Segurança
1. **Manipulação 100% em Baixa Tensão (12V DC):**  
   Os estudantes tocam, montam e testam exclusivamente a protoboard energizada em 12V DC (corrente contínua). Essa tensão é classificada como Extra-Baixa Tensão de Segurança (SELV), sendo totalmente inofensiva ao toque humano (sem risco de choque elétrico).
2. **Potência Isolada e Confinada (220V AC):**  
   A alimentação de 220V AC da Air Fryer permanece confinada em uma caixa isolada, com fusível térmico/geral de 10A e prensa-cabos. Nenhum estudante ou participante tem contato mecânico ou elétrico com a rede alternada.
3. **Acionamento Óptico (Sem Conexão Elétrica entre 12V e 220V):**  
   O elo entre a bancada e o eletrodoméstico é um **Relé de Estado Sólido (SSR)**. O acionamento interno é feito por um emissor infravermelho (LED interno) que dispara um sensor óptico (fototriac). Há zero continuidade metálica entre os dois lados do circuito.

---

## 2. Conceitos Fundamentais Trabalhados na Oficina

| Conceito | Aplicação Prática na Bancada |
| :--- | :--- |
| **Tensão ($V$)** | Medição da diferença de potencial fornecida pela fonte (12V) e as quedas em cada componente da malha. |
| **Corrente ($I$)** | Compreensão de que a corrente só flui se a malha for contínua (circuito fechado vs. circuito aberto). |
| **Resistência ($R$)** | Limitação de corrente para proteger o LED e determinação do código de cores dos resistores. |
| **Polaridade** | Diferenciação entre ânodo (+) e cátodo (-) do LED, mostrando que semicondutores só conduzem em sentido direto. |
| **Matriz da Protoboard** | Lógica das conexões internas: barramentos laterais de alimentação (linhas horizontais) e nós centrais (colunas verticais). |
| **Multímetro Digital** | Uso prático de três escalas essenciais: teste de continuidade sonoro (bip), tensão contínua (DCV) e resistência ($\Omega$). |

---

## 3. Circuito de Referência (Gabarito de Montagem Correta)

Na montagem oficial, todos os componentes do circuito de comando estão dispostos em **série**. Quando o botão de comando é pressionado, a malha fecha, a corrente flui, o LED indicador acende e o Relé SSR atraca, disparando a Air Fryer.

### Diagrama Esquemático da Malha de Comando (12V)

```
  (+12V DC) ───[ Linha Vermelha da Protoboard ]
       │
       ▼
 ┌──────────────┐
 │  Push-Button │  (Chave táctil - pinos normalmente abertos)
 └──────┬───────┘
        │
        ▼
 ┌──────────────┐
 │ Resistor 470Ω│  (Limitação de corrente para ~18 mA)
 └──────┬───────┘
        │
        ▼
 ┌──────────────┐
 │ LED Indicador│  (Ânodo no resistor, Cátodo no SSR)
 └──────┬───────┘
        │
        ▼
 ┌──────────────┐
 │  Entrada SSR │  (Borne + do Relé de Estado Sólido)
 │   LU-5-R     │
 │  Entrada SSR │  (Borne - do Relé de Estado Sólido)
 └──────┬───────┘
        │
        ▼
   (GND / 0V) ───[ Linha Azul da Protoboard ]
```

### Memória de Cálculo e Dimensionamento Elétrico

Para que o LED acenda visivelmente e a corrente seja suficiente para saturar com folga o optoacoplador interno do Relé SSR (que exige entre $3\text{ mA}$ e $10\text{ mA}$ para disparo seguro), realizamos o dimensionamento pela Lei de Kirchhoff das Malhas:

$$V_{CC} = V_{\text{botão}} + V_{R} + V_{LED} + V_{SSR}$$

Considerando:
- Tensão da fonte: $V_{CC} = 12{,}0\text{ V}$
- Queda no botão em condução: $V_{\text{botão}} \approx 0\text{ V}$
- Queda de tensão no LED vermelho típico: $V_{LED} \approx 2{,}0\text{ V}$
- Queda de tensão na entrada do SSR (LED infravermelho interno): $V_{SSR} \approx 1{,}5\text{ V}$

A tensão que recai sobre o resistor limitador é:

$$V_{R} = 12{,}0\text{ V} - 2{,}0\text{ V} - 1{,}5\text{ V} = 8{,}5\text{ V}$$

Aplicando a Lei de Ohm para um resistor padrão de $470\,\Omega$:

$$I = \frac{V_{R}}{R} = \frac{8{,}5\text{ V}}{470\,\Omega} \approx 0{,}0181\text{ A} = \mathbf{18{,}1\text{ mA}}$$

> **Conclusão Técnica:** A corrente de $\approx 18\text{ mA}$ é perfeitamente segura para um resistor de $1/4\text{ W}$ ($P = V \cdot I \approx 8{,}5\text{ V} \cdot 0{,}0181\text{ A} \approx 0{,}154\text{ W} < 0{,}25\text{ W}$), garante alta luminosidade ao LED e supera amplamente o limiar de disparo do relé.

---

## 4. Mapeamento das 4 Bancadas com Falhas Injetadas ("Os 4 Esquadrões")

Para tornar a dinâmica acessível no tempo de aula (oficina de 1h30 a 2h), cada bancada recebe um circuito com **exatamente um defeito clássico de montagem**. Os estudantes devem aplicar o método de investigação técnica: observar o sintoma, levantar hipóteses, testar com o multímetro e realizar o conserto.

---

### 🔴 Bancada 1: LED Invertido (Bloqueio por Polaridade Reversa)

* **Conceito Trabalhado:** Polaridade de semicondutores (o diodo só conduz em sentido direto; em sentido reverso, bloqueia a passagem da corrente).
* **O Defeito Injetado:** O LED é inserido com o Cátodo (perna menor / chanfro) voltado para o resistor e o Ânodo (perna longa) voltado para a entrada do SSR.

```
(+12V) ─── [Botão] ─── [Resistor 470 Ω] ─── [ Cátodo (-) ──|>|── Ânodo (+) ] ─── [SSR (+)] ...
                                            ▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲
                                            LED POLARIZADO EM SENTIDO REVERSO
```

* **Montagem na Protoboard:**
  - Resistor conectado na **Linha 10**.
  - Perna menor do LED (Cátodo) inserida na **Linha 10**.
  - Perna maior do LED (Ânodo) inserida na **Linha 11**.
  - Jumper que vai ao SSR (+) inserido na **Linha 11**.
* **Sintoma Observado:** Ao pressionar o botão, o LED não acende e a Air Fryer não liga.
* **Roteiro de Diagnóstico com Multímetro:**
  1. *Escala de Tensão DC (20V):* Manter o botão pressionado e medir sobre os terminais do LED. O multímetro indicará praticamente os $12\text{V}$ inteiros da fonte, comprovando que o LED está agindo como uma barreira aberta.
  2. *Escala de Teste de Diodo:* Com o circuito desenergizado, colocar a ponta vermelha no ânodo e a preta no cátodo. O display só mostrará condução se as pontas forem invertidas.
* **Ação de Correção:** Desespetar o LED da protoboard, girá-lo em 180° e reinseri-lo com a perna longa (ânodo) na Linha 10 (lado do resistor).

---

### 🟡 Bancada 2: Jumper em Linha Deslocada (Circuito Aberto)

* **Conceito Trabalhado:** Matriz de contatos da protoboard (furos na mesma coluna compartilham o mesmo contato metálico; colunas adjacentes são isoladas entre si).
* **O Defeito Injetado:** Um jumper que deveria conectar a saída do resistor à entrada do LED é inserido uma linha ao lado, criando uma descontinuidade física invisível ao olho desatento.

```
(+12V) ─── [Botão] ─── [Linha 15: Resistor 470 Ω]  (Circuito Aberto / Vazio)
                             ✖ DESCONEXÃO FÍSICA
                       [Linha 16: Jumper] ─────── [Ânodo LED] ─── [SSR (+)] ...
```

* **Montagem na Protoboard:**
  - O resistor de $470\,\Omega$ termina na **Linha 15**.
  - O jumper de interligação é espetado na **Linha 16** (uma linha abaixo).
  - O LED está inserido entre a Linha 16 e a Linha 17.
* **Sintoma Observado:** Visualmente o circuito parece perfeito, mas a corrente é zero. Apertar o botão não produz nenhum efeito.
* **Roteiro de Diagnóstico com Multímetro:**
  1. *Escala de Continuidade (Bip Sonoro):* Com o circuito desenergizado, encostar uma ponta de prova no terminal de saída do resistor e a outra ponta no terminal do jumper.
  2. *Resultado:* Silêncio total ($O.L$ no display). O multímetro não apita, provando aos alunos que não há conexão elétrica entre a Linha 15 e a Linha 16.
* **Ação de Correção:** Mover o jumper da Linha 16 para a Linha 15, compartilhando a mesma trilha condutora do resistor.

---

### 🔵 Bancada 3: Resistor de Valor Excessivo (Atenuação Severa de Corrente)

* **Conceito Trabalhado:** Primeira Lei de Ohm ($I = V/R$) e código de cores dos resistores.
* **O Defeito Injetado:** O resistor correto de $470\,\Omega$ (amarelo, violeta, marrom) é substituído por um resistor de **$100\text{ k}\Omega$** (marrom, preto, amarelo) ou **$1\text{ M}\Omega$** (marrom, preto, verde).

```
(+12V) ─── [Botão] ─── [ Resistor 100 kΩ ] ─── [ LED ] ─── [ SSR (+) ] ─── [ SSR (-) ] ─── (GND)
                       ▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲
                       Corrente atenuada para ~0,08 mA (Abaixo do limiar do SSR)
```

* **Cálculo da Falha:**
  
  $$I_{\text{defeito}} = \frac{8{,}5\text{ V}}{100.000\,\Omega} = 0{,}000085\text{ A} \approx \mathbf{0{,}085\text{ mA}} \; (85\,\mu\text{A})$$

* **Sintoma Observado:** A corrente é tão minúscula que o LED não emite luz visível e o optotriac do Relé SSR não atinge a corrente mínima de disparo ($3\text{ mA}$ a $10\text{ mA}$). A Air Fryer permanece inerte.
* **Roteiro de Diagnóstico com Multímetro:**
  1. *Inspeção Visual:* Comparar a tabela de código de cores do Manual do Aluno com as faixas do resistor da bancada.
  2. *Escala de Resistência ($\Omega$):* Com o circuito desenergizado, medir a resistência sobre os terminais do componente. O visor apontará $100\text{ k}\Omega$ (ou valor fora da escala de ohms baixos), revelando que a resistência é mais de 200 vezes maior do que o projeto previa.
* **Ação de Correção:** Substituir o componente pelo resistor correto de $470\,\Omega$ fornecido no kit da bancada.

---

### 🟣 Bancada 4: Botão Táctil Rotacionado em 90° (Curto-Circuito Permanente)

* **Conceito Trabalhado:** Topologia interna de chaves tácteis (*push-buttons* de 4 pinos: os pinos opostos são unidos em pares por barras metálicas internas; o clique apenas conecta os dois pares entre si).
* **O Defeito Injetado:** O botão é montado girado em 90° em relação ao canal central da protoboard. Com isso, o fio de entrada (+12V) e o resistor ficam conectados aos terminais que já são unidos internamente pela carcaça do botão.

```
(+12V) ─── [ Barra interna contínua do Botão ] ─── [ Resistor ] ─── [ LED ] ─── [ SSR ]
           ▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲
           CIRCUITO PERMANENTEMENTE FECHADO (CURTO DIRETO)
```

* **Sintoma Observado:** Ao ligar a fonte de alimentação na tomada, **o LED acende imediatamente e a Air Fryer começa a funcionar na mesma hora**, sem que ninguém toque no botão! Apertar o botão não surte nenhum efeito.
* **Roteiro de Diagnóstico com Multímetro:**
  1. Retirar o botão da protoboard para testá-lo isoladamente na bancada.
  2. *Escala de Continuidade (Bip Sonoro):* Colocar as pontas de prova nos terminais do botão **sem apertar**. O multímetro apita continuamente ($0{,}00\,\Omega$), provando que aqueles dois pinos estão em curto permanente no sentido em que foram conectados.
* **Ação de Correção:** Girar o botão em 90° e reinseri-lo sobre a fenda central da protoboard, garantindo que o canal separe os dois lados e a corrente só passe sob o clique mecânico.

---

## 5. Dicas Pedagógicas e Logística para o Facilitador

### ⏱️ A Gestão do "Tempo da Batata Frita"
Uma das grandes atrações da oficina é a recompensa real das batatas fritas prontas ao final. No entanto, o preparo de batatas congeladas em uma Air Fryer leva entre **12 e 18 minutos** a 200 °C:

1. **Estratégia Recomendada:**
   - Antes do início da dinâmica das equipes, o facilitador demonstra a bancada de testes e realiza um breve pré-aquecimento do cesto com as batatas.
   - Durante a resolução dos enigmas pelas equipes, a Air Fryer permanece conectada ao relé principal.
   - Assim que a primeira equipe conclui o conserto e comuta a chave, o aquecimento final entra em ação.
   - Enquanto o cesto termina de dourar as batatas, o facilitador conduz a roda de conversa reflexiva sobre segurança e cursos do IFSC.

### 🔌 Conexão com Defeitos Domésticos Reais
Durante a explicação de encerramento, o instrutor deve exibir um **Fusível Térmico real de eletrodoméstico**:
- **O que quebra de verdade numa Air Fryer?** Na imensa maioria dos casos de descarte de eletroportáteis, o aparelho parou de funcionar porque a ventoinha travou com gordura ou houve sobreaquecimento, rompendo o termofusível interno de proteção.
- **Demonstração com o Multímetro:** O professor testa um fusível queimado (silêncio total / $O.L$) e um fusível novo (bip contínuo sonoro). Isso desmistifica o conserto e mostra que um componente de R$ 3,00 pode evitar o descarte de um aparelho de R$ 300,00.

### 🛡️ Limites Éticos e Conscientização de Risco
É dever pedagógico da oficina alertar os estudantes sobre o que **NÃO** fazer em casa:
- Nunca abrir aparelhos ligados à tomada ou logo após o uso.
- Alguns equipamentos domésticos (como fornos de micro-ondas, fontes de computadores e TVs antigas) possuem **capacitores de alta tensão** que armazenam cargas letais mesmo após semanas desligados da tomada.
- O conserto seguro exige método, instrumentos certificados e capacitação formal — exatamente a proposta dos cursos técnicos e de Engenharia Mecatrônica do IFSC.

---

## 6. Lista de Materiais da Bancada Completa (BOM)

| Item | Componente / Especificação | Qtd por Bancada | Função no Projeto |
| :---: | :--- | :---: | :--- |
| **1** | Fonte Chaveada 12V DC (1A ou 2A) | 1 un | Alimentação segura da protoboard |
| **2** | Protoboard 400 ou 830 pontos | 1 un | Montagem e matriz de contato dos alunos |
| **3** | Push-Button 4 pinos (6x6mm) | 1 un | Chave táctil de comando |
| **4** | Resistor $470\,\Omega$ / 1/4W (amarelo, violeta, marrom) | 1 un | Resistor oficial de limitação |
| **5** | Resistor $100\text{ k}\Omega$ (marrom, preto, amarelo) | 1 un | Resistor de falha da Bancada 3 |
| **6** | LED Difuso 5mm (Vermelho ou Verde) | 1 un | Indicador de passagem de corrente |
| **7** | Relé de Estado Sólido (SSR) com entrada 3-32V DC e saída 24-380V AC (ex: Fotek, LU-5-R ou similar) | 1 un | Acoplador óptico de potência |
| **8** | Jumpers Macho-Macho | 6 un | Interligação dos nós da protoboard |
| **9** | Multímetro Digital com escala de continuidade sonoro | 1 un | Instrumento de diagnóstico das equipes |
| **10** | Caixa de Potência Trancada com Fritadeira Air Fryer 220V | 1 conjunto geral | Carga final demonstrativa e recompensa |
