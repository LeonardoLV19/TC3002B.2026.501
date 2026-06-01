from antlr.RaraLangListener import RaraLangListener
from antlr.RaraLangParser import RaraLangParser


class MIPSListener(RaraLangListener):

    def __init__(self):
        self._data = []      # líneas de la sección .data
        self._text = []      # líneas del cuerpo de main
        self._stack = []     # pila: tuplas (tipo, valor)  tipo = "int" | "str"
        self._reg = 0        # contador de registros $t
        self._str_n = 0      # contador de etiquetas de string

    # ── helpers ──────────────────────────────────────────────────────────────

    def _reg_next(self):
        r = f"$t{self._reg}"
        self._reg += 1
        return r

    def _str_label(self):
        label = f"_str{self._str_n}"
        self._str_n += 1
        return label

    # ── expresiones ──────────────────────────────────────────────────────────

    def exitInt(self, ctx: RaraLangParser.IntContext):
        reg = self._reg_next()
        self._text.append(f"    li {reg}, {ctx.INT().getText()}")
        self._stack.append(("int", reg))

    def exitBased(self, ctx: RaraLangParser.BasedContext):
        # token tiene la forma [dígitos:base]
        token = ctx.BASED_NUMBER().getText()[1:-1]   # quita corchetes
        digits, base = token.rsplit(":", 1)
        value = int(digits, int(base))
        reg = self._reg_next()
        self._text.append(f"    li {reg}, {value}")
        self._stack.append(("int", reg))

    def exitString(self, ctx: RaraLangParser.StringContext):
        raw = ctx.STRING().getText()   # incluye las comillas
        label = self._str_label()
        self._data.append(f"{label}: .asciiz {raw}")
        self._stack.append(("str", label))

    # ── sentencias ───────────────────────────────────────────────────────────

    def exitPrintStmt(self, ctx: RaraLangParser.PrintStmtContext):
        kind, val = self._stack.pop()
        if kind == "int":
            self._text += [
                f"    move $a0, {val}",
                f"    li $v0, 1",       # print_int
                f"    syscall",
            ]
        else:                            # str
            self._text += [
                f"    la $a0, {val}",
                f"    li $v0, 4",       # print_string
                f"    syscall",
            ]
        # nueva línea después de cada print
        self._text += [
            f"    li $a0, 10",
            f"    li $v0, 11",          # print_char
            f"    syscall",
        ]

    # ── salida ───────────────────────────────────────────────────────────────

    def output(self) -> str:
        lines = []
        if self._data:
            lines.append(".data")
            lines.extend(self._data)
            lines.append("")
        lines.append(".text")
        lines.append("main:")
        lines.extend(self._text)
        lines.append("    li $v0, 10")  # exit
        lines.append("    syscall")
        return "\n".join(lines) + "\n"
