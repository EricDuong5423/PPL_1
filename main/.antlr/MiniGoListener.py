# Generated from /Users/supreme3bye/Desktop/PPL_1/main/MiniGo.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .MiniGoParser import MiniGoParser
else:
    from MiniGoParser import MiniGoParser

# This class defines a complete listener for a parse tree produced by MiniGoParser.
class MiniGoListener(ParseTreeListener):

    # Enter a parse tree produced by MiniGoParser#program.
    def enterProgram(self, ctx:MiniGoParser.ProgramContext):
        pass

    # Exit a parse tree produced by MiniGoParser#program.
    def exitProgram(self, ctx:MiniGoParser.ProgramContext):
        pass


    # Enter a parse tree produced by MiniGoParser#literal.
    def enterLiteral(self, ctx:MiniGoParser.LiteralContext):
        pass

    # Exit a parse tree produced by MiniGoParser#literal.
    def exitLiteral(self, ctx:MiniGoParser.LiteralContext):
        pass


    # Enter a parse tree produced by MiniGoParser#list_literal.
    def enterList_literal(self, ctx:MiniGoParser.List_literalContext):
        pass

    # Exit a parse tree produced by MiniGoParser#list_literal.
    def exitList_literal(self, ctx:MiniGoParser.List_literalContext):
        pass


    # Enter a parse tree produced by MiniGoParser#list_literal_noempty.
    def enterList_literal_noempty(self, ctx:MiniGoParser.List_literal_noemptyContext):
        pass

    # Exit a parse tree produced by MiniGoParser#list_literal_noempty.
    def exitList_literal_noempty(self, ctx:MiniGoParser.List_literal_noemptyContext):
        pass


    # Enter a parse tree produced by MiniGoParser#all_type.
    def enterAll_type(self, ctx:MiniGoParser.All_typeContext):
        pass

    # Exit a parse tree produced by MiniGoParser#all_type.
    def exitAll_type(self, ctx:MiniGoParser.All_typeContext):
        pass


    # Enter a parse tree produced by MiniGoParser#basic_type.
    def enterBasic_type(self, ctx:MiniGoParser.Basic_typeContext):
        pass

    # Exit a parse tree produced by MiniGoParser#basic_type.
    def exitBasic_type(self, ctx:MiniGoParser.Basic_typeContext):
        pass


    # Enter a parse tree produced by MiniGoParser#list_array_type_lit.
    def enterList_array_type_lit(self, ctx:MiniGoParser.List_array_type_litContext):
        pass

    # Exit a parse tree produced by MiniGoParser#list_array_type_lit.
    def exitList_array_type_lit(self, ctx:MiniGoParser.List_array_type_litContext):
        pass


    # Enter a parse tree produced by MiniGoParser#array_type_lit.
    def enterArray_type_lit(self, ctx:MiniGoParser.Array_type_litContext):
        pass

    # Exit a parse tree produced by MiniGoParser#array_type_lit.
    def exitArray_type_lit(self, ctx:MiniGoParser.Array_type_litContext):
        pass


    # Enter a parse tree produced by MiniGoParser#array_type.
    def enterArray_type(self, ctx:MiniGoParser.Array_typeContext):
        pass

    # Exit a parse tree produced by MiniGoParser#array_type.
    def exitArray_type(self, ctx:MiniGoParser.Array_typeContext):
        pass


    # Enter a parse tree produced by MiniGoParser#array_literal.
    def enterArray_literal(self, ctx:MiniGoParser.Array_literalContext):
        pass

    # Exit a parse tree produced by MiniGoParser#array_literal.
    def exitArray_literal(self, ctx:MiniGoParser.Array_literalContext):
        pass


    # Enter a parse tree produced by MiniGoParser#dim_lit.
    def enterDim_lit(self, ctx:MiniGoParser.Dim_litContext):
        pass

    # Exit a parse tree produced by MiniGoParser#dim_lit.
    def exitDim_lit(self, ctx:MiniGoParser.Dim_litContext):
        pass


    # Enter a parse tree produced by MiniGoParser#dim.
    def enterDim(self, ctx:MiniGoParser.DimContext):
        pass

    # Exit a parse tree produced by MiniGoParser#dim.
    def exitDim(self, ctx:MiniGoParser.DimContext):
        pass


    # Enter a parse tree produced by MiniGoParser#list_array_element.
    def enterList_array_element(self, ctx:MiniGoParser.List_array_elementContext):
        pass

    # Exit a parse tree produced by MiniGoParser#list_array_element.
    def exitList_array_element(self, ctx:MiniGoParser.List_array_elementContext):
        pass


    # Enter a parse tree produced by MiniGoParser#array_element.
    def enterArray_element(self, ctx:MiniGoParser.Array_elementContext):
        pass

    # Exit a parse tree produced by MiniGoParser#array_element.
    def exitArray_element(self, ctx:MiniGoParser.Array_elementContext):
        pass


    # Enter a parse tree produced by MiniGoParser#struct_literal.
    def enterStruct_literal(self, ctx:MiniGoParser.Struct_literalContext):
        pass

    # Exit a parse tree produced by MiniGoParser#struct_literal.
    def exitStruct_literal(self, ctx:MiniGoParser.Struct_literalContext):
        pass


    # Enter a parse tree produced by MiniGoParser#list_elements_lit.
    def enterList_elements_lit(self, ctx:MiniGoParser.List_elements_litContext):
        pass

    # Exit a parse tree produced by MiniGoParser#list_elements_lit.
    def exitList_elements_lit(self, ctx:MiniGoParser.List_elements_litContext):
        pass


    # Enter a parse tree produced by MiniGoParser#list_element.
    def enterList_element(self, ctx:MiniGoParser.List_elementContext):
        pass

    # Exit a parse tree produced by MiniGoParser#list_element.
    def exitList_element(self, ctx:MiniGoParser.List_elementContext):
        pass


    # Enter a parse tree produced by MiniGoParser#list_expression.
    def enterList_expression(self, ctx:MiniGoParser.List_expressionContext):
        pass

    # Exit a parse tree produced by MiniGoParser#list_expression.
    def exitList_expression(self, ctx:MiniGoParser.List_expressionContext):
        pass


    # Enter a parse tree produced by MiniGoParser#expression.
    def enterExpression(self, ctx:MiniGoParser.ExpressionContext):
        pass

    # Exit a parse tree produced by MiniGoParser#expression.
    def exitExpression(self, ctx:MiniGoParser.ExpressionContext):
        pass


    # Enter a parse tree produced by MiniGoParser#expression1.
    def enterExpression1(self, ctx:MiniGoParser.Expression1Context):
        pass

    # Exit a parse tree produced by MiniGoParser#expression1.
    def exitExpression1(self, ctx:MiniGoParser.Expression1Context):
        pass


    # Enter a parse tree produced by MiniGoParser#expression2.
    def enterExpression2(self, ctx:MiniGoParser.Expression2Context):
        pass

    # Exit a parse tree produced by MiniGoParser#expression2.
    def exitExpression2(self, ctx:MiniGoParser.Expression2Context):
        pass


    # Enter a parse tree produced by MiniGoParser#expression3.
    def enterExpression3(self, ctx:MiniGoParser.Expression3Context):
        pass

    # Exit a parse tree produced by MiniGoParser#expression3.
    def exitExpression3(self, ctx:MiniGoParser.Expression3Context):
        pass


    # Enter a parse tree produced by MiniGoParser#expression4.
    def enterExpression4(self, ctx:MiniGoParser.Expression4Context):
        pass

    # Exit a parse tree produced by MiniGoParser#expression4.
    def exitExpression4(self, ctx:MiniGoParser.Expression4Context):
        pass


    # Enter a parse tree produced by MiniGoParser#expression5.
    def enterExpression5(self, ctx:MiniGoParser.Expression5Context):
        pass

    # Exit a parse tree produced by MiniGoParser#expression5.
    def exitExpression5(self, ctx:MiniGoParser.Expression5Context):
        pass


    # Enter a parse tree produced by MiniGoParser#expression6.
    def enterExpression6(self, ctx:MiniGoParser.Expression6Context):
        pass

    # Exit a parse tree produced by MiniGoParser#expression6.
    def exitExpression6(self, ctx:MiniGoParser.Expression6Context):
        pass


    # Enter a parse tree produced by MiniGoParser#expression7.
    def enterExpression7(self, ctx:MiniGoParser.Expression7Context):
        pass

    # Exit a parse tree produced by MiniGoParser#expression7.
    def exitExpression7(self, ctx:MiniGoParser.Expression7Context):
        pass


    # Enter a parse tree produced by MiniGoParser#funcall.
    def enterFuncall(self, ctx:MiniGoParser.FuncallContext):
        pass

    # Exit a parse tree produced by MiniGoParser#funcall.
    def exitFuncall(self, ctx:MiniGoParser.FuncallContext):
        pass


    # Enter a parse tree produced by MiniGoParser#funcall_noempty.
    def enterFuncall_noempty(self, ctx:MiniGoParser.Funcall_noemptyContext):
        pass

    # Exit a parse tree produced by MiniGoParser#funcall_noempty.
    def exitFuncall_noempty(self, ctx:MiniGoParser.Funcall_noemptyContext):
        pass


    # Enter a parse tree produced by MiniGoParser#const_declared.
    def enterConst_declared(self, ctx:MiniGoParser.Const_declaredContext):
        pass

    # Exit a parse tree produced by MiniGoParser#const_declared.
    def exitConst_declared(self, ctx:MiniGoParser.Const_declaredContext):
        pass


    # Enter a parse tree produced by MiniGoParser#var_declared.
    def enterVar_declared(self, ctx:MiniGoParser.Var_declaredContext):
        pass

    # Exit a parse tree produced by MiniGoParser#var_declared.
    def exitVar_declared(self, ctx:MiniGoParser.Var_declaredContext):
        pass


    # Enter a parse tree produced by MiniGoParser#func_declared.
    def enterFunc_declared(self, ctx:MiniGoParser.Func_declaredContext):
        pass

    # Exit a parse tree produced by MiniGoParser#func_declared.
    def exitFunc_declared(self, ctx:MiniGoParser.Func_declaredContext):
        pass


    # Enter a parse tree produced by MiniGoParser#parameter_lit.
    def enterParameter_lit(self, ctx:MiniGoParser.Parameter_litContext):
        pass

    # Exit a parse tree produced by MiniGoParser#parameter_lit.
    def exitParameter_lit(self, ctx:MiniGoParser.Parameter_litContext):
        pass


    # Enter a parse tree produced by MiniGoParser#parameter.
    def enterParameter(self, ctx:MiniGoParser.ParameterContext):
        pass

    # Exit a parse tree produced by MiniGoParser#parameter.
    def exitParameter(self, ctx:MiniGoParser.ParameterContext):
        pass


    # Enter a parse tree produced by MiniGoParser#method_declared.
    def enterMethod_declared(self, ctx:MiniGoParser.Method_declaredContext):
        pass

    # Exit a parse tree produced by MiniGoParser#method_declared.
    def exitMethod_declared(self, ctx:MiniGoParser.Method_declaredContext):
        pass


    # Enter a parse tree produced by MiniGoParser#struct_declared.
    def enterStruct_declared(self, ctx:MiniGoParser.Struct_declaredContext):
        pass

    # Exit a parse tree produced by MiniGoParser#struct_declared.
    def exitStruct_declared(self, ctx:MiniGoParser.Struct_declaredContext):
        pass


    # Enter a parse tree produced by MiniGoParser#interface_declared.
    def enterInterface_declared(self, ctx:MiniGoParser.Interface_declaredContext):
        pass

    # Exit a parse tree produced by MiniGoParser#interface_declared.
    def exitInterface_declared(self, ctx:MiniGoParser.Interface_declaredContext):
        pass


    # Enter a parse tree produced by MiniGoParser#declared.
    def enterDeclared(self, ctx:MiniGoParser.DeclaredContext):
        pass

    # Exit a parse tree produced by MiniGoParser#declared.
    def exitDeclared(self, ctx:MiniGoParser.DeclaredContext):
        pass


    # Enter a parse tree produced by MiniGoParser#list_statement.
    def enterList_statement(self, ctx:MiniGoParser.List_statementContext):
        pass

    # Exit a parse tree produced by MiniGoParser#list_statement.
    def exitList_statement(self, ctx:MiniGoParser.List_statementContext):
        pass


    # Enter a parse tree produced by MiniGoParser#declared_statement.
    def enterDeclared_statement(self, ctx:MiniGoParser.Declared_statementContext):
        pass

    # Exit a parse tree produced by MiniGoParser#declared_statement.
    def exitDeclared_statement(self, ctx:MiniGoParser.Declared_statementContext):
        pass


    # Enter a parse tree produced by MiniGoParser#assign_statement.
    def enterAssign_statement(self, ctx:MiniGoParser.Assign_statementContext):
        pass

    # Exit a parse tree produced by MiniGoParser#assign_statement.
    def exitAssign_statement(self, ctx:MiniGoParser.Assign_statementContext):
        pass


    # Enter a parse tree produced by MiniGoParser#operators.
    def enterOperators(self, ctx:MiniGoParser.OperatorsContext):
        pass

    # Exit a parse tree produced by MiniGoParser#operators.
    def exitOperators(self, ctx:MiniGoParser.OperatorsContext):
        pass


    # Enter a parse tree produced by MiniGoParser#list_assignment_lhs.
    def enterList_assignment_lhs(self, ctx:MiniGoParser.List_assignment_lhsContext):
        pass

    # Exit a parse tree produced by MiniGoParser#list_assignment_lhs.
    def exitList_assignment_lhs(self, ctx:MiniGoParser.List_assignment_lhsContext):
        pass


    # Enter a parse tree produced by MiniGoParser#assignment_lhs.
    def enterAssignment_lhs(self, ctx:MiniGoParser.Assignment_lhsContext):
        pass

    # Exit a parse tree produced by MiniGoParser#assignment_lhs.
    def exitAssignment_lhs(self, ctx:MiniGoParser.Assignment_lhsContext):
        pass


    # Enter a parse tree produced by MiniGoParser#list_array_index.
    def enterList_array_index(self, ctx:MiniGoParser.List_array_indexContext):
        pass

    # Exit a parse tree produced by MiniGoParser#list_array_index.
    def exitList_array_index(self, ctx:MiniGoParser.List_array_indexContext):
        pass


    # Enter a parse tree produced by MiniGoParser#array_index.
    def enterArray_index(self, ctx:MiniGoParser.Array_indexContext):
        pass

    # Exit a parse tree produced by MiniGoParser#array_index.
    def exitArray_index(self, ctx:MiniGoParser.Array_indexContext):
        pass


    # Enter a parse tree produced by MiniGoParser#else_statement.
    def enterElse_statement(self, ctx:MiniGoParser.Else_statementContext):
        pass

    # Exit a parse tree produced by MiniGoParser#else_statement.
    def exitElse_statement(self, ctx:MiniGoParser.Else_statementContext):
        pass


    # Enter a parse tree produced by MiniGoParser#elif_statement.
    def enterElif_statement(self, ctx:MiniGoParser.Elif_statementContext):
        pass

    # Exit a parse tree produced by MiniGoParser#elif_statement.
    def exitElif_statement(self, ctx:MiniGoParser.Elif_statementContext):
        pass


    # Enter a parse tree produced by MiniGoParser#if_statement.
    def enterIf_statement(self, ctx:MiniGoParser.If_statementContext):
        pass

    # Exit a parse tree produced by MiniGoParser#if_statement.
    def exitIf_statement(self, ctx:MiniGoParser.If_statementContext):
        pass


    # Enter a parse tree produced by MiniGoParser#range_loop.
    def enterRange_loop(self, ctx:MiniGoParser.Range_loopContext):
        pass

    # Exit a parse tree produced by MiniGoParser#range_loop.
    def exitRange_loop(self, ctx:MiniGoParser.Range_loopContext):
        pass


    # Enter a parse tree produced by MiniGoParser#init_loop.
    def enterInit_loop(self, ctx:MiniGoParser.Init_loopContext):
        pass

    # Exit a parse tree produced by MiniGoParser#init_loop.
    def exitInit_loop(self, ctx:MiniGoParser.Init_loopContext):
        pass


    # Enter a parse tree produced by MiniGoParser#basic_loop.
    def enterBasic_loop(self, ctx:MiniGoParser.Basic_loopContext):
        pass

    # Exit a parse tree produced by MiniGoParser#basic_loop.
    def exitBasic_loop(self, ctx:MiniGoParser.Basic_loopContext):
        pass


    # Enter a parse tree produced by MiniGoParser#for_statement.
    def enterFor_statement(self, ctx:MiniGoParser.For_statementContext):
        pass

    # Exit a parse tree produced by MiniGoParser#for_statement.
    def exitFor_statement(self, ctx:MiniGoParser.For_statementContext):
        pass


    # Enter a parse tree produced by MiniGoParser#break_statement.
    def enterBreak_statement(self, ctx:MiniGoParser.Break_statementContext):
        pass

    # Exit a parse tree produced by MiniGoParser#break_statement.
    def exitBreak_statement(self, ctx:MiniGoParser.Break_statementContext):
        pass


    # Enter a parse tree produced by MiniGoParser#continue_statement.
    def enterContinue_statement(self, ctx:MiniGoParser.Continue_statementContext):
        pass

    # Exit a parse tree produced by MiniGoParser#continue_statement.
    def exitContinue_statement(self, ctx:MiniGoParser.Continue_statementContext):
        pass


    # Enter a parse tree produced by MiniGoParser#call_statement.
    def enterCall_statement(self, ctx:MiniGoParser.Call_statementContext):
        pass

    # Exit a parse tree produced by MiniGoParser#call_statement.
    def exitCall_statement(self, ctx:MiniGoParser.Call_statementContext):
        pass


    # Enter a parse tree produced by MiniGoParser#return_statement.
    def enterReturn_statement(self, ctx:MiniGoParser.Return_statementContext):
        pass

    # Exit a parse tree produced by MiniGoParser#return_statement.
    def exitReturn_statement(self, ctx:MiniGoParser.Return_statementContext):
        pass


    # Enter a parse tree produced by MiniGoParser#end_statement.
    def enterEnd_statement(self, ctx:MiniGoParser.End_statementContext):
        pass

    # Exit a parse tree produced by MiniGoParser#end_statement.
    def exitEnd_statement(self, ctx:MiniGoParser.End_statementContext):
        pass


    # Enter a parse tree produced by MiniGoParser#struct_statement.
    def enterStruct_statement(self, ctx:MiniGoParser.Struct_statementContext):
        pass

    # Exit a parse tree produced by MiniGoParser#struct_statement.
    def exitStruct_statement(self, ctx:MiniGoParser.Struct_statementContext):
        pass


    # Enter a parse tree produced by MiniGoParser#method_parameter.
    def enterMethod_parameter(self, ctx:MiniGoParser.Method_parameterContext):
        pass

    # Exit a parse tree produced by MiniGoParser#method_parameter.
    def exitMethod_parameter(self, ctx:MiniGoParser.Method_parameterContext):
        pass


    # Enter a parse tree produced by MiniGoParser#method_parameter_lit.
    def enterMethod_parameter_lit(self, ctx:MiniGoParser.Method_parameter_litContext):
        pass

    # Exit a parse tree produced by MiniGoParser#method_parameter_lit.
    def exitMethod_parameter_lit(self, ctx:MiniGoParser.Method_parameter_litContext):
        pass


    # Enter a parse tree produced by MiniGoParser#method_statement.
    def enterMethod_statement(self, ctx:MiniGoParser.Method_statementContext):
        pass

    # Exit a parse tree produced by MiniGoParser#method_statement.
    def exitMethod_statement(self, ctx:MiniGoParser.Method_statementContext):
        pass


    # Enter a parse tree produced by MiniGoParser#statement.
    def enterStatement(self, ctx:MiniGoParser.StatementContext):
        pass

    # Exit a parse tree produced by MiniGoParser#statement.
    def exitStatement(self, ctx:MiniGoParser.StatementContext):
        pass


    # Enter a parse tree produced by MiniGoParser#ignore.
    def enterIgnore(self, ctx:MiniGoParser.IgnoreContext):
        pass

    # Exit a parse tree produced by MiniGoParser#ignore.
    def exitIgnore(self, ctx:MiniGoParser.IgnoreContext):
        pass



del MiniGoParser