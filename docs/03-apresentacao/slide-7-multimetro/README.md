# 🔬 Módulo Didático Interativo: Slide 7 — Multímetro 3D & Diagnóstico de Falhas

Este diretório contém o protótipo autônomo do **Slide 7** da apresentação acadêmica do projeto extensionista *"Entre Fios e Fritas: Desvendando a Eletrônica Básica"* (IFSC Mecatrônica).

---

## 📁 Estrutura do Módulo

```text
slide-7-multimetro/
├── slide-7.html              # Página interativa autônoma para testes locais
├── assets/                   # Sprites 3D recortados em alta definição
│   ├── multimetro-completo.png
│   ├── multimetro-corpo.png
│   ├── ponteira-vermelha.png
│   └── ponteira-preta.png
├── scripts/
│   └── separar_sprites.py    # Script em Python (Pillow) para extração de sprites via componente conexo
└── README.md                 # Este documento
```

---

## 🚀 Como Testar Localmente

1. Abra o arquivo [`slide-7.html`](slide-7.html) diretamente em qualquer navegador moderno (Google Chrome, Microsoft Edge, Mozilla Firefox).
2. Não requer servidor local, Node.js ou bibliotecas externas pesadas — utiliza **HTML5 nativo, CSS 3D, SVG e Web Audio API**.

### 🎮 Atalhos de Teclado
* Teclas `1`, `2`, `3` ou `4`: Alterna entre as bancadas de teste.
* `Espaço` ou `Enter`: Executa a medição (desloca as ponteiras até o componente e mede a continuidade).
* Tecla `R`: Retorna o multímetro e as ponteiras à posição de repouso (*dock*).

---

## 🛠️ Tecnologias Utilizadas
* **Composição 2.5D / CSS 3D:** Perspectiva isométrica com rotação tridimensional suave e sombreamento dinâmico.
* **Cabos Flexíveis em SVG:** Curvas cúbicas de Bézier recalculadas em tempo real (`requestAnimationFrame`) simulando a gravidade e a elasticidade dos cabos de silicone.
* **Feedback Sonoro:** Simulação acústica do buzzer piezoelétrico (onda senoidal a 2350 Hz via Web Audio API) idêntica à de multímetros digitais reais (Minipa / Fluke).
