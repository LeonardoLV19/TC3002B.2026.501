# Iteración 4 — Operadores Unicode

## ¿Qué hace el compilador ahora que no hacía antes?
El compilador entiende cuatro operadores adicionales escritos con símbolos tipográficos: módulo (`⊞`), doble más (`⊠`), promedio entero (`≈`) y negación unaria (`±`). Antes era imposible escribir `print 10 ⊞ 3` o `print ±8`; ahora estos programas compilan y producen el código MIPS correcto. El operador `≈` usa desplazamiento aritmético en lugar de división entera para garantizar redondeo hacia menos infinito también con números negativos.

## ¿Qué se agregó a la gramática?
Se añadieron cuatro tokens nuevos para los símbolos Unicode. Los tres binarios (`⊞`, `⊠`, `≈`) se integraron en las reglas de expresión ya existentes: `⊞` y `⊠` se agregaron al grupo de mayor precedencia junto con `×` y `÷`, mientras que `≈` se agregó al grupo de menor precedencia junto con `+` y `-`. El operador unario `±` se agregó como una alternativa de prefijo de la forma `± expr`, posicionada después de los grupos binarios en la regla.

## ¿Qué métodos del Listener se implementaron?
- **exitMulDiv** (extendido) — ahora maneja también `⊞`: emite `div`+`mfhi` para tomar el residuo; y `⊠`: emite `sll left, left, 1` seguido de `add` para calcular `2a + b`
- **exitAddSub** (extendido) — ahora maneja también `≈`: emite `add` seguido de `sra left, left, 1` para dividir por 2 con redondeo hacia menos infinito
- **exitNeg** — nuevo: saca el valor de la pila y emite `sub val, $zero, val` para negar

## ¿Qué decisión técnica tomaste que no estaba explícita en la especificación?
La especificación no dice dónde colocar los nuevos operadores en la jerarquía de precedencia respecto a los que ya existían. Se decidió que `⊞` y `⊠` comparten nivel con `×` y `÷` porque son operaciones de tipo multiplicativo (módulo involucra división, doble más involucra multiplicación por 2). `≈` comparte nivel con `+` y `-` porque involucra una suma. Para `±`, al ser unario, se colocó después de los grupos binarios, lo que tiene una consecuencia no obvia: en la expresión `±3 ≈ ±1`, el `±` externo envuelve toda la subexpresión `3 ≈ ±1` en lugar de aplicarse solo al `3` — esto produce un resultado distinto al esperado intuitivamente (ver limitaciones).

## Pruebas que pasan
| Archivo | Output en spim |
|---|---|
| 10_unicode_basic.rara | 1, 13, 5, -8 |
| 11_avg_negative.rara | -2, -3 |
| 12_double_neg.rara | 5, 8 |

## Limitaciones conocidas
- Bug encontrado: `print ±3 ≈ ±1` genera `li $t0, 3` y `li $t1, 1` en lugar de -3 y -1. El operador `±` no se aplica antes de `≈` porque en la gramática `±` tiene menor precedencia que los operadores binarios, por lo que `±3 ≈ ±1` se parsea como `±(3 ≈ ±1)` y no como `(±3) ≈ (±1)`. El resultado es 2 en lugar de -2. Bug documentado pero no corregido.
- Módulo con divisor cero: igual que en `÷`, `⊞` no detecta división por cero — SPIM ejecuta `div` silenciosamente y `mfhi` devuelve 0.
- `⊠` no está definido para strings ni para valores mayores a 2^30 — el `sll` puede producir desbordamiento sin aviso.

---
*Revisado por Leonardo Lopez Vidal. Correcciones: la explicación del bug de `±3 ≈ ±1` es que no es que se pierdan los signos, sino que la gramática parsea `±3 ≈ ±1` como `±(3 ≈ ±1)` por precedencia. El resultado 2 es correcto para esa interpretación, pero no para la intuitiva.*
