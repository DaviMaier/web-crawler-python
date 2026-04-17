
# 🕷️ Web Content Crawler (Python)

Crawler desenvolvido em Python para **extração estruturada de conteúdo web**, com suporte a navegação automática (crawling), persistência de progresso e coleta de dados reutilizáveis para migração ou reconstrução de sistemas.

> Projeto aplicado na prática para migração de conteúdo de um site institucional com mais de 10 anos de dados.

---

# 🎯 Objetivo

Construir uma ferramenta capaz de:

* Navegar automaticamente por um site (crawler)
* Identificar e extrair conteúdos relevantes
* Coletar textos completos das páginas
* Baixar imagens associadas
* Gerar uma base de dados estruturada (JSON)
* Permitir continuidade de execução sem perda de progresso

---

# ✨ Features

* BFS-based crawling strategy
* Persistent state (resume anytime)
* Automatic image downloading
* Structured JSON output
* Duplicate prevention
* Content extraction with fallback strategies

---

# 🧠 Abordagem Técnica

O sistema utiliza uma estratégia de **crawling em largura (BFS)**:

1. Inicializa com uma URL base
2. Percorre links internos do domínio
3. Prioriza páginas de conteúdo (ex: artigos)
4. Evita revisitas com controle de estado
5. Persiste dados continuamente em disco

---

# ⚙️ Tecnologias Utilizadas

* Python 3
* `requests` → requisições HTTP
* `beautifulsoup4` → parsing HTML
* `json` → armazenamento estruturado
* `hashlib` → geração de identificadores únicos

---

# 📂 Estrutura Gerada

```
site_completo/
 ├── html/              # páginas salvas em HTML
 ├── imagens/           # imagens baixadas
 ├── dados.json         # conteúdo estruturado
 ├── visitados.json     # controle de páginas visitadas
 └── fila.json          # fila de URLs pendentes
```

---

# 📊 Estrutura dos Dados

Cada página processada gera um objeto:

```json
{
  "titulo": "Título da página",
  "url": "https://...",
  "arquivo": "site_completo/html/arquivo.html",
  "conteudo": "Texto completo extraído...",
  "imagens": ["caminho/da/imagem.jpg"]
}
```

---

# ▶️ Execução

## 1. Clonar repositório

```
git clone <SEU_REPOSITORIO>
cd web-crawler-python
```

## 2. Instalar dependências

```
pip install -r requirements.txt
```

## 3. Executar crawler

```
python scraper.py
```

---

# 🔄 Persistência de Estado

O crawler salva automaticamente o progresso em:

* `visitados.json`
* `fila.json`
* `dados.json`

Isso permite:

* interrupção manual (`Ctrl + C`)
* retomada exata da execução posteriormente
* execução distribuída em diferentes sessões

---

# 📌 Use Case

Aplicado na migração de mais de 10 anos de conteúdo de um site institucional legado para um sistema moderno.

---

# 🧩 Características Técnicas

* Evita páginas duplicadas
* Geração de nomes únicos via hash (baseado na URL)
* Filtro de links irrelevantes (ex: versões print/pdf)
* Extração resiliente de conteúdo (múltiplos seletores HTML)
* Download automático de imagens
* Estrutura pronta para integração com outros sistemas

---

# ⚠️ Limitações

* Dependente da estrutura HTML do site
* Não executa JavaScript (não suporta SPA/React nativamente)
* Pode coletar páginas irrelevantes sem pós-processamento

---

# 🚀 Possíveis Extensões

* Integração com banco de dados (PostgreSQL, MongoDB)
* Uso de embeddings para busca semântica
* Interface web para visualização dos dados
* Suporte a scraping com JavaScript (Selenium/Playwright)
* Pipeline de limpeza e categorização automática

---

# 👨‍💻 Autor

Desenvolvido por **Davi Maier Prestes da Silva** como solução para extração, migração e reestruturação de conteúdo web em larga escala.

---

# 📄 Licença

Uso livre para fins educacionais e projetos pessoais.
