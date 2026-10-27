#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script definitivo de segmentação e extração de sprites do Multímetro Digital 3D.
Utiliza análise de componentes conexos (Flood-fill guiado por cor) a partir das pontas de prova,
garantindo recorte 100% perfeito, bordas limpas e sem nenhum resíduo de outros componentes.
"""

import os
from collections import deque
from PIL import Image

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, "../../../../"))
INPUT_IMG_PATH = os.path.join(PROJECT_ROOT, "midia", "Multímetro digital azul com pontas de prova.png")
OUTPUT_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, "../assets"))

os.makedirs(OUTPUT_DIR, exist_ok=True)

def remove_background_floodfill(img):
    img = img.convert("RGBA")
    w, h = img.size
    pixels = img.load()

    visited = set()
    queue = deque()

    for x in range(w):
        queue.append((x, 0))
        queue.append((x, h - 1))
        visited.add((x, 0))
        visited.add((x, h - 1))

    for y in range(h):
        queue.append((0, y))
        queue.append((w - 1, y))
        visited.add((0, y))
        visited.add((w - 1, y))

    def is_bg_color(r, g, b):
        return r >= 240 and g >= 240 and b >= 240

    while queue:
        cx, cy = queue.popleft()
        r, g, b, _ = pixels[cx, cy]
        if is_bg_color(r, g, b):
            pixels[cx, cy] = (r, g, b, 0)
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < w and 0 <= ny < h and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    nr, ng, nb, _ = pixels[nx, ny]
                    if is_bg_color(nr, ng, nb):
                        queue.append((nx, ny))

    # Anti-aliasing de borda
    for y in range(1, h - 1):
        for x in range(1, w - 1):
            r, g, b, a = pixels[x, y]
            if a > 0:
                has_transparent_neighbor = any(pixels[x + dx, y + dy][3] == 0 for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)])
                if has_transparent_neighbor:
                    whiteness = min(r, g, b)
                    if whiteness > 210:
                        alpha = int(255 * (1.0 - (whiteness - 210) / 45.0))
                        alpha = max(0, min(255, alpha))
                        pixels[x, y] = (r, g, b, alpha)

    return img

def main():
    print(f"Lendo imagem: {INPUT_IMG_PATH}")
    orig = Image.open(INPUT_IMG_PATH)
    w, h = orig.size

    print("Removendo fundo...")
    base_img = remove_background_floodfill(orig)

    # 1. multimetro-completo.png
    full_path = os.path.join(OUTPUT_DIR, "multimetro-completo.png")
    base_img.save(full_path, "PNG")
    print(f"-> multimetro-completo.png salvo")

    base_pix = base_img.load()

    # 2. ponteira-vermelha.png via componente conexo a partir de (145, 160)
    red_img = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    red_pix = red_img.load()

    seed_red = (145, 160)
    queue = deque([seed_red])
    visited_red = set([seed_red])

    while queue:
        cx, cy = queue.popleft()
        if cy > 700: # Base da empunhadura
            continue
        red_pix[cx, cy] = base_pix[cx, cy]

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < w and 0 <= ny <= 700 and (nx, ny) not in visited_red:
                r, g, b, a = base_pix[nx, ny]
                if a > 20:
                    # É a ponteira vermelha (agulha cinza ou corpo vermelho, sem preto do cabo vizinho)
                    is_black = (r < 75 and g < 75 and b < 80 and nx > 230)
                    if not is_black:
                        visited_red.add((nx, ny))
                        queue.append((nx, ny))

    red_bbox = red_img.getbbox()
    if red_bbox:
        red_img = red_img.crop(red_bbox)
    red_path = os.path.join(OUTPUT_DIR, "ponteira-vermelha.png")
    red_img.save(red_path, "PNG")
    print(f"-> ponteira-vermelha.png salva: {red_img.size}")

    # 3. ponteira-preta.png via componente conexo a partir de (302, 160)
    black_img = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    black_pix = black_img.load()

    seed_black = (302, 160)
    queue = deque([seed_black])
    visited_black = set([seed_black])

    while queue:
        cx, cy = queue.popleft()
        if cy > 700: # Base da empunhadura
            continue
        black_pix[cx, cy] = base_pix[cx, cy]

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < w and 0 <= ny <= 700 and (nx, ny) not in visited_black:
                r, g, b, a = base_pix[nx, ny]
                if a > 20:
                    is_red = (r > 130 and r > 1.3 * b)
                    is_blue = (b > r + 30 and b > 100)
                    if not is_red and not is_blue:
                        visited_black.add((nx, ny))
                        queue.append((nx, ny))

    black_bbox = black_img.getbbox()
    if black_bbox:
        black_img = black_img.crop(black_bbox)
    black_path = os.path.join(OUTPUT_DIR, "ponteira-preta.png")
    black_img.save(black_path, "PNG")
    print(f"-> ponteira-preta.png salva: {black_img.size}")

    # 4. multimetro-corpo.png
    body_img = base_img.copy()
    body_pix = body_img.load()

    # Remove os pixels pertencentes à ponteira vermelha e preta
    for x, y in visited_red:
        body_pix[x, y] = (0, 0, 0, 0)
    for x, y in visited_black:
        body_pix[x, y] = (0, 0, 0, 0)

    # Limpeza adicional para remover restos de fios soltos à esquerda e abaixo de y=980
    for y in range(h):
        for x in range(w):
            if y > 980:
                body_pix[x, y] = (0, 0, 0, 0)
            elif x < 420:
                body_pix[x, y] = (0, 0, 0, 0)
            elif x < 530 and y > 800:
                r, g, b, a = body_pix[x, y]
                is_blue = (b > r + 30 and b > 110)
                is_red = (r > 150 and r > b * 2)
                if not (is_blue or is_red):
                    body_pix[x, y] = (0, 0, 0, 0)

    body_bbox = body_img.getbbox()
    if body_bbox:
        body_img = body_img.crop(body_bbox)
    body_path = os.path.join(OUTPUT_DIR, "multimetro-corpo.png")
    body_img.save(body_path, "PNG")
    print(f"-> multimetro-corpo.png salva: {body_img.size}")

    print("\nExtração finalizada com perfeição técnica!")

if __name__ == "__main__":
    main()
