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
    'let': 'LET'
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
    'COL',
    'SEMCOL'
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
t_COL = r':'
t_SEMCOL = r';'

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

while 1:
    try:
        s = raw_input('swift 4.1 > ')
    except EOFError:
        break
    if not s:
        continue
    print(s)
    lexer.input(s)
    for token in lexer:
        print(token)
    print()