# Marco Lopez - A01203445

import sys

if sys.version_info[0] >= 3:
    raw_input = input

reserved_words = {
    'readLine': 'READLINE',
    'print': 'PRINT',
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
    'var': 'VAR',
    'let': 'LET',
    'func': 'FUNC',
    'return': 'RETURN',
    'or': 'OR',
    'and': 'AND',
    'not': 'NOT'
}

tokens = (
    'ID',
    'NUMBER',
    'STRING',
    'BOOL',
    'LINE_COMMENT',
    'BLOCK_COMMENT',
    'POINT',
    'EQ',
    'NEQ',
    'GT',
    'LT',
    'GOET',
    'LOET',
    'ASSIGN',
    'SUM',
    'SUBST',
    'PROD',
    'DIV',
    'LPARENT',
    'RPARENT',
    'LBRACK',
    'RBRACK',
    'SEMCOL',
    'COMA'
) + tuple(reserved_words.values())

# Tokens
def t_BOOL(t):
    r'(true|false)'
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved_words.get(t.value, 'ID')
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

line = r'.*'

t_STRING = r'("' + line + '"|\'' + line + '\')'
#t_BOOL = r'(true|false)'
t_LINE_COMMENT = r'//' + line
t_BLOCK_COMMENT = r'/\*' + line + '\*/'
t_READLINE = r'readLine'
t_PRINT = r'print'
t_IF = r'if'
t_ELSE = r'else'
t_WHILE = r'while'
t_POINT = r'\.'
t_EQ = r'=='
t_NEQ = r'!='
t_GT = r'>'
t_LT = r'<'
t_GOET = r'>='
t_LOET = r'<='
t_ASSIGN = r'='
t_SUM = r'\+'
t_SUBST = r'-'
t_PROD = r'\*'
t_DIV = r'/'
t_LPARENT = r'\('
t_RPARENT = r'\)'
t_LBRACK = r'\{'
t_RBRACK = r'\}'
t_SEMCOL = r';'
t_COMA = r','

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

t_ignore = " \t"

# Build the lexer
import ply.lex as lex
lexer = lex.lex()

# Parsing rules

"""
precedence = (
    ('left', '+', '-'),
    ('left', '*', '/'),
    ('right', 'UMINUS'),
)
"""

# dictionary of names
names = {}

def p_line(p):
    """codeLine : suite
    """
    pass

def p_suite(p):
    """suite    : stmt
                | stmt suite
    """
    pass

def p_stmt(p):
    """stmt : exprStmt
            | declar SEMCOL
            | call SEMCOL
            | selectionStmt
            | iterationStmt
            | returnStmt SEMCOL
            | inputStmt SEMCOL
            | outputStmt SEMCOL
            | lineComment
            | blockComment
    """
    pass

def p_declar(p):
    """declar   : varDeclar SEMCOL
                | funcDeclar
    """
    pass

def p_var_declar(p):
    """varDeclar    : VAR ID ASSIGN STRING
                    | LET ID ASSIGN STRING
                    | ID ASSIGN exprStmt
    """
    pass

def p_func_declar(p):
    """funcDeclar   : FUNC ID LPARENT RPARENT LBRACK suite RBRACK
                    | FUNC ID LPARENT params RPARENT LBRACK suite RBRACK
    """
    pass

def p_params(p):
    """params   : paramsList
    """
    pass

def p_params_list(p):
    """paramsList   : ID COMA paramsList
                    | ID
    """
    pass

def p_call(p):
    """call : ID
            | ID POINT call
            | ID LPARENT RPARENT
            | ID LPARENT params RPARENT
            | call POINT call
    """
    pass

def p_expr_stmt(p):
    """exprStmt : simpleExpr
    """
    pass

def p_selection_stmt(p):
    """selectionStmt    : IF LPARENT simpleExpr RPARENT LBRACK suite RBRACK
                        | IF LPARENT simpleExpr RPARENT LBRACK suite RBRACK ELSE LBRACK suite RBRACK
    """
    pass

def p_iteration_stmt(p):
    """iterationStmt    : WHILE LPARENT simpleExpr RPARENT LBRACK suite RBRACK
    """
    pass

def p_return(p):
    """returnStmt   : RETURN
                    | RETURN simpleExpr
    """
    pass

def p_simple_expr(p):
    """simpleExpr   : simpleExpr OR andExpr
                    | andExpr
    """
    pass

def p_and_expr(p):
    """andExpr  : andExpr AND unaryRelExpr
                | unaryRelExpr
    """
    pass

def p_unary_rel_expr(p):
    """unaryRelExpr : NOT unaryRelExpr
                    | relExpr
    """
    pass

def p_rel_expr(p):
    """relExpr  : sumExpr relop sumExpr
                | sumExpr
    """
    pass

def p_relop(p):
    """relop    : LOET
                | LT
                | GOET
                | GT
                | EQ
                | NEQ
    """
    pass

def p_sum_expr(p):
    """sumExpr  : sumExpr sumop term
                | term
    """
    pass

def p_sumop(p):
    """sumop    : SUM
                | SUBST
    """
    pass

def p_term(p):
    """term : term mulop opElement
            | opElement
    """
    pass

def p_op_element(p):
    """opElement    : call
                    | NUMBER
    """
    pass

def p_mulop(p):
    """mulop    : PROD
                | DIV
    """
    pass

def p_input_stmt(p):
    """inputStmt : READLINE LPARENT RPARENT
    """
    pass

def p_output_stmt(p):
    """outputStmt : PRINT LPARENT STRING RPARENT
    """
    pass

def p_line_comment(p):
    """lineComment  : LINE_COMMENT
    """
    pass

def p_block_comment(p):
    """blockComment : BLOCK_COMMENT
    """
    pass

def p_error(p):
    if p:
        print("Syntax error at '%s'" % p.value)
    else:
        print("Syntax error at EOF")

import ply.yacc as yacc
parser = yacc.yacc()

while 1:
    try:
        s = raw_input('swift 4.1 > ')
    except EOFError:
        break
    if not s:
        continue
    print(s)
    parser.parse(s)
    """
    try:
        s = raw_input('swift 4.2 > ')
    except EOFError:
        break
    if not s:
        continue
    print(s)
    lexer.input(s)
    for token in lexer:
        print(token)
    print()
    """