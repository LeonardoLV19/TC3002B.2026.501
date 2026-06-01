# Iteración 3 — Aritmética

## ¿Qué hace el compilador ahora que no hacía antes?
El compilador puede evaluar expresiones aritméticas compuestas y usar su resultado en un `print` o en una asignación. Antes solo podía manejar valores simples (literales o variables); ahora puede procesar expresiones como `x + y`, `(x + 2) × (y - 1)` o cualquier combinación de suma, resta, multiplicación y división. La precedencia de operadores está incorporada en la gramática: `×` y `÷` siempre evalúan antes que `+` y `-`, y los paréntesis pueden cambiar ese orden.

## ¿Qué se agregó a la gramática?
Se agregaron cuatro tokens para los operadores: `+`, `-`, el símbolo tipográfico `×` (no el asterisco), y el símbolo tipográfico `÷` (no la diagonal). Se añadieron dos nuevas formas de expresión binaria: una para multiplicación y división, y otra para suma y resta. El hecho de que la forma `×`/`÷` aparezca antes en la regla de expresión le da mayor precedencia sobre `+`/`-`. También se añadió la forma de expresión con paréntesis `( expr )`, que no genera ninguna instrucción extra sino que solo controla el orden en que el árbol es recorrido.

## ¿Qué métodos del Listener se implementaron?
- **enterPrintStmt** — resetea el contador de registros temporales a `$t0` al inicio de cada sentencia print
- **enterAssignStmt** — resetea el contador de registros temporales a `$t0` al inicio de cada asignación
- **exitMulDiv** — saca dos operandos de la pila; si el operador es `×` emite `mult` + `mflo`; si es `÷` emite `div` + `mflo`; reutiliza el registro del operando izquierdo para el resultado
- **exitAddSub** — saca dos operandos de la pila; emite `add` o `sub` según el operador; reutiliza el registro del operando izquierdo para el resultado

`exitParen` no se implementó porque no hace nada: cuando el nodo paren termina, el resultado de la subexpresión interior ya está en la pila.

## ¿Qué decisión técnica tomaste que no estaba explícita en la especificación?
La especificación no dice nada sobre cómo gestionar los registros temporales cuando hay múltiples sentencias. Sin ningún mecanismo de reciclaje, un programa con seis sentencias de aritmética usaría `$t10`, `$t11`... que no existen en MIPS (solo hay `$t0`–`$t9`). Se decidió resetear el contador de registros a `$t0` al entrar en cada sentencia (`enterPrintStmt`, `enterAssignStmt`), aprovechando que los temporales de una sentencia ya no se necesitan en la siguiente — los valores permanentes están en `.data` y los resultados ya fueron impresos o almacenados. También se decidió reutilizar el registro del operando izquierdo como destino del resultado en todas las operaciones binarias, lo que reduce el número de registros necesarios por expresión.

## Pruebas que pasan
| Archivo | Output en spim |
|---|---|
| 07_arithmetic_ops.rara | 13, 7, 30, 3 |
| 08_precedence.rara | 14, 20 |
| 09_arithmetic_vars.rara | 13, 7, 30, 3, 24 |

## Limitaciones conocidas
- División entre cero: `print 10 ÷ 0` imprime 0 sin error — SPIM ejecuta `div` con divisor 0 silenciosamente y `mflo` devuelve 0
- El residuo de la división siempre se pierde — el compilador usa `mflo` pero nunca `mfhi`
- Desbordamiento en multiplicación: si el producto no cabe en 32 bits, `mflo` devuelve solo los bits bajos sin ninguna advertencia
- Una expresión aritmética muy profunda dentro de una sola sentencia podría agotar `$t0`–`$t9`; el reseteo por sentencia resuelve el problema entre sentencias pero no dentro de una sola expresión con más de 10 operandos anidados

---
*Revisado por Leonardo Lopez Vidal. Correcciones: ninguna — las decisiones técnicas están en el código y las limitaciones coinciden con lo probado.*
