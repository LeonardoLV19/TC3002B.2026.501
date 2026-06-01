from antlr.RaraLangListener import RaraLangListener
from antlr.RaraLangParser import RaraLangParser


class _CtrlFrame:
    """Buffers de código para un if/then/else o un while en curso."""
    def __init__(self, label: int, ctx, kind: str = 'if'):
        self.label    = label
        self.ctx      = ctx        # IfStmtContext o WhileStmtContext dueño del frame
        self.kind     = kind       # 'if' | 'while'
        self.cond_buf = []
        self.then_buf = []         # cuerpo del then (if) o del ciclo (while)
        self.else_buf = []
        self.cond_reg = None       # registro que contiene el resultado de la condición
        self.phase    = 'cond'     # 'cond' | 'then' | 'else'
        self.has_else = False


class MIPSListener(RaraLangListener):

    def __init__(self):
        self._data      = []
        self._text      = []
        self._main_text = self._text
        self._buf_stack = []
        self._stack     = []
        self._reg       = 0
        self._str_n     = 0
        self._vars      = {}
        self._frames    = []
        self._label_n   = 0
        self._func_bufs = []   # [(name, [lines]), ...]

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
            self._text += [f"    mult {left}, {right}", f"    mflo {left}"]
        elif op == '÷':
            self._text += [f"    div {left}, {right}",  f"    mflo {left}"]
        elif op == '⊞':
            self._text += [f"    div {left}, {right}",  f"    mfhi {left}"]
        else:
            self._text += [f"    sll {left}, {left}, 1", f"    add {left}, {left}, {right}"]
        self._stack.append(("int", left))

    def exitAddSub(self, ctx: RaraLangParser.AddSubContext):
        _, right = self._stack.pop()
        _, left  = self._stack.pop()
        op = ctx.op.text
        if op == '+':
            self._text.append(f"    add {left}, {left}, {right}")
        elif op == '-':
            self._text.append(f"    sub {left}, {left}, {right}")
        else:
            self._text += [f"    add {left}, {left}, {right}", f"    sra {left}, {left}, 1"]
        self._stack.append(("int", left))

    def exitCompare(self, ctx: RaraLangParser.CompareContext):
        _, right = self._stack.pop()
        _, left  = self._stack.pop()
        op = ctx.op.text
        if op == '==':
            self._text.append(f"    seq {left}, {left}, {right}")
        elif op == '!=':
            self._text.append(f"    sne {left}, {left}, {right}")
        elif op == '<':
            self._text.append(f"    slt {left}, {left}, {right}")
        else:   # >
            self._text.append(f"    slt {left}, {right}, {left}")
        self._stack.append(("int", left))

    def exitNeg(self, ctx: RaraLangParser.NegContext):
        _, val = self._stack.pop()
        self._text.append(f"    sub {val}, $zero, {val}")
        self._stack.append(("int", val))

    # ── control de flujo: if/then/else ───────────────────────────────────────

    def enterIfStmt(self, ctx: RaraLangParser.IfStmtContext):
        self._reg = 0
        frame = _CtrlFrame(self._label_n, ctx, kind='if')
        self._label_n += 1
        self._frames.append(frame)
        self._buf_stack.append(self._text)
        self._text = frame.cond_buf

    def exitIfStmt(self, ctx: RaraLangParser.IfStmtContext):
        frame = self._frames.pop()
        self._text = self._buf_stack.pop()
        lbl      = frame.label
        end_lbl  = f"_if_end_{lbl}"
        else_lbl = f"_if_else_{lbl}"
        self._text.extend(frame.cond_buf)
        if frame.has_else:
            self._text.append(f"    beq {frame.cond_reg}, $zero, {else_lbl}")
            self._text.extend(frame.then_buf)
            self._text.append(f"    j {end_lbl}")
            self._text.append(f"{else_lbl}:")
            self._text.extend(frame.else_buf)
        else:
            self._text.append(f"    beq {frame.cond_reg}, $zero, {end_lbl}")
            self._text.extend(frame.then_buf)
        self._text.append(f"{end_lbl}:")

    # ── control de flujo: while ───────────────────────────────────────────────

    def enterWhileStmt(self, ctx: RaraLangParser.WhileStmtContext):
        self._reg = 0
        frame = _CtrlFrame(self._label_n, ctx, kind='while')
        self._label_n += 1
        self._frames.append(frame)
        self._buf_stack.append(self._text)
        self._text = frame.cond_buf

    def exitWhileStmt(self, ctx: RaraLangParser.WhileStmtContext):
        frame = self._frames.pop()
        self._text = self._buf_stack.pop()
        lbl       = frame.label
        start_lbl = f"_while_start_{lbl}"
        end_lbl   = f"_while_end_{lbl}"
        self._text.append(f"{start_lbl}:")
        self._text.extend(frame.cond_buf)
        self._text.append(f"    beq {frame.cond_reg}, $zero, {end_lbl}")
        self._text.extend(frame.then_buf)
        self._text.append(f"    j {start_lbl}")
        self._text.append(f"{end_lbl}:")

    # ── bloques ───────────────────────────────────────────────────────────────

    def exitBlockStmt(self, ctx: RaraLangParser.BlockStmtContext):
        pass   # las sentencias internas ya emitieron a self._text

    # ── transiciones de fase (compartido por if y while) ─────────────────────

    def enterEveryRule(self, ctx):
        if not self._frames:
            return
        frame = self._frames[-1]
        if ctx.parentCtx is not frame.ctx:
            return
        stmt_types = (
            RaraLangParser.PrintStmtContext,
            RaraLangParser.AssignStmtContext,
            RaraLangParser.IfStmtContext,
            RaraLangParser.WhileStmtContext,
            RaraLangParser.BlockStmtContext,
            RaraLangParser.ReturnStmtContext,
        )
        if not isinstance(ctx, stmt_types):
            return
        if frame.phase == 'cond':
            frame.cond_reg = self._stack.pop()[1]
            frame.phase = 'then'
            self._reg = 0
            self._text = frame.then_buf
        elif frame.phase == 'then' and frame.kind == 'if':
            frame.has_else = True
            frame.phase = 'else'
            self._reg = 0
            self._text = frame.else_buf

    # ── sentencias simples ────────────────────────────────────────────────────

    def enterPrintStmt(self, ctx: RaraLangParser.PrintStmtContext):
        self._reg = 0

    def enterAssignStmt(self, ctx: RaraLangParser.AssignStmtContext):
        self._reg = 0

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

    # ── funciones ─────────────────────────────────────────────────────────────

    def enterFuncDecl(self, ctx: RaraLangParser.FuncDeclContext):
        self._reg = 0
        name = ctx.ID().getText()
        buf = [f"{name}:"]
        # almacenar argumentos en variables .data
        if ctx.paramList():
            for i, tok in enumerate(ctx.paramList().ID()):
                label = self._var_label(tok.getText())
                buf.append(f"    sw $a{i}, {label}")
        self._buf_stack.append(self._text)
        self._text = buf

    def exitFuncDecl(self, ctx: RaraLangParser.FuncDeclContext):
        self._text.append(f"    jr $ra")
        self._func_bufs.append(self._text)
        self._text = self._buf_stack.pop()
        self._reg = 0

    def enterReturnStmt(self, ctx: RaraLangParser.ReturnStmtContext):
        self._reg = 0

    def exitReturnStmt(self, ctx: RaraLangParser.ReturnStmtContext):
        _, val = self._stack.pop()
        self._text.append(f"    move $v0, {val}")
        self._text.append(f"    jr $ra")

    def exitCall(self, ctx: RaraLangParser.CallContext):
        name = ctx.ID().getText()
        nargs = len(ctx.argList().expr()) if ctx.argList() else 0
        # pop args (stack: arg0 deepest, argN-1 on top) → reverse
        args = [self._stack.pop()[1] for _ in range(nargs)]
        args.reverse()
        for i, reg in enumerate(args):
            self._text.append(f"    move $a{i}, {reg}")
        # guardar $ra antes del jal (bug de función-llama-función)
        self._text += [
            f"    addiu $sp, $sp, -4",
            f"    sw $ra, 0($sp)",
            f"    jal {name}",
            f"    lw $ra, 0($sp)",
            f"    addiu $sp, $sp, 4",
        ]
        result = self._reg_next()
        self._text.append(f"    move {result}, $v0")
        self._stack.append(("int", result))

    # ── salida ───────────────────────────────────────────────────────────────

    def output(self) -> str:
        lines = []
        if self._data:
            lines.append(".data")
            lines.extend(self._data)
            lines.append("")
        lines.append(".text")
        lines.append("main:")
        lines.extend(self._main_text)
        lines.append("    li $v0, 10")
        lines.append("    syscall")
        for buf in self._func_bufs:
            lines.append("")
            lines.extend(buf)
        return "\n".join(lines) + "\n"
