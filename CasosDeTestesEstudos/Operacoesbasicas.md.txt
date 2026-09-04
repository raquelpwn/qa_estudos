# Caso de Teste — Calculadora de Operações Básicas

## Objetivo

Verificar se a calculadora realiza corretamente as operações de soma, subtração, multiplicação e divisão.

---

## CT-001 — Divisão por zero

**Descrição:**
Verificar o comportamento do sistema ao tentar realizar uma divisão por zero.

**Pré-condição:**
O programa deve estar em execução.

**Passos para reprodução:**

1. Informar um número no primeiro campo.
2. Informar `0` no segundo campo.
3. Selecionar a opção `4 - Divisão`.

**Dados de teste:**

* Número 1: `10`
* Número 2: `0`
* Operação: `4`

**Resultado esperado:**
O sistema deve informar que não é possível realizar uma divisão por zero, sem apresentar um erro inesperado.

**Resultado atual:**
O programa apresenta um erro ao tentar realizar a divisão por zero.

**Status:** 🔴 Falhou


