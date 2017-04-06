from GrammarVisitor import GrammarVisitor
from GrammarParser import GrammarParser


class MyVisitor(GrammarVisitor):
    def __init__(self):
        self.memory = {}

    def visitAssign(self, ctx):
        name = ctx.ID().getText()
        value = self.visit(ctx.expr())
        self.memory[name] = value
        print(value)
        return value

    def visitPrintExpr(self, ctx):
        value = self.visit(ctx.expr())
        print(value)
        return 0

    def visitInt(self, ctx):
        try:
            return ctx.INT().getText()
        except TypeError:
            return "SYNTAX ERROR"


    def visitDec(self, ctx):
        try:
            return ctx.DEC().getText()
        except TypeError:
            return "SYNTAX ERROR"

    def visitId(self, ctx):
        name = ctx.ID().getText()
        if name in self.memory:
            return self.memory[name]
        return 0

    def visitOpIn(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        try:
            if float(left) - int(float(left)) == 0:
                left = int(float(left))
            else:
                left = float(left)

            if isinstance(right, list):
                return left in right
            return "SEMANTIC ERROR"
        except ValueError:
            # Left is a string
            try:
                float(right)
                return "SEMANTIC ERROR"
            except ValueError:
                return str(left) in right

    def visitList(self, ctx):
        try:
            new_list = []
            index = 0
            for ex in ctx.expr():
                val = self.visit(ctx.expr(index))
                try:
                    if float(val) - int(float(val)) != 0:
                        new_list.append(float(val))
                    else:
                        new_list.append(int(float(val)))
                except ValueError:
                    if '\"'  in str(val) or '\'' in str(val):
                        new_list.append(str(val).strip('\"'))
                    else:
                        new_list.append(val)
                index += 1
            return new_list
        except TypeError:
            return "SYNTAX ERROR"

    def visitIndex(self, ctx):
        try:
            array = self.visit(ctx.expr(0))
            index = self.visit(ctx.expr(1))
            try:
                if float(index) - int(float(index)) == 0:
                    if int(float(index)) < len(array):
                        if isinstance(array[int(float(index))], str):
                            return  array[int(float(index))]
                        else:
                            return array[int(float(index))]
                    else:
                        return "SEMANTIC ERROR"
                return "SEMANTIC ERROR"
            except ValueError:
                if '\"' in str(index) or '\'' in str(index):
                    return "SEMANTIC ERROR"
                else:
                    return array[index]
        except TypeError:
            return "SEMANTIC ERROR"

    def visitString(self, ctx):
        try:
            new_string = str(ctx.STRING().getText()).strip("\"")
            return new_string
        except TypeError:
            return "SYNTAX ERROR"

    def visitMulDiv(self, ctx):
        try:
            left = float(self.visit(ctx.expr(0)))
            if left - int(left) == 0:
                left = int(left)
            try:
                # Both left and right are numbers
                right = float(self.visit(ctx.expr(1)))
                if right -int(right) == 0:
                    right = int(right)
                if ctx.op.type == GrammarParser.MUL:
                    return left * right
                if right != 0:
                    if ctx.op.type == GrammarParser.DIV:
                        return left / right
                    return left % right
                return "SEMANTIC ERROR"
            except ValueError:
                # Left is a number but right is a string
                if ctx.op.type == GrammarParser.MUL:
                    if left - int(left) == 0:
                        right = str(self.visit(ctx.expr(1))).strip('\'').strip('\"')
                        return left * right
                return "SEMANTIC ERROR"
        except ValueError:
            # Left is definitely a string
            left = self.visit(ctx.expr(0))
            right = self.visit(ctx.expr(1))
            try:
                if ctx.op.type == GrammarParser.MUL:
                    right = float(self.visit(ctx.expr(1)))
                    if right - int(right) == 0:
                        return str(left).strip('\'').strip('\"') * int(right)
                return "SEMANTIC ERROR"
            except ValueError:
                # Right is also a string
                return "SEMANTIC ERROR"

    def visitAddSub(self, ctx):
        try:
            left = float(self.visit(ctx.expr(0)))
            if left - int(left) == 0:
                left = int(left)
            try:
                # Both left and right are numbers
                right = float(self.visit(ctx.expr(1)))
                if right -int(right) == 0:
                    right = int(right)
                if ctx.op.type == GrammarParser.ADD:
                    return left + right
                return left - right
            except ValueError:
                # Left is a number but right is a string
                return "SEMANTIC ERROR"
        except ValueError:
            # Left is definitely a string
            left = self.visit(ctx.expr(0))
            right = self.visit(ctx.expr(1))
            try:
                right = float(self.visit(ctx.expr(1)))
                return "SEMANTIC ERROR"
            except ValueError:
                # Right is also a string
                if ctx.op.type == GrammarParser.ADD:
                    return str(left).strip('\'') + str(right).strip('\'')
                return "SEMANTIC ERROR"

    def visitExpFlo(self, ctx):
        try:
            left = float(self.visit(ctx.expr(0)))
            if left - int(left) == 0:
                left = int(left)
            try:
                # Both left and right are numbers
                right = float(self.visit(ctx.expr(1)))
                if right -int(right) == 0:
                    right = int(right)
                if ctx.op.type == GrammarParser.EXP:
                    return left ** right
                return left // right
            except ValueError:
                # Left is a number but right is a string
                return "SEMANTIC ERROR"
        except ValueError:
            return "SEMANTIC ERROR"

    def visitParens(self, ctx):
        return self.visit(ctx.expr())

    def visitNot(self, ctx):
        try:
            right = float(ctx.expr().getText())
            if  right != 0:
                return 0
            else:
                return 1
        except ValueError:
            return "SEMANTIC ERROR"

    def visitAndOr(self, ctx):
        left = int(self.visit(ctx.expr(0)))
        right = int(self.visit(ctx.expr(1)))
        if ctx.op.type == GrammarParser.AND:
            if left != 0 and right != 0:
                return 1
            return 0
        else:
            if left != 0 or right !=0:
                return 1
            return 0

    def visitBool(self, ctx):
        if ctx.op.type == GrammarParser.TRUE:
            return 1
        return 0

    def visitComparators(self, ctx):
        left = int(self.visit(ctx.expr(0)))
        right = int(self.visit(ctx.expr(1)))
        if ctx.op.type == GrammarParser.GRT:
            return 1 if left > right else 0
        elif ctx.op.type == GrammarParser.GRE:
            return 1 if left >= right else 0
        elif ctx.op.type == GrammarParser.LET:
            return 1 if left < right else 0
        elif ctx.op.type == GrammarParser.LEE:
            return 1 if left <= right else 0
        elif ctx.op.type == GrammarParser.EQL:
            return 1 if left == right else 0
        else:
            return 1 if left != right else 0