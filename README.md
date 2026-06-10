# trabalho-DevOps
# 🤖 Exploradores DevOps – GitHub Actions na Prática

Projeto acadêmico desenvolvido para a disciplina de DevOps.  
**Tecnologia explorada:** GitHub Actions  
**Grupo:** _(Arthur Mota, Filippe, Isadora, Rebeca Alencar)_

---

## 📌 O que é GitHub Actions?

GitHub Actions é uma plataforma de **integração contínua e entrega contínua (CI/CD)** integrada ao próprio GitHub. Ela permite automatizar tarefas do desenvolvimento de software diretamente no repositório, sem precisar de ferramentas externas.

Com o GitHub Actions, sempre que um desenvolvedor envia código novo (via `push`), o GitHub pode automaticamente:

- Rodar testes para verificar se o código está funcionando
- Verificar a qualidade do código
- Compilar o projeto
- Fazer deploy em servidores

Tudo isso sem intervenção humana — é o conceito de **automação de pipeline**.

---

## 🎯 Objetivo da Demonstração

Este projeto demonstra o uso do GitHub Actions para **executar testes automáticos** em um pequeno programa Python (uma calculadora) sempre que novo código é enviado ao repositório.

A ideia central é mostrar na prática o conceito de **CI (Integração Contínua):** qualquer alteração no código é automaticamente testada, e o resultado fica visível para todo o time.

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

O arquivo `.github/workflows/rodar-python.yml` define o fluxo de automação. Veja o que cada parte faz:

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

1. O GitHub detecta que novo código foi enviado
2. Sobe uma máquina virtual Ubuntu do zero
3. Baixa o código do repositório para essa máquina
4. Instala o Python 3.11
5. Instala o pytest
6. Roda os testes da calculadora
7. Exibe ✅ (passou) ou ❌ (falhou) para cada teste
8. Desliga a máquina virtual

---

## 🧪 O que é pytest e como os testes funcionam

**pytest** é uma ferramenta Python que automatiza a verificação do código. Em vez de testar manualmente cada função, você escreve um arquivo de testes uma vez e o pytest verifica tudo em segundos.

A palavra-chave principal é o `assert` ("afirmo que"):

```python
assert somar(2, 3) == 5   # afirmo que somar 2 e 3 deve retornar 5
```

Se a afirmação for verdadeira → teste passa ✅  
Se for falsa → teste falha ❌ e o GitHub Actions notifica o time

### Testes implementados

| Teste | O que verifica |
|---|---|
| `test_somar` | Se a soma retorna o valor correto |
| `test_subtrair` | Se a subtração retorna o valor correto |
| `test_multiplicar` | Se a multiplicação retorna o valor correto |
| `test_dividir` | Se a divisão retorna o valor correto |
| `test_dividir_por_zero` | Se o código lança erro ao tentar dividir por zero |

---

## ▶️ Como reproduzir a demonstração

**Pré-requisitos:** ter uma conta no GitHub (sem necessidade de instalar nada localmente).

1. Faça um fork deste repositório
2. Acesse o repositório forkado
3. Edite qualquer arquivo (por exemplo, adicione um comentário em `calculadora.py`)
4. Faça o commit da alteração
5. Vá para a aba **Actions** do repositório
6. Veja o workflow rodar automaticamente e os testes passando

Para simular um erro: altere uma função da calculadora com um valor errado (ex: `return a + b + 1`) e observe o workflow acusar a falha em vermelho.

---

## ✅ Vantagens do GitHub Actions

- **Integrado ao GitHub:** não precisa configurar ferramentas externas
- **Gratuito para repositórios públicos**
- **Feedback imediato:** o time sabe em segundos se o código quebrou algo
- **Reproduzível:** cada execução roda em um ambiente limpo e idêntico
- **Marketplace de actions:** milhares de automações prontas para usar

## ⚠️ Limitações

- Repositórios privados têm limite de minutos gratuitos por mês
- Workflows complexos podem demorar para executar
- Depende da infraestrutura do GitHub (indisponível se o GitHub cair)
- A curva de aprendizado do YAML pode ser um obstáculo inicial

---

## 📚 Referências

- [Documentação oficial do GitHub Actions (PT-BR)](https://docs.github.com/pt/actions)
- [Documentação do pytest](https://docs.pytest.org/)
- [Guia rápido do GitHub Actions](https://docs.github.com/pt/actions/get-started/quickstart)
