# Reporte — Iteración 6: While y bloques de sentencias

## Qué se implementó

- Sentencia `while <cond> do <stmt>`: evalúa la condición antes de cada iteración y salta al final del ciclo si es falsa.
- Sentencia de bloque `{ stmt* }`: agrupa cero o más sentencias sin introducir nuevo ámbito de variables.
- Soporte de anidación arbitraria de `while` y bloques dentro de `if`/`while`.

## Decisiones técnicas

**Buffer por frame (`_CtrlFrame`).**  
Al entrar a un `while`, se crea un `_CtrlFrame` con `kind='while'` y se redirige `self._text` al buffer `cond_buf`. El ANTLR listener acumula las instrucciones de la condición ahí. Cuando detecta el primer hijo-sentencia directo del `while` en `enterEveryRule`, hace pop del valor de condición del stack, lo guarda en `frame.cond_reg`, y redirige `self._text` a `then_buf`. Al salir del nodo (`exitWhileStmt`), ensambla:

```
_while_start_N:
    <cond_buf>
    beq <cond_reg>, $zero, _while_end_N
    <then_buf>
    j _while_start_N
_while_end_N:
```

**Pila de frames y buffers (`_frames`, `_buf_stack`).**  
Para anidación, cada `while` e `if` empuja el buffer activo en `_buf_stack` y al salir lo restaura. Así los buffers del ciclo interior quedan dentro del `then_buf` del ciclo exterior.

**Reset de registro por sentencia.**  
`enterPrintStmt` y `enterAssignStmt` resetean `self._reg = 0`. Dentro de un bloque cada sentencia reutiliza $t0–$t9, evitando agotarlos.

**Bloque vacío.**  
`exitBlockStmt` es `pass`; si no hay sentencias internas, `then_buf` queda vacío y el bucle/if simplemente no emite instrucciones de cuerpo.

**Condición inicialmente falsa.**  
El `beq` al inicio del cuerpo garantiza que si la condición es falsa desde la primera iteración, el cuerpo nunca se ejecuta.

## Pruebas que pasan

| Archivo | Entrada / condición | Salida esperada |
|---|---|---|
| `18_while_basic.rara` | `x=1`, ciclo `while x < 4` | 1, 2, 3 |
| `19_while_false.rara` | `x=10`, `while x < 5` | (nada) |
| `20_while_nested.rara` | `i` de 1–2, `j` de 1–2 | 1 1 1 2 2 1 2 2 |
| `21_empty_block.rara` | `if x > 0 then {}`, luego `print x` | 5 |
| `22_while_if.rara` | `x` de 1–3, imprime solo si `x == 2` | 2 |
| `23_triple_while.rara` | Triple while anidado, imprime `k` | 1 2 1 2 1 2 1 2 |

## Limitaciones conocidas

- No hay `break` ni `continue`; el único mecanismo de salida del ciclo es la condición.
- La condición del `while` sólo acepta expresiones que dejan un valor en el stack; no hay cortocircuito lógico (`&&`, `||`).
- Los registros $t0–$t9 se reutilizan por sentencia; expresiones muy complejas (> 10 temporales) dentro de un solo `print`/`<--` aún podrían desbordarse.

---

Revisado por Leonardo Lopez Vidal. Correcciones: el reporte omitió las pruebas 18, 19 y 20 en la sección de pruebas que pasan — las agregué manualmente.
