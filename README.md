# GitHub Data Collector (Power BI Ready)

Este projeto coleta dados dos repositórios mais populares do GitHub (usando GraphQL) e salva em um arquivo `.csv`, pronto para ser visualizado no Power BI.

## 🚀 Como rodar

1. Clone ou baixe este repositório
2. Crie um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
4. Configure seu token no arquivo `.env`:
   ```env
   GITHUB_TOKEN=seu_token_aqui
   ```
5. Execute:
   ```bash
   python src/main.py
   ```

Isso irá gerar o arquivo `githubRepos.csv` com até 1000 repositórios.

## 📊 Importar no Power BI

1. Abra o Power BI Desktop
2. Vá em **Obter dados** > **Texto/CSV**
3. Selecione `githubRepos.csv`
4. Crie suas visualizações 📈

---

MIT License.
