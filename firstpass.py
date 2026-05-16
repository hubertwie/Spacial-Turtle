from antlr4 import ParseTreeListener
from SpacialTurtleParser import SpacialTurtleParser
from symbols import SymbolTable, Type, FunctionSymbol


class FirstPassListener(ParseTreeListener):
    """
    Listener do pierwszego przebiegu analizy.
    Rejestruje deklaracje zmiennych i funkcji w tablicy symboli,
    sprawdza redeklaracje, zarządza zakresami (push/pop)
    dla pętli, bloków if, faceBlock oraz funkcji.
    """

    def __init__(self, symbol_table: SymbolTable) -> None:
        """
        Inicjalizuje listener z gotową tablicą symboli.
        :param symbol_table: Tablica symboli do rejestrowania deklaracji.
        :type symbol_table: SymbolTable
        """
        self.symbol_table = symbol_table

    def _get_type(self, type_str: str, line: int, column: int) -> Type:
        """
        Konwertuje napis reprezentujący typ na odpowiednią wartość enum Type.
        W przypadku nieznanego typu rzuca wyjątek z numerem linii i kolumny.
        :param type_str: Nazwa typu jako string ('int', 'float', 'bool', 'string').
        :type type_str: str
        :param line: Numer linii, w której wystąpił ten typ.
        :type line: int
        :param column: Numer kolumny, w której wystąpił ten typ.
        :type column: int
        :return: Odpowiedni typ enum.
        :rtype: Type
        :raises ValueError: Jeśli type_str nie jest rozpoznawany.
        """
        if type_str == 'int':
            return Type.INT
        elif type_str == 'float':
            return Type.FLOAT
        elif type_str == 'bool':
            return Type.BOOL
        elif type_str == 'string':
            return Type.STRING
        else:
            raise ValueError(f"Linia {line}, kol. {column}: Nieznany typ '{type_str}'")

    def enterForStmt(self, ctx: SpacialTurtleParser.ForStmtContext) -> None:
        """
        Wywoływane przy wejściu do węzła pętli for.
        Tworzy nowy zakres dla zmiennych wewnątrz pętli.
        :param ctx: Kontekst parsera dla pętli for.
        :type ctx: SpacialTurtleParser.ForStmtContext
        """
        self.symbol_table.push_scope()

    def exitForStmt(self, ctx: SpacialTurtleParser.ForStmtContext) -> None:
        """
        Wywoływane przy wyjściu z węzła pętli for.
        Zamyka zakres utworzony dla tej pętli.
        :param ctx: Kontekst parsera dla pętli for.
        :type ctx: SpacialTurtleParser.ForStmtContext
        """
        self.symbol_table.pop_scope()

    def enterWhileStmt(self, ctx: SpacialTurtleParser.WhileStmtContext) -> None:
        """
        Wywoływane przy wejściu do węzła pętli while.
        Tworzy nowy zakres dla zmiennych wewnątrz pętli.
        :param ctx: Kontekst parsera dla pętli while.
        :type ctx: SpacialTurtleParser.WhileStmtContext
        """
        self.symbol_table.push_scope()

    def exitWhileStmt(self, ctx: SpacialTurtleParser.WhileStmtContext) -> None:
        """
        Wywoływane przy wyjściu z węzła pętli while.
        Zamyka zakres utworzony dla tej pętli.
        :param ctx: Kontekst parsera dla pętli while.
        :type ctx: SpacialTurtleParser.WhileStmtContext
        """
        self.symbol_table.pop_scope()

    def enterFaceBlock(self, ctx: SpacialTurtleParser.FaceBlockContext) -> None:
        """
        Wywoływane przy wejściu do bloku face (tworzenia ściany).
        Tworzy nowy zakres dla zmiennych lokalnych wewnątrz face.
        :param ctx: Kontekst parsera dla bloku face.
        :type ctx: SpacialTurtleParser.FaceBlockContext
        """
        self.symbol_table.push_scope()

    def exitFaceBlock(self, ctx: SpacialTurtleParser.FaceBlockContext) -> None:
        """
        Wywoływane przy wyjściu z bloku face.
        Zamyka zakres utworzony dla tego bloku.
        :param ctx: Kontekst parsera dla bloku face.
        :type ctx: SpacialTurtleParser.FaceBlockContext
        """
        self.symbol_table.pop_scope()

    def enterBlock(self, ctx: SpacialTurtleParser.BlockContext) -> None:
        """
        Wywoływane przy wejściu do bloku kodu ({...}).
        Tylko jeśli rodzicem jest IfStmtContext,
        tworzy nowy zakres dla gałęzi if/else.
        :param ctx: Kontekst parsera dla bloku kodu.
        :type ctx: SpacialTurtleParser.BlockContext
        """
        if ctx.parentCtx is not None and type(ctx.parentCtx).__name__ == 'IfStmtContext':
            self.symbol_table.push_scope()

    def exitBlock(self, ctx: SpacialTurtleParser.BlockContext) -> None:
        """
        Wywoływane przy wyjściu z bloku kodu.
        Zamyka zakres tylko jeśli rodzicem było IfStmtContext.
        :param ctx: Kontekst parsera dla bloku kodu.
        :type ctx: SpacialTurtleParser.BlockContext
        """
        if ctx.parentCtx is not None and type(ctx.parentCtx).__name__ == 'IfStmtContext':
            self.symbol_table.pop_scope()

    def enterFuncDef(self, ctx: SpacialTurtleParser.FuncDefContext) -> None:
        """
        Wywoływane przy wejściu do definicji funkcji.
        Tworzy nowy zakres dla zmiennych lokalnych funkcji,
        rejestruje funkcję w tablicy symboli,
        a także dodaje parametry jako zmienne w tym zakresie.
        :param ctx: Kontekst parsera dla definicji funkcji.
        :type ctx: SpacialTurtleParser.FuncDefContext
        """
        self.symbol_table.push_scope()

        name = ctx.ID().getText()
        params = []
        if ctx.typedParamList():
            for param_ctx in ctx.typedParamList().paramWithType():
                param_name = param_ctx.ID().getText()
                line = param_ctx.varType().start.line
                col = param_ctx.varType().start.column
                param_type = self._get_type(param_ctx.varType().getText(), line, col)
                params.append((param_name, param_type))
                self.symbol_table.add_variable(param_name, param_type, line, col)

        return_type = Type.VOID
        if ctx.varType():
            line = ctx.varType().start.line
            col = ctx.varType().start.column
            return_type = self._get_type(ctx.varType().getText(), line, col)

        func_sym = FunctionSymbol(name, params, return_type, ctx.start.line, ctx.start.column)
        self.symbol_table.add_function(func_sym)

    def exitFuncDef(self, ctx: SpacialTurtleParser.FuncDefContext) -> None:
        """
        Wywoływane przy wyjściu z definicji funkcji.
        Zamyka zakres utworzony dla tej funkcji.
        :param ctx: Kontekst parsera dla definicji funkcji.
        :type ctx: SpacialTurtleParser.FuncDefContext
        """
        self.symbol_table.pop_scope()

    def enterDeclaration(self, ctx: SpacialTurtleParser.DeclarationContext) -> None:
        """
        Wywoływane przy wejściu do deklaracji zmiennej.
        Rejestruje zmienną w bieżącym zakresie tablicy symboli.
        :param ctx: Kontekst parsera dla deklaracji zmiennej.
        :type ctx: SpacialTurtleParser.DeclarationContext
        """
        name = ctx.ID().getText()
        line = ctx.varType().start.line
        col = ctx.varType().start.column
        var_type = self._get_type(ctx.varType().getText(), line, col)
        self.symbol_table.add_variable(name, var_type, ctx.start.line, ctx.start.column)