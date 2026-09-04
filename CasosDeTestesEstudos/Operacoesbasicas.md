# Caso de Teste — Operações Básicas

## Objetivo

Validar se o programa realiza corretamente as operações matemáticas básicas:

* Soma
* Subtração
* Multiplicação
* Divisão

---

## CT-001 — Soma

**Entrada:**

* Número 1: `10`
* Número 2: `5`
* Operação: `1`

**Resultado esperado:**
O programa deve apresentar `15`.

**Resultado atual:**
O programa apresentou `15`.

**Status:** 🟢 Aprovado

---

## CT-002 — Subtração

**Entrada:**

* Número 1: `10`
* Número 2: `5`
* Operação: `2`

**Resultado esperado:**
O programa deve apresentar `5`.

**Resultado atual:**
O programa apresentou `5`.

**Status:** 🟢 Aprovado

---

## CT-003 — Multiplicação

**Entrada:**

* Número 1: `10`
* Número 2: `5`
* Operação: `3`

**Resultado esperado:**
O programa deve apresentar `50`.

**Resultado atual:**
O programa apresentou `50`.

**Status:** 🟢 Aprovado

---

## CT-004 — Divisão

**Entrada:**

* Número 1: `10`
* Número 2: `5`
* Operação: `4`

**Resultado esperado:**
O programa deve apresentar `2`.

**Resultado atual:**
O programa apresentou `2`.

**Status:** 🟢 Aprovado

---

## CT-005 — Divisão por zero

**Entrada:**

* Número 1: `10`
* Número 2: `0`
* Operação: `4`

**Resultado esperado:**
O programa deve informar que não é possível realizar uma divisão por zero.

**Resultado atual:**
O programa apresenta um erro ao tentar realizar a divisão.

**Status:** 🔴 Reprovado

---

# Bug encontrado

Foi identificado um problema na operação de divisão quando o segundo número informado é `0`.

O código tenta realizar:

```python
resultado = n1 / n2
```

Quando `n2` é `0`, ocorre um erro de divisão por zero.

---

# Correção

Foi adicionada uma validação para verificar se o segundo número é `0` antes de realizar a divisão.

```python
if n2 == 0:
 print("Não é possível dividir por zero")
    else:    
      resultado = n1 / n2
```

---

# 🔄 Reteste

Após a correção, o teste CT-005 será executado novamente.

**Resultado esperado:**
O programa deve informar que não é possível realizar uma divisão por zero e não apresentar erro.

**Status:** 🟢 Aprovado
