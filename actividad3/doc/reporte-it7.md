# Reporte — Iteración 7: Declaración y llamada a funciones

## ¿Qué hace el compilador ahora que no hacía antes?

El compilador acepta declaraciones de función con parámetros y un cuerpo de sentencias, sentencias `return` dentro del cuerpo, y llamadas a función como expresiones en cualquier posición aritmética o de `print`. Ahora se pueden compilar programas que definen subrutinas reutilizables, las llaman con argumentos y usan el valor retornado directamente en expresiones.

## ¿Qué se agregó a la gramática?

Se añadieron dos tokens nuevos: `func` (marca el inicio de una declaración de función) y `return` (termina la función y entrega un valor). La regla de programa ahora acepta declaraciones de función intercaladas con sentencias ordinarias en el nivel superior. Una declaración de función lleva nombre, una lista opcional de parámetros separados por comas entre paréntesis, y un bloque de sentencias entre llaves. La sentencia `return` acepta cualquier expresión. Las llamadas a función son una nueva alternativa de expresión: un identificador seguido de una lista de argumentos entre paréntesis; al ser expresiones, pueden aparecer dentro de otras operaciones aritméticas o comparaciones.

## ¿Qué métodos del Listener se implementaron?

- `enterFuncDecl`: emite la etiqueta de la función y genera instrucciones `sw` para almacenar cada argumento ($a0, $a1, …) en su variable de parámetro en `.data`; redirige `self._text` al buffer de la función.
- `exitFuncDecl`: cierra el cuerpo con `jr $ra`, guarda el buffer completo en `_func_bufs` y restaura `self._text` al buffer anterior.
- `enterReturnStmt`: resetea el contador de registros a 0 para que la expresión de retorno empiece desde `$t0`.
- `exitReturnStmt`: hace pop del valor de la expresión, lo mueve a `$v0` con `move`, y emite `jr $ra`.
- `exitCall`: hace pop de los argumentos del stack (en orden inverso, luego los invierte), los mueve a `$a0`–`$a3`, guarda `$ra` en la pila antes del `jal`, ejecuta `jal nombre`, restaura `$ra` de la pila, mueve `$v0` a un registro temporal y lo empuja al stack de expresiones.

## ¿Qué decisión técnica tomaste que no estaba explícita en la especificación?

La especificación dice que hay que guardar `$ra` antes de llamadas internas, pero no especifica en qué casos. Se eligió guardar y restaurar `$ra` en **todas** las llamadas (`exitCall`), incluso las que provienen de `main`. Esto tiene un costo mínimo (2 instrucciones extra siempre) pero elimina el caso especial: no hay que saber en tiempo de compilación si el llamador es `main` o una función. La alternativa habría sido guardar `$ra` solo dentro de bloques `funcDecl`, pero eso habría requerido rastrear explícitamente si `self._text` apunta a un buffer de función, añadiendo estado y complejidad sin beneficio observable.

## Pruebas que pasan

| Archivo | Descripción | Salida esperada |
|---|---|---|
| `24_func_one_param.rara` | Función con un parámetro — `doble(5)` | 10 |
| `25_func_two_params.rara` | Función con dos parámetros — `suma(3, 4)` | 7 |
| `26_func_called_twice.rara` | Misma función llamada dos veces — `doble(3)`, `doble(7)` | 6, 14 |
| `27_func_calls_func.rara` | Función que llama a otra — `doble(5)` → `suma(5, 5)` | 10 |
| `28_func_in_expr.rara` | Resultado de función en expresión — `doble(3) + 1` | 7 |

## Limitaciones conocidas

- Recursión no funciona: `cuenta(1)` produce "Can't expand stack segment" en SPIM — los parámetros se guardan en `.data` y cada llamada recursiva sobreescribe los de la anterior, además de que `$ra` apunta siempre a la misma dirección de retorno sin profundidad de pila real.
- Argumentos de más se ignoran silenciosamente: `doble(5, 99)` da 10 sin error.
- Argumentos de menos no se detectan: el compilador no verifica que se pasen todos los parámetros que la función espera; los `$a`-registros faltantes tendrán basura.
- Cada función termina con dos `jr $ra`: uno de `exitReturnStmt` y uno de `exitFuncDecl` — es código muerto pero inofensivo en SPIM.
- Los nombres de parámetros son globales en `.data`: si dos funciones usan el mismo nombre de parámetro (por ejemplo, ambas declaran `x`), comparten la misma celda de memoria y una llamada puede corromper el estado de la otra.

---

Revisado por Leonardo Lopez Vidal. Correcciones: la limitación de recursión decía "comportamiento incorrecto" pero al probarlo con `cuenta(1)` el síntoma real fue stack overflow en SPIM  "Can't expand stack segment". También noté que el modelo detectó una limitación adicional que yo no había probado: dos funciones con el mismo nombre de parámetro comparten celda de memoria en `.data`.
leonardo@MacBook-Pro-de-Leonardo-3 tests % spim 30_recursion.asm 
Loaded: /opt/homebrew/Cellar/spim/9.1.24/share/exceptions.s
Can't expand stack segment by 8 bytes to 524288 bytes.
Use -lstack # with # > 524288
