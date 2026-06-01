# Iteración 5 — Control de flujo

## ¿Qué hace el compilador ahora que no hacía antes?
El compilador puede tomar decisiones en tiempo de ejecución: evalúa una condición y ejecuta un bloque de código solo si el resultado es distinto de cero. Antes todos los programas eran lineales; ahora pueden tener ramas con `if/then` y `if/then/else`, incluyendo ifs anidados donde el `else` pertenece al `if` más cercano. Los comparadores (`==`, `!=`, `<`, `>`) producen 1 o 0 y pueden usarse como valores en expresiones aritméticas.

## ¿Qué se agregó a la gramática?
Se añadieron las palabras clave `if`, `then` y `else`. Se añadieron cuatro operadores de comparación: igual (`==`), distinto (`!=`), menor que (`<`) y mayor que (`>`). Una comparación entre dos expresiones es en sí misma una expresión que produce 1 si es verdadera y 0 si es falsa, con menor precedencia que todos los operadores aritméticos. Se añadió la sentencia `if expresión then sentencia` con el bloque `else sentencia` opcional; cada rama acepta exactamente una sentencia (no un bloque con varias líneas — eso viene en It6).

## ¿Qué métodos del Listener se implementaron?
- **exitCompare** — saca dos operandos de la pila; emite `seq`, `sne`, `slt` o `slt` con operandos invertidos para `>` (a > b ≡ b < a); deja 0 o 1 en el registro resultado
- **enterIfStmt** — crea un `_CtrlFrame` con tres buffers vacíos (cond/then/else), empuja el buffer activo a una pila, y redirige `self._text` al buffer de condición
- **enterEveryRule** — detecta cuándo el nodo que está por entrar es un stmt directo del ifStmt; en la primera transición (cond→then) guarda el registro de la condición y redirige al buffer then; en la segunda (then→else) marca `has_else = True` y redirige al buffer else
- **exitIfStmt** — restaura el buffer padre, vuelca el buffer cond, emite el `beq` de salto, vuelca then, y si hay else emite el `j` al fin, la etiqueta else, el buffer else, y finalmente la etiqueta de fin

La clase auxiliar **`_CtrlFrame`** no es un método del Listener pero es el mecanismo central: almacena los tres buffers, el registro de la condición, la fase actual y si hay else, permitiendo que ifs anidados funcionen correctamente mediante una pila de frames.

## ¿Qué decisión técnica tomaste que no estaba explícita en la especificación?
La especificación describe el mecanismo de buffers pero no explica cómo detectar la transición de la condición al then cuando la condición puede tener cualquier profundidad arbitraria. Se decidió usar `ctx.parentCtx is frame.ctx` en `enterEveryRule` para filtrar únicamente los hijos DIRECTOS del nodo `ifStmt` dueño del frame actual, ignorando cualquier nodo a mayor profundidad. Esto garantiza que expresiones complejas dentro de la condición (como `(x + 2) > y`) no disparen la transición por accidente, y que ifs anidados en el cuerpo del then no interfieran con el frame del if exterior.

## Pruebas que pasan
| Archivo | Output en spim |
|---|---|
| 13_if_comparators.rara | 1, 1, 1, 1 |
| 14_if_else.rara | 10, 0 |
| 15_if_nested.rara | 5, 99 |
| 16_if_false.rara | (nada — condición falsa sin else) |
| 17_if_nested2.rara | 7 |

## Limitaciones conocidas
- Cada rama del if acepta exactamente una sentencia — no es posible escribir múltiples líneas en un then o else sin bloques `{ }`, que se agregan en It6
- No hay verificación de tipos: una comparación entre un string y un entero pasa la gramática y genera MIPS inválido silenciosamente
- El dangling else se resuelve al if más cercano (comportamiento estándar), pero no hay ningún mensaje de advertencia cuando la indentación visual sugiere lo contrario
- Las etiquetas de salto usan un contador global (`_if_end_0`, `_if_end_1`…); si se compilan múltiples programas con la misma instancia del listener, los contadores no se resetean — aunque en la práctica `main.py` crea una instancia nueva por archivo

---
*Revisado por Leonardo Lopez Vidal. Correcciones: ninguna, verifiqué que `ctx.parentCtx is frame.ctx` está en `enterEveryRule` del código, la decisión técnica es real. Las pruebas coinciden con lo que imprimió spim.*
