# trabalho-DevOps
# 🤖 Exploradores DevOps – GitHub Actions na Prática

Projeto acadêmico desenvolvido para a disciplina de DevOps.  
**Tecnologia explorada:** GitHub Actions  
**Grupo:** _Arthur Mota, Fillipe Barbosa, Isadora Martins, Rebeca Alencar, Vitória Merlino_

---

## 📌 O que é GitHub Actions?

GitHub Actions é uma plataforma de **integração contínua e entrega contínua (CI/CD)** integrada ao próprio GitHub. Ela permite automatizar tarefas do desenvolvimento de software diretamente no repositório, sem precisar de ferramentas externas.

Com o GitHub Actions, sempre que um desenvolvedor envia código novo (via `push`), o GitHub pode automaticamente:

- Rodar testes para verificar se o código está funcionando
- Verificar a qualidade do código
- Compilar o projeto
- Fazer deploy em servidores

Tudo isso sem intervenção manual.

---

## 🎯 Objetivo da Demonstração

Este projeto demonstra o uso do GitHub Actions para **executar testes automáticos** em um pequeno programa Python (uma calculadora) sempre que novo código é enviado ao repositório.

A ideia central é mostrar na prática o conceito de **CI (Integração Contínua):** qualquer alteração no código é automaticamente testada, e o resultado fica visível para todo o time.

---

## 🪢 Passo a passo de como foi construído o repositório:
1. **Criação do repositório:** um repositório público no GitHub, inicializado com um README.md padrão, gerado automaticamente.
   
2. **Configuração do workflow:** foi adicionado um novo arquivo chamado `.github/workflows/rodar-python.yml`, onde já foi criado de uma só vez o diretório (pasta) e o arquivo .yml que roda a automação.

3. **Configuração do arquivo rodar-python.yml:** foi configurado dentro deste arquivo o gatilho que rodaria a automação (`push`), a máquina virtual que rodará a automação (Ubuntu), a instalação de uma versão do python e o arquivo que será rodado na automação (`test_calculadora.py`).
   
4. **Criação do arquivo calculadora.py:** um arquivo python com 4 funções básicas: somar, subtrair, multiplicar e dividir. A função dividir inclui validação de divisão por zero, lançando um ValueError caso o divisor seja zero.
   
5. **Criação do arquivo test_calculadora.py:** arquivo de teste do arquivo `calculadora.py`, usando a biblioteca pytest. O arquivo possui 5 testes: test_somar, test_subtrair, test_multiplicar, test_dividr e test_dividir_por_zero.
   
6. **Verificação do resultado:** após os arquivos devidamente criados e ser feito um `push` no GitHub, o workflow rodou automaticamente e foram verificados os resultados para saber se os arquivos continham algum erro. 

---

## 📁 Estrutura do Repositório

```
trabalho-DevOps/
├── .github/
│   └── workflows/
│       └── rodar-python.yml     ← o workflow de automação
├── calculadora.py               ← código que será testado
├── test_calculadora.py          ← testes automáticos com pytest
└── README.md                    ← este arquivo
```

---

## ⚙️ Como funciona o Workflow

O arquivo `.github/workflows/rodar-python.yml` define o fluxo de automação.

```yaml
name: Testes Automáticos - Calculadora Python

on: [push]   # dispara a cada push no repositório

jobs:
  executar-python:
    runs-on: ubuntu-latest   # roda em uma máquina virtual Ubuntu

    steps:
      - name: Baixar o código do repositório
        uses: actions/checkout@v4.2.2   # copia os arquivos para a máquina virtual

      - name: Instalar Python
        uses: actions/setup-python@v5.6.0
        with:
          python-version: '3.11'

      - name: Instalar dependências de teste
        run: pip install pytest   # instala a ferramenta de testes

      - name: Rodar os testes automáticos
        run: pytest test_calculadora.py -v   # executa os testes e mostra o resultado
```

**Passo a passo do que acontece a cada push:**

1. O GitHub detecta que novo código foi enviado;
2. Sobe uma máquina virtual Ubuntu do zero;
3. Baixa o código do repositório para essa máquina;
4. Instala o Python 3.11;
5. Instala o pytest;
6. Roda os testes da calculadora;
7. Exibe ✅ (passou) ou ❌ (falhou) para cada teste;
8. Desliga a máquina virtual.

---

## 🧪 O que é pytest e como os testes funcionam

**pytest** é uma ferramenta Python que automatiza a verificação do código. Em vez de testar manualmente cada função, você escreve um arquivo de testes uma vez e o pytest verifica tudo em segundos.

A palavra-chave principal é o `assert` ("afirmo que"):

```python
assert somar(2, 3) == 5   # afirmo que somar 2 e 3 deve retornar 5
```

Se a afirmação for verdadeira → teste passa ✅.
Se for falsa → teste falha ❌ e o GitHub Actions notifica o time.

---

## ✅ Vantagens do GitHub Actions

- **Integrado ao GitHub:** não precisa configurar ferramentas externas;
- **Gratuito para repositórios públicos;**
- **Feedback imediato:** o time sabe em segundos se o código quebrou algo;
- **Reproduzível:** cada execução roda em um ambiente limpo e idêntico;
- **Marketplace de actions:** milhares de automações prontas para usar.

---

## ❓ Dificuldades enfrentadas
- **Pasta com nome incorreto:** a pasta foi criada como `trabalho.github/workflows` em vez de `.github/workflows`, fazendo o GitHub Actions ignorar o workflow completamente;
- **Ordem dos arquivos:** a princípio, os arquivos foram criados em commits separados, fazendo o workflow rodar antes de todos existirem e causando erro de `exit code 2`;
- **Versões desatualizadas:** as actions `checkout` e `setup-python` exibiram aviso de depreciação do Node.js 20, resolvido atualizando para versões específicas (`@v4.2.2` e `@v5.6.0`).

---

## ⚠️ Limitações

- Repositórios privados têm limite de minutos gratuitos por mês;
- Workflows complexos podem demorar para executar;
- Depende da infraestrutura do GitHub (indisponível se o GitHub cair);
- A curva de aprendizado do YAML pode ser um obstáculo inicial.
