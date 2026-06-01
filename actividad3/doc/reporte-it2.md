# Iteración 2 — Variables

## ¿Qué hace el compilador ahora que no hacía antes?
El compilador puede guardar valores en variables con nombre y recuperarlos después. Antes solo podía imprimir literales directamente; ahora puede procesar sentencias como `x <-- 10` y luego `print x`, generando el código MIPS correspondiente para almacenar y cargar desde memoria. Esto permite escribir programas que reutilizan valores sin repetir literales.

## ¿Qué se agregó a la gramática?
Se agregaron tres cosas. Primero, un token para nombres de variable: cualquier secuencia que empiece con letra o guión bajo seguida de letras, dígitos o guiones bajos. Segundo, un token para el operador de asignación `<--`. Tercero, una nueva forma de sentencia `nombre <-- expresión` que guarda el resultado de una expresión en una variable. También se agregó el nombre de variable como una forma válida de expresión, lo que permite leer su valor en cualquier lugar donde antes solo cabían literales.

## ¿Qué métodos del Listener se implementaron?
- **exitVar** — lee el nombre de la variable, carga su valor desde memoria con `lw` a un nuevo registro temporal, y hace push a la pila
- **exitAssignStmt** — hace pop del valor calculado por la expresión y lo almacena en la dirección de la variable con `sw`

También se agregó el helper interno **`_var_label(name)`** que la primera vez que ve un nombre de variable lo registra en `.data` como `_var_nombre: .word 0`, y en llamadas siguientes devuelve la etiqueta ya existente.

## ¿Qué decisión técnica tomaste que no estaba explícita en la especificación?
La especificación no menciona qué pasa si una variable en RaraLang tiene el mismo nombre que una instrucción o directiva de MIPS (`add`, `sub`, `div`, `.data`, etc.). Se decidió agregar el prefijo `_var_` a todas las etiquetas de variables en el `.asm` generado — por ejemplo, la variable `add` se convierte en la etiqueta `_var_add`. Esto evita que el ensamblador de SPIM interprete la etiqueta como parte de una instrucción. La alternativa habría sido mantener el nombre original y confiar en que SPIM lo maneja bien, pero el test `06_var_mips_name.rara` confirma que el prefijo es necesario para que `add`, `sub` y `div` funcionen sin error.

## Pruebas que pasan
| Archivo | Output en spim |
|---|---|
| 04_var_basic.rara | 10, 3 |
| 05_var_reassign.rara | 5, 20 |
| 06_var_mips_name.rara | 7, 4, 2 |

## Limitaciones conocidas
- Leer una variable sin haberla asignado no produce error — el compilador crea la entrada en `.data` con `.word 0` y el programa imprime 0 silenciosamente. Esto podría enmascarar bugs en programas más grandes.
- Solo se pueden guardar enteros en variables. Asignar un string (`x <-- "hola"`) genera MIPS con `sw` sobre una etiqueta de `.asciiz`, lo cual produce un comportamiento incorrecto en SPIM sin ninguna advertencia del compilador.
- Los registros temporales siguen sin reutilizarse. En un programa con muchas asignaciones y lecturas se puede agotar el rango `$t0`–`$t9`. Esto tendrá que resolverse en la iteración de aritmética donde ya se necesita composición de expresiones.

---
*Revisado por Leonardo Lopez Vidal. Correcciones: el reporte dice que leer una variable sin asignar imprime 0 silenciosamente, pero al probarlo con `print x` el compilador generó un `.asm` malformado con `sw _str0, _var_echo` que spim rechazó con error de sintaxis no imprime 0, genera código inválido.*
