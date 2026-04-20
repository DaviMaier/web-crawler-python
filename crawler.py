import requests
from bs4 import BeautifulSoup
import os
import json
import re
import time
import hashlib
from urllib.parse import urljoin, urlparse

BASE_URL = "https://ippf.org.br"

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

os.makedirs("site_completo/html", exist_ok=True)
os.makedirs("site_completo/imagens", exist_ok=True)

# ---------------------------
# CARREGAR PROGRESSO
# ---------------------------
if os.path.exists("site_completo/visitados.json"):
    with open("site_completo/visitados.json", "r", encoding="utf-8") as f:
        visitados = set(json.load(f))
else:
    visitados = set()

if os.path.exists("site_completo/fila.json"):
    with open("site_completo/fila.json", "r", encoding="utf-8") as f:
        fila = json.load(f)
else:
    fila = [BASE_URL]

if os.path.exists("site_completo/dados.json"):
    with open("site_completo/dados.json", "r", encoding="utf-8") as f:
        dados = json.load(f)
else:
    dados = []

# ---------------------------
# UTIL
# ---------------------------
def limpar_nome(nome):
    nome = nome.lower()
    nome = re.sub(r'[^a-z0-9]', '-', nome)
    return nome[:60]

def eh_interno(url):
    return "ippf.org.br" in urlparse(url).netloc

def ja_visitado(url):
    return url in visitados

# ---------------------------
# BAIXAR IMAGENS
# ---------------------------
def baixar_imagens(soup, base_url):
    imagens = []

    for img in soup.find_all("img"):
        src = img.get("src")
        if not src:
            continue

        url_img = urljoin(base_url, src)
        nome = url_img.split("/")[-1]

        if nome.strip() == "":
            continue

        caminho = f"site_completo/imagens/{nome}"

        try:
            if not os.path.exists(caminho):
                img_data = requests.get(url_img, headers=HEADERS, timeout=10).content
                with open(caminho, "wb") as f:
                    f.write(img_data)

            imagens.append(caminho)
        except:
            pass

    return imagens

# ---------------------------
# EXTRAIR CONTEÚDO
# ---------------------------
def extrair_conteudo(soup):
    conteudo = soup.find("div", class_="item-page")

    if not conteudo:
        conteudo = soup.find("div", id="content")

    if not conteudo:
        conteudo = soup.find("table")

    if not conteudo:
        conteudo = soup.find("body")

    return conteudo

# ---------------------------
# PEGAR TÍTULO MELHOR
# ---------------------------
def extrair_titulo(soup):
    if soup.find("h1"):
        return soup.find("h1").get_text(strip=True)

    if soup.find("h2"):
        return soup.find("h2").get_text(strip=True)

    if soup.title:
        return soup.title.get_text(strip=True)

    return "pagina"

# ---------------------------
# PROCESSAR PÁGINA
# ---------------------------
def processar_pagina(url):
    print("Visitando:", url)

    try:
        res = requests.get(url, headers=HEADERS, timeout=10)

        if "text/html" not in res.headers.get("Content-Type", ""):
            return

        soup = BeautifulSoup(res.text, "html.parser")

        titulo = extrair_titulo(soup)
        conteudo = extrair_conteudo(soup)

        if not conteudo:
            return

        html = str(conteudo)
        texto_limpo = conteudo.get_text(separator=" ", strip=True)

        # nome único
        hash_url = hashlib.md5(url.encode()).hexdigest()[:8]
        nome = limpar_nome(titulo) + "-" + hash_url

        caminho_html = f"site_completo/html/{nome}.html"

        with open(caminho_html, "w", encoding="utf-8") as f:
            f.write(html)

        imagens = baixar_imagens(conteudo, url)

        dados.append({
            "titulo": titulo,
            "url": url,
            "arquivo": caminho_html,
            "conteudo": texto_limpo,
            "imagens": imagens
        })

        # novos links
        for a in soup.find_all("a", href=True):
            link = urljoin(url, a["href"])

            if "format=pdf" in link or "print=1" in link:
                continue

            if eh_interno(link) and not ja_visitado(link):
                if "view=article" in link:
                    fila.insert(0, link)
                else:
                    fila.append(link)

    except Exception as e:
        print("Erro:", e)

# ---------------------------
# EXECUÇÃO
# ---------------------------
LIMITE_PAGINAS = 5000

while fila and len(visitados) < LIMITE_PAGINAS:
    url = fila.pop(0)

    if ja_visitado(url):
        continue

    visitados.add(url)

    processar_pagina(url)

    # salvar progresso
    with open("site_completo/visitados.json", "w", encoding="utf-8") as f:
        json.dump(list(visitados), f, ensure_ascii=False, indent=2)

    with open("site_completo/fila.json", "w", encoding="utf-8") as f:
        json.dump(fila, f, ensure_ascii=False, indent=2)

    with open("site_completo/dados.json", "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=2)

    time.sleep(1)

print("\nFinalizado 🚀")
print(f"Páginas coletadas: {len(dados)}")
