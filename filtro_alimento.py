import json

with open("site_completo/dados.json", "r", encoding="utf-8") as f:
    dados = json.load(f)

alimentos = []

for item in dados:
    url = item.get("url", "")

    if "catid=7" in url and "view=article" in url:
        alimentos.append(item)

with open("alimentos.json", "w", encoding="utf-8") as f:
    json.dump(alimentos, f, ensure_ascii=False, indent=2)

print("\nFiltro finalizado 🚀")
print(f"Total de alimentos encontrados: {len(alimentos)}")
