### Conceitos Fundamentais de Circuitos Elétricos e Eletrônica Básica

- - **Grandezas Elétricas Elementares:** Introduzir de forma prática os conceitos de **tensão**, **corrente** e **resistência**, além do conceito de **circuito fechado versus circuito aberto**

(a corrente só flui se houver continuidade física).

##### Componentes Básicos e Função

- - - **Resistores:** Limitação de corrente.
      - **LEDs:** Indicadores visuais de funcionamento e a importância da **polaridade**

(anodo/catodo).

- - - **Chaves e Botões (Push-buttons):** Abertura e fechamento de trechos de comando.
      - **Relé de Estado Sólido (Conceito):** Ensinar que o relé funciona como uma "chave acionada eletronicamente", em que uma baixa tensão comanda a ligação de um eletrodoméstico.

### Leitura e Montagem em Protoboard (Matriz de Contatos)

- - **Estrutura e Lógica da Protoboard:** Ensinar como funcionam as conexões internas: - As trilhas laterais de alimentação (linhas horizontais de + e -). - As colunas de conexão de nós (linhas verticais de componentes).
    - **Inserção e Organização:** Como posicionar os terminais sem entortá-los e como ligar os

_jumpers_ entre os nós corretos.

### Diagnóstico de Defeitos e Uso do Multímetro

- - **Operação Básica do Multímetro:** Como utilizar as escalas para medição de **tensão contínua (DC)** e, fundamentalmente, a função de **continuidade / teste sonoro** para rastreamento de nós.
    - **Método de Resolução de Problemas (Troubleshooting):** Como levantar hipóteses diante de um circuito inoperante (o "defeito" simulado da equipe) e testar nó a nó onde a conexão foi interrompida ou montada de forma invertida.

### Segurança Elétrica e Noções de Montagem

- - **Diferenciação entre Baixa Tensão e Rede Elétrica:** Ensinar que na bancada eles estão manipulando apenas **12V (corrente contínua)**, totalmente seguro ao toque humano, enquanto a rede elétrica de 220V permanece isolada em uma caixa fechada.
    - **Conscientização de Segurança:** Cuidados essenciais ao energizar circuitos e manusear eletrodomésticos reais.

A proposta é **totalmente viável**, pedagogicamente excelente e está perfeitamente alinhada à metodologia ativa de _"aprender fazendo"_ descrita na proposta do projeto.

A seguir, apresento uma análise crítica de viabilidade, pontos fortes, riscos e sugestões práticas para estruturar a dinâmica:

### Pontos Fortes da Proposta

- - **Conexão Realidade-Conceito:** A recompensa tangível (a batata frita pronta no final) conecta o esforço cognitivo à utilidade prática imediata de um eletrodoméstico, aumentando muito o engajamento.
    - **Segurança por Isolamento (Arquitetura do Protótipo):** Como definido no Documento 3, a bancada opera em **12V DC** na protoboard. A comutação da rede de 220V é feita por um relé de estado sólido (SSR) confinado em uma caixa fechada com fusível e prensa-cabos. Os estudantes **nunca têm contato com a alta tensão**, eliminando o risco de choque elétrico durante a atividade.
    - **Formação Cidadã e Limites de Segurança:** Ensinar que aparelhos têm riscos internos (capacitores carregados, tensões de rede, ferramentas térmicas como ferro de solda) ensina responsabilidade, desmistifica a tecnologia e previne acidentes domésticos, além de valorizar a formação técnica/engenharia no IFSC.

### Definição do Tipo de Esquemático: Literal vs. Simplificado/Colorido

##### Recomendação: Utilize um esquemático pictórico / híbrido e colorido

- - **Por quê?** Estudantes de ensino médio nunca viram diagramas elétricos normatizados (NBR/IEC). Entregar símbolos puros de transistores, resistores e chaves pode gerar uma barreira visual desnecessária e frustração inicial.

##### Como fazer

- - - Desenhe os componentes no formato visual real (desenho da protoboard com as colunas numeradas/letradas e componentes com suas cores e terminais destacados: perna maior do LED para ânodo, faixas do resistor, etc.).
      - Paralelamente, em um canto da folha, coloque o **símbolo esquemático oficial** de cada componente. Assim, você introduz a simbologia técnica de engenharia sem travar a execução do reparo.

### Cenários de "Defeito" Sugeridos para a Protoboard

Para que a resolução seja acessível no tempo de uma oficina, divida as equipes com defeitos clássicos e progressivos:

1. **LED / Diodo Invertido:** O circuito está todo montado, mas o LED (ou diodo de proteção

da bobina/comando) está invertido. O circuito não fecha e a air fryer não aciona.

1. **Jumper em Linha Deslocada:** O jumper deveria conectar à linha do resistor, mas está espetado na coluna ao lado (circuito aberto).
2. **Resistor de Valor Incorreto ou Faltando:** Limitação excessiva de corrente impedindo o sinal de controle no relé SSR.
3. **Push-Button / Chave Rotacionada em 90°:** O botão está conectado em terminais permanentemente em curto ou permanentemente abertos devido à pinagem interna da protoboard.

### Viabilidade Prática do "Tempo da Batata Frita" (Atenção Operacional)

A ideia de assar batatas fritas é o ponto alto da gamificação, mas exige atenção logística:

- - **Tempo de Preparo:** Uma porção de batatas na air fryer leva de **12 a 20 minutos** a 200

°C. Se cada bancada for ligar a air fryer apenas no último minuto da oficina, os alunos não conseguirão comer a tempo sem estourar o horário da aula.

##### Sugestão Prática

- - - **Etapa 1:** A air fryer já pode ficar pré-aquecida e ligada em um teste inicial demonstrativo pelo grupo de Mecatrônica.
      - **Etapa 2:** Durante o desafio das equipes, a alimentação principal fica conectada ao relé SSR com o cesto já carregado com as batatas. À medida que as bancadas validam seus circuitos de 12V em protoboard, o sinal é comutado e o cozimento acontece enquanto se realiza a roda de conversa e a explicação sobre fusíveis/segurança.

### Abordagem sobre Consertos Domésticos e Segurança

A inclusão da explicação sobre fusíveis térmicos e capacitores é muito pertinente:

- - **Fusível Térmico da Air Fryer:** É o defeito real mais comum desse aparelho (quando a ventoinha trava ou há sobreaquecimento, o termofusível queima). Mostrar o componente e demonstrar o teste com a **escala de continuidade do multímetro (bip sonoro)** é simples, visual e impactante.
    - **Mensagem Educativa e Limites Éticos:** Enfatize que:
      - Manusear equipamentos ligados à tomada ou logo após o desligamento apresenta risco de choque e queimaduras.
      - Alguns aparelhos (micro-ondas, fontes de alimentação) acumulam cargas perigosas em capacitores de alta tensão mesmo fora da tomada.
      - O conserto responsável exige capacitação técnica formal e ferramentas seguras, servindo de convite para conhecerem cursos do IFSC.

Para implementar a dinâmica na oficina, o circuito de bancada deve operar em **12V DC**, controlando a entrada de acionamento do Relé de Estado Sólido (SSR) em série com um LED indicador, um resistor e o botão de acionamento. Quando a malha é fechada corretamente, o SSR chaveia a alimentação de 220V (confinada na caixa de proteção) e aciona a air fryer.

## Circuito de Refierência (Montagem Correta)

Neste arranjo em série, o relé só fecha se todos os componentes estiverem operacionais e com a polaridade adequada.

Plaintext

\[ +12V DC \] ──── (Linha +)

│

\[ Push-Button \] (Pinos normais abertos)

│

\[ Resistor 470 Ω \] (Limitação de corrente)

│

\[ Ânodo (+) LED Cátodo (-) \]

│

\[ Entrada SSR (+) \] ─── (Relé de Estado Sólido) \[ Entrada SSR (-) \]

│

\[ GND / 0V \] ─── (Linha -)

- **Cálculo da corrente nominal:** Com fonte de 12V, queda de tensão no LED de, aproximadamente, 2V e na entrada do SSR de, aproximadamente, 1,5V, a queda no resistor de 470 Ohms é de 8,5V, resultando em uma corrente de aproximadamente **18 mA**. Essa corrente acende o LED e satura com folga o optoacoplador de disparo do relé.

## Mapeamento dos 4 Cenários de Defieito

#### Equipe 1: LED Invertido (Bloqueio por Polaridade)

- - **O Defieito:** O LED está inserido com o Cátodo voltado para o lado positivo do circuito e o Ânodo voltado para o SSR.

##### Diagrama do Circuito com Falha

Plaintext

(+12V) ─── \[Botão\] ─── \[Resistor 470 Ω\] ─── \[ Cátodo (-) ──|>|── Ânodo (+) \] ─── \[SSR (+)\] ...

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ LED POLARIZADO REVERSO

##### Montagem prática na protoboard

- Linha 10: Terminal do Resistor e **perna menor (Cátodo / chanfiro reto)** do LED.
- Linha 11: Perna maior (Ânodo) do LED conectada ao fio que vai ao borne (+) do SSR.
  - **Sintoma:** Ao pressionar o botão, o LED não acende e a air fryer não liga.
  - **Diagnóstico com multímetro:** Na escala de tensão DC (20V), ao segurar o botão, a tensão de 12V inteira recai sobre o LED bloqueado. Na escala de teste de diodo, com o circuito desenergizado, o multímetro indicará condução apenas se inverterem as pontas de prova.
  - **Correção:** Inverter o LED na protoboard (perna longa/ânodo voltada para o resistor).

#### Equipe 2: Jumper em Linha Deslocada (Circuito Aberto)

- - **O Defieito:** Um jumper que deveria interligar dois componentes está espetado na coluna ao lado, aproveitando-se do fato de que os furos adjacentes na protoboard não compartilham contato metálico.

##### Diagrama do Circuito com Falha

Plaintext

(+12V) ─── \[Botão\] ─── \[Linha 15: Resistor 470 Ω\] (Vazio / Aberto)

X

\[Linha 16: Jumper\] ───────── \[Ânodo LED\] ─── \[SSR (+)\] ...

##### Montagem prática na protoboard

- O resistor de 470 Ω termina na **Linha 15**.
- O jumper que deveria ligar o resistor ao ânodo do LED é inserido na **Linha 16** (uma linha abaixo).
- O LED continua inserido na Linha 16 e Linha 17.
  - **Sintoma:** O circuito parece visualmente alinhado para um olhar desatento, mas a corrente é zero. Pressionar o botão não produz nenhum efeito.
  - **Diagnóstico com multímetro:** Na escala de continuidade (bip sonoro), colocar uma

ponta de prova no terminal do resistor e a outra no jumper. O multímetro não apita, provando a descontinuidade do nó.

- - **Correção:** Mover o jumper da Linha 16 para a Linha 15, fechando a trilha condutora.

#### Equipe 3: Resistor de Valor Excessivo (Corrente Insuficiente)

1. **O Defieito:** Substituir o resistor correto de 470 Ohms por um resistor de **100k Ohms** (marrom, preto, amarelo) ou **1M Ohms** (marrom, preto, verde).

##### Diagrama do Circuito com Falha

Plaintext

(+12V) ─── \[Botão\] ─── \[ Resistor 100 kΩ \] ─── \[ LED \] ─── \[ SSR (+) \] ─── \[ SSR (-) \]

─── (GND)

^^^^^^^^^^^^^^^^^^^ Corrente limitada a 0,08 mA

##### Montagem prática na protoboard

- - Inserir fisicamente o resistor de 100k Ohms no mesmo local onde deveria estar o de 470 Ohms.

1. **Sintoma:** A corrente do circuito cai para 𝐼 = <sup>8,5</sup> <sup>𝑉</sup> ≈ 0, 08 𝑚𝐴 (80 µ𝐴). O LED

100.000 Ω

permanece apagado e a corrente não atinge o limiar mínimo de disparo do SSR (que exige tipicamente entre 3 𝑚𝐴 e 10 𝑚𝐴), mantendo a air fryer desligada.

##### Diagnóstico com multímetro

- - Conferência visual do código de cores das faixas.
    - Com o circuito desenergizado, colocar o multímetro na escala de resistência (Ω) sobre

os terminais do componente para constatar o valor de 100 𝑘Ω em vez de 470 Ω.

1. **Correção:** Substituir o componente pelo resistor de 470 Ω (amarelo, violeta, marrom) ou

330 Ω (laranja, laranja, marrom).

1. **Equipe 4: Push-Button Rotacionado em 90° (Curto Permanente)**
   - **O Defieito:** As chaves tácteis quadradas de 4 pinos possuem seus terminais internamente conectados aos pares (Pino 1 ligado ao Pino 2; Pino 3 ligado ao Pino 4). Ao girar a chave em 90° na protoboard, o sinal de entrada e o de saída ficam conectados ao mesmo par condutor contínuo.

##### Diagrama do Circuito com Falha

Plaintext

(+12V) ─── \[ Pinos 1 e 2 unidos internamente pela carcaça \] ─── \[ Resistor \] ─── \[ LED \]

─── \[ SSR \]

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ CIRCUITO CONTINUAMENTE FECHADO

##### Montagem prática na protoboard

- O botão é montado girado sobre o canal central de modo que o trilho de entrada (+12V) e a saída para o resistor fiquem conectados nos pinos correspondentes ao mesmo lado interno da chave.
  - **Sintoma:** Ao energizar a fonte de 12V, **o LED acende imediatamente e a air firyer liga na mesma hora**, sem que ninguém pressione o botão. Pressionar o botão não desliga o aparelho.
  - **Diagnóstico com multímetro:** Retirar o botão da protoboard e colocar o multímetro na escala de continuidade\[cite: 3\]. Ao testar os terminais sem pressionar, o multímetro apita direto, revelando que a chave está permanentemente em curto no sentido em que foi instalada.
  - **Correção:** Girar a chave em 90° para que o canal central separe os pares condutores e a passagem de corrente ocorra apenas sob o clique mecânico.