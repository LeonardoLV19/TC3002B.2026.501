from antlr.RaraLangListener import RaraLangListener
from antlr.RaraLangParser import RaraLangParser


class MIPSListener(RaraLangListener):

    def __init__(self):
        self._data = []      # líneas de la sección .data
        self._text = []      # líneas del cuerpo de main
        self._stack = []     # pila: tuplas (tipo, registro)  tipo = "int" | "str"
        self._reg = 0        # contador de registros $t
        self._str_n = 0      # contador de etiquetas de string
        self._vars = {}      # nombre RaraLang → etiqueta MIPS

    # ── helpers ──────────────────────────────────────────────────────────────

    def _reg_next(self):
        r = f"$t{self._reg}"
        self._reg += 1
        return r

    def _str_label(self):
        label = f"_str{self._str_n}"
        self._str_n += 1
        return label

    def _var_label(self, name: str) -> str:
        if name not in self._vars:
            label = f"_var_{name}"
            self._vars[name] = label
            self._data.append(f"{label}: .word 0")
        return self._vars[name]

    # ── expresiones: literales y variables ───────────────────────────────────

    def exitInt(self, ctx: RaraLangParser.IntContext):
        reg = self._reg_next()
        self._text.append(f"    li {reg}, {ctx.INT().getText()}")
        self._stack.append(("int", reg))

    def exitBased(self, ctx: RaraLangParser.BasedContext):
        token = ctx.BASED_NUMBER().getText()[1:-1]
        digits, base = token.rsplit(":", 1)
        value = int(digits, int(base))
        reg = self._reg_next()
        self._text.append(f"    li {reg}, {value}")
        self._stack.append(("int", reg))

    def exitString(self, ctx: RaraLangParser.StringContext):
        raw = ctx.STRING().getText()
        label = self._str_label()
        self._data.append(f"{label}: .asciiz {raw}")
        self._stack.append(("str", label))

    def exitVar(self, ctx: RaraLangParser.VarContext):
        name = ctx.ID().getText()
        label = self._var_label(name)
        reg = self._reg_next()
        self._text.append(f"    lw {reg}, {label}")
        self._stack.append(("int", reg))

    # ── expresiones: aritmética ───────────────────────────────────────────────

    def exitMulDiv(self, ctx: RaraLangParser.MulDivContext):
        _, right = self._stack.pop()
        _, left  = self._stack.pop()
        op = ctx.op.text
        if op == '×':
            self._text += [
                f"    mult {left}, {right}",
                f"    mflo {left}",
            ]
        else:  # ÷
            self._text += [
                f"    div {left}, {right}",
                f"    mflo {left}",
            ]
        self._stack.append(("int", left))

    def exitAddSub(self, ctx: RaraLangParser.AddSubContext):
        _, right = self._stack.pop()
        _, left  = self._stack.pop()
        op = ctx.op.text
        if op == '+':
            self._text.append(f"    add {left}, {left}, {right}")
        else:  # -
            self._text.append(f"    sub {left}, {left}, {right}")
        self._stack.append(("int", left))

    # exitParen no hace nada: el resultado de la subexpresión ya está en la pila

    # ── sentencias ───────────────────────────────────────────────────────────

    def enterPrintStmt(self, ctx: RaraLangParser.PrintStmtContext):
        self._reg = 0   # los $t son locales a cada sentencia

    def enterAssignStmt(self, ctx: RaraLangParser.AssignStmtContext):
        self._reg = 0   # los $t son locales a cada sentencia

    def exitAssignStmt(self, ctx: RaraLangParser.AssignStmtContext):
        kind, val = self._stack.pop()
        label = self._var_label(ctx.ID().getText())
        self._text.append(f"    sw {val}, {label}")

    def exitPrintStmt(self, ctx: RaraLangParser.PrintStmtContext):
        kind, val = self._stack.pop()
        if kind == "int":
            self._text += [
                f"    move $a0, {val}",
                f"    li $v0, 1",
                f"    syscall",
            ]
        else:
            self._text += [
                f"    la $a0, {val}",
                f"    li $v0, 4",
                f"    syscall",
            ]
        self._text += [
            f"    li $a0, 10",
            f"    li $v0, 11",
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
        lines.append("    li $v0, 10")
        lines.append("    syscall")
        return "\n".join(lines) + "\n"
