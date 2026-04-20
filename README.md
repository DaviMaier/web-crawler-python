# 🕷️ Web Crawler - Content Extraction System

Sistema de web crawler desenvolvido em Python para extração, organização e backup de conteúdos de sites institucionais.

## 📌 Descrição

Este projeto implementa um crawler baseado em estratégia BFS (Breadth-First Search), capaz de percorrer páginas internas de um site, extrair conteúdos relevantes e armazená-los localmente de forma estruturada.

Foi aplicado na migração de mais de 10 anos de conteúdo de um site institucional legado para uma nova plataforma moderna.

---

## 🚀 Funcionalidades

* 🔍 Crawling automático de páginas internas
* 🧠 Estratégia BFS para navegação eficiente
* 💾 Persistência de progresso (retomada automática)
* 📄 Extração de conteúdo HTML e texto limpo
* 🖼️ Download automático de imagens
* 🔗 Descoberta dinâmica de links internos
* ⚡ Prioridade para páginas de conteúdo (`view=article`)
* 📊 Métricas em tempo real:

  * Progresso (%)
  * Páginas coletadas
  * Páginas por segundo (pps)
  * Tempo estimado restante

---

## 🏗️ Estrutura do Projeto

```
site_completo/
│
├── html/              # Páginas HTML extraídas
├── imagens/           # Imagens baixadas
├── dados.json         # Conteúdo estruturado
├── fila.json          # Fila de URLs pendentes
└── visitados.json     # URLs já processadas
```

---

## ⚙️ Tecnologias Utilizadas

* Python 3
* Requests
* BeautifulSoup4
* JSON
* Hashlib

---

## ▶️ Como Executar

### 1. Instalar dependências

```bash
pip install requests beautifulsoup4
```

### 2. Executar o crawler

```bash
python crawler.py
```

---

## 🔁 Retomada Automática

O sistema salva o progresso automaticamente:

* `visitados.json` → páginas já processadas
* `fila.json` → próximas páginas
* `dados.json` → conteúdos extraídos

Permite interromper e continuar sem perda de dados.

---

## 📊 Exemplo de Saída

```bash
[120/5000] (2.40%) - 1.85 pág/s - 65.2 min - https://...
```

---

## 🎯 Caso de Uso

Este crawler foi utilizado para:

* Backup de conteúdo de site legado
* Extração de artigos institucionais
* Preparação de dados para migração de plataforma
* Preservação de conteúdo histórico

---

## ⚠️ Limitações

* Não acessa conteúdos protegidos por login
* Não extrai banco de dados diretamente
* Dependente da estrutura HTML do site

---

## 📌 Observações

* O projeto pode ser adaptado para outros sites alterando a URL base
* Recomenda-se validar a estrutura do site antes da execução
* Ideal para sites com conteúdo público e estruturado

---

## 👨‍💻 Autor

Desenvolvido por Davi Maier Prestes da Silva

---

## 📄 Licença

Este projeto é livre para uso educacional e adaptação.
