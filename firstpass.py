from antlr4 import ParseTreeListener
from SpacialTurtleParser import SpacialTurtleParser
from symbols import SymbolTable, Type, FunctionSymbol


class FirstPassListener(ParseTreeListener):
    def __init__(self, symbol_table: SymbolTable):
        self.symbol_table = symbol_table

    def enterForStmt(self, ctx):
        self.symbol_table.push_scope()

    def exitForStmt(self, ctx):
        self.symbol_table.pop_scope()

    def enterWhileStmt(self, ctx):
        self.symbol_table.push_scope()

    def exitWhileStmt(self, ctx):
        self.symbol_table.pop_scope()

    def enterFaceBlock(self, ctx):
        self.symbol_table.push_scope()

    def exitFaceBlock(self, ctx):
        self.symbol_table.pop_scope()

    def enterBlock(self, ctx):
        if ctx.parentCtx is not None and type(ctx.parentCtx).__name__ == 'IfStmtContext':
            self.symbol_table.push_scope()

    def exitBlock(self, ctx):
        if ctx.parentCtx is not None and type(ctx.parentCtx).__name__ == 'IfStmtContext':
            self.symbol_table.pop_scope()


    def enterFuncDef(self, ctx: SpacialTurtleParser.FuncDefContext):
        name = ctx.ID().getText()
        params = []

        if ctx.paramList():
            for id_ctx in ctx.paramList().ID():
                params.append((id_ctx.getText(), Type.FLOAT))

        return_type = Type.VOID
        for stmt in ctx.statement():
            if stmt.returnStmt() and stmt.returnStmt().expr():
                return_type = Type.FLOAT
                break

        func_sym = FunctionSymbol(name, params, return_type, ctx.start.line, ctx.start.column)
        self.symbol_table.add_function(func_sym)

    def enterDeclaration(self, ctx: SpacialTurtleParser.DeclarationContext):
        name = ctx.ID().getText()
        type_str = ctx.varType().getText()

        if type_str == 'int':
            var_type = Type.INT
        elif type_str == 'float':
            var_type = Type.FLOAT
        elif type_str == 'bool':
            var_type = Type.BOOL
        elif type_str == 'string':
            var_type = Type.STRING
        else:
            var_type = Type.FLOAT

        self.symbol_table.add_variable(name, var_type, ctx.start.line, ctx.start.column)