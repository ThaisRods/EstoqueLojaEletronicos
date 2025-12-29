# Sistema de Controle de Estoque – Loja de Eletrônicos

## Descrição do Projeto

Este projeto consiste em um **Sistema de Controle de Estoque desenvolvido em Python**, voltado para o gerenciamento de produtos de uma loja de eletrônicos por meio de uma interface em **terminal (CLI)**.

O sistema possibilita o controle eficiente de itens em estoque, permitindo **cadastro, atualização, exclusão e consulta de produtos**, garantindo validações básicas para evitar inconsistências nos dados.

---

## Funcionalidades

* **Cadastro de produtos**

  * Nome do produto
  * Preço unitário
  * Quantidade em estoque
  * Especificações técnicas

* **Atualização de produtos**

  * Alteração de quantidade
  * Alteração de preço

* **Exclusão de produtos**

  * Confirmação antes da remoção

* **Visualização do estoque**

  * Listagem completa de todos os produtos cadastrados

* **Consulta individual**

  * Visualização detalhada de um produto específico

* **Menu interativo**

  * Navegação simples e intuitiva via terminal

---

## 🗂️ Estrutura de Dados

Os dados são armazenados em memória utilizando **dicionários Python**, estruturados da seguinte forma:

```text
{
  "Nome do Produto": {
      "preco": float,
      "qtd": int,
      "detalhes": string
  }
}
```

Essa abordagem facilita o acesso rápido, a manutenção e a escalabilidade do sistema.

---

## Execução do Projeto

### Requisitos

* Python 3.x

### Como executar

1. Clone ou faça o download do projeto
2. Acesse o diretório do projeto via terminal
3. Execute o arquivo principal:

```bash
python main.py
```
4. Utilize o menu exibido para interagir com o sistema

---

## Validações Implementadas

* Prevenção de cadastro de produtos duplicados
* Validação de entradas numéricas
* Bloqueio de valores negativos para preço e quantidade
* Tratamento de erros para entradas inválidas do usuário

---

## Objetivo

O objetivo deste projeto é demonstrar, de forma prática, o uso de:

* Estruturas de dados (dicionários)
* Funções
* Estruturas de controle
* Tratamento de exceções
* Boas práticas iniciais de organização de código em Python

Este sistema pode servir como **base para aplicações mais complexas**, como sistemas com persistência em banco de dados ou interfaces gráficas.

---

## Possíveis Evoluções

* Persistência de dados em arquivos (JSON ou CSV)
* Integração com banco de dados
* Cálculo automático do valor total do estoque
* Implementação de interface gráfica
* Sistema de autenticação de usuários

---

## Desenvolvedora

**Thais Rodrigues**
Dezembro de 2025
