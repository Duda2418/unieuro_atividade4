import os
import time
import subprocess
from PIL import Image

Image.MAX_IMAGE_PIXELS = None

from concurrent.futures import ProcessPoolExecutor

# 🔥 AJUSTE AQUI SE NECESSÁRIO
IMAGEM = "imagem_aleatoria_1gb.ppm"

PASTA_PARTES = "partes"
PASTA_SAIDA = "saida"

os.makedirs(PASTA_PARTES, exist_ok=True)
os.makedirs(PASTA_SAIDA, exist_ok=True)


# 🔪 1. Dividir em N partes
def dividir_imagem(n_partes):
    img = Image.open(IMAGEM)
    largura, altura = img.size

    altura_parte = altura // n_partes
    caminhos = []

    for i in range(n_partes):
        topo = i * altura_parte
        base = altura if i == n_partes - 1 else (i + 1) * altura_parte

        parte = img.crop((0, topo, largura, base))

        caminho = f"{PASTA_PARTES}/parte_{i}.ppm"
        parte.save(caminho)

        caminhos.append(caminho)

    return caminhos


# 🧩 2. Juntar partes
def juntar_imagens(n_partes, nome_saida):
    partes = []

    for i in range(n_partes):
        caminho = f"{PASTA_PARTES}/parte_{i}.ppm"
        partes.append(Image.open(caminho))

    largura = partes[0].width
    altura_total = sum(p.height for p in partes)

    nova = Image.new("RGB", (largura, altura_total))

    y = 0
    for p in partes:
        nova.paste(p, (0, y))
        y += p.height

    nova.save(f"{PASTA_SAIDA}/{nome_saida}.ppm")


# ⚙️ 3. Chamar o programa externo (caixa-preta)
def processar(parte):
    subprocess.run([
        "python",
        "conversoremescalacinza (1).py",
        parte
    ])


# 🧪 4. TESTE 1 — dividir em 8 e juntar (sem paralelismo)
def teste_dividir_juntar():
    print("\n🔹 Teste: dividir em 8 e juntar")

    dividir_imagem(8)
    juntar_imagens(8, "teste_juncao")

    print("✔ Teste concluído! Imagem reconstruída.")


# 🚀 5. TESTE 2 — paralelização
def teste_paralelo():
    threads_list = [2, 4, 8, 12]

    for n in threads_list:
        print(f"\n🚀 Executando com {n} threads...")

        partes = dividir_imagem(n)

        inicio = time.time()

        with ProcessPoolExecutor(max_workers=n) as executor:
            executor.map(processar, partes)

        fim = time.time()

        juntar_imagens(n, f"resultado_{n}")

        print(f"⏱ Tempo com {n} threads: {fim - inicio:.2f} segundos")


# ▶️ EXECUÇÃO
if __name__ == "__main__":
    teste_dividir_juntar()   # primeiro teste simples
    teste_paralelo()         # depois paralelismo