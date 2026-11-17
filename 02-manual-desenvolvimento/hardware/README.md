# 🛠️ Módulo de Hardware e Engenharia da Bancada

> **Projeto:** Entre Fios & Fritas — Desvendando a Eletrônica da Cozinha  
> **Curso:** Engenharia Mecatrônica — IFSC Campus Florianópolis  

Este diretório contém os projetos elétricos, diagramas esquemáticos e o guia completo de montagem, dimensionamento e injeção de falhas para a realização da oficina didática.

---

## 📄 Documento Principal

* **📘 [Guia de Engenharia da Bancada: Circuitos e Injeção de Falhas (Markdown)](explicacao-proposta-circuitos.md)**  
  *(Também disponível em formato editável Microsoft Word: [`explicacao-proposta-circuitos.docx`](explicacao-proposta-circuitos.docx))*  
  Manual técnico e pedagógico para facilitadores e replicadores da oficina. Detalha:
  1. **Arquitetura de Segurança por Projeto (*Safety by Design*):** Separação estrita entre o comando em baixa tensão (12V DC SELV) operado pelos estudantes e a potência de 220V AC confinada com acionamento óptico por Relé de Estado Sólido (SSR).
  2. **Fundamentos e Dimensionamento:** Aplicação da Lei de Ohm e Leis de Kirchhoff ($I \approx 18{,}1\text{ mA}$) com valores comerciais de resistores ($470\,\Omega$).
  3. **Roteiro dos 4 Defeitos Injetados:** Guia completo de cada esquadrão com esquemático da falha, coordenadas na protoboard, sintomas, diagnóstico com multímetro (continuidade, tensão e resistência) e ação de reparo:
     - 🔴 **Bancada 1:** LED Invertido (polaridade reversa / barreira semicondutora).
     - 🟡 **Bancada 2:** Jumper Desconectado / Deslocado (circuito aberto).
     - 🔵 **Bancada 3:** Resistor de $100\text{ k}\Omega$ no lugar de $470\,\Omega$ (limitação extrema de corrente).
     - 🟣 **Bancada 4:** Botão Táctil Rotacionado em 90° (curto-circuito permanente).
  4. **Logística do Facilitador:** Dicas para sincronizar o "tempo da batata frita" (12 a 18 min), demonstração com fusíveis térmicos reais e conscientização sobre limites de segurança em eletrodomésticos com capacitores de alta tensão.
  5. **Lista de Materiais Completa (BOM):** Relação detalhada de todos os componentes por bancada.

---

## 📐 Diagramas e Esquemáticos

* **[`esquematicos/esquematico-circuito.pdf`](esquematicos/esquematico-circuito.pdf):** Diagrama esquemático oficial em formato vetorial com a malha de comando e a ligação do relé SSR.
* **[`esquematicos/circuito-tinkercad.png`](esquematicos/circuito-tinkercad.png):** Montagem visual na protoboard simulada no Tinkercad.
* **[`esquematicos/diagrama-funcionamento.png`](esquematicos/diagrama-funcionamento.png):** Diagrama visual de funcionamento da bancada.
