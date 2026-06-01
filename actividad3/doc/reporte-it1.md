# Iteración 1 — Literales y print

## ¿Qué hace el compilador ahora que no hacía antes?
El compilador puede tomar un programa RaraLang con instrucciones print y convertirlo en un archivo .asm válido para QtSPIM. Antes de esta iteración, MIPSListener.py era una clase vacía que no generaba nada. Ahora puede manejar tres tipos de valores imprimibles: enteros decimales, números en cualquier base (binario, octal, hexadecimal) y cadenas de texto.

## ¿Qué se agregó a la gramática?
La gramática ya venía con los tokens necesarios para esta iteración, no hubo que modificarla. Reconoce la instrucción print seguida de una expresión, y como expresión acepta tres formas: un entero decimal, un número en otra base con el formato [dígitos:base], y una cadena de texto delimitada por comillas dobles. También ignora comentarios que empiezan con # y espacios en blanco.

## ¿Qué métodos del Listener se implementaron?
- **exitInt** — lee el token INT, reserva un registro $t_n y emite `li $t_n, valor`
- **exitBased** — extrae dígitos y base del token [dígitos:base], convierte a decimal con `int(digits, base)` y emite el mismo `li` que un entero normal
- **exitString** — crea una etiqueta `_str_n` en `.data` con `.asciiz` y guarda la etiqueta en la pila
- **exitPrintStmt** — saca el valor de la pila; si es entero emite `move $a0` + syscall 1; si es string emite `la $a0` + syscall 4. En ambos casos agrega syscall 11 con ASCII 10 para nueva línea
- **output()** — ensambla el archivo final: sección `.data` (solo si hay strings), `.text`, etiqueta `main:`, el código acumulado, y syscall 10 al final

## ¿Qué decisión técnica tomaste que no estaba explícita en la especificación?
La especificación no indica si cada print debe terminar con nueva línea. Se decidió siempre emitir syscall 11 con `\n` (ASCII 10) después de cada print. La alternativa habría sido no agregarla, pero todos los valores se imprimirían pegados en la misma línea.

También se decidió asignar registros temporales en orden ascendente ($t0, $t1...) sin reutilizarlos. Funciona para It 1 pero tendrá que revisarse en iteraciones con expresiones compuestas.

## Pruebas que pasan
| Archivo | Output en spim |
|---|---|
| 01_int_literal.rara | 5, 1000 |
| 02_based_numbers.rara | 255, 255, 255 |
| 03_strings.rara | hola mundo, RaraLang, iteracion 1 |

## Limitaciones conocidas
- `[29:2]` no produce error visible — el compilador atrapa la excepción silenciosamente y genera un .asm que no imprime nada
- Los registros temporales nunca se liberan; con muchos print se agotarían $t0–$t9
- Sin validación de sintaxis propia — los errores vienen directamente de ANTLR sin formato amigable

---
*Revisado por Leonardo Lopez Vidal. Correcciones: el reporte decía que [29:2] lanza una excepción no manejada, pero revisando el código de exitBased confirmé que no hay ningún try/except — la excepción sube a Python y se muestra en terminal, pero el .asm generado queda vacío. Esto explica lo que vi al correrlo en spim: no hubo output ni error visible desde spim, el error fue antes en el compilador.*
