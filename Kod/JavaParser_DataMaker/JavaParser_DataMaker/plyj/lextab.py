# lextab.py. This file automatically created by PLY (version 3.11). Don't edit!
_tabversion   = '3.10'
_lextokens    = set(('ABSTRACT', 'AND', 'AND_ASSIGN', 'ASSERT', 'BLOCK_COMMENT', 'BOOLEAN', 'BREAK', 'BYTE', 'CASE', 'CATCH', 'CHAR', 'CHAR_LITERAL', 'CLASS', 'CONTINUE', 'DEFAULT', 'DIVIDE_ASSIGN', 'DO', 'DOUBLE', 'ELLIPSIS', 'ELSE', 'ENUM', 'EQ', 'EXTENDS', 'FALSE', 'FINAL', 'FINALLY', 'FLOAT', 'FOR', 'GTEQ', 'IF', 'IMPLEMENTS', 'IMPORT', 'INSTANCEOF', 'INT', 'INTERFACE', 'LINE_COMMENT', 'LONG', 'LSHIFT', 'LSHIFT_ASSIGN', 'LTEQ', 'MINUSMINUS', 'MINUS_ASSIGN', 'NAME', 'NATIVE', 'NEQ', 'NEW', 'NULL', 'NUM', 'OR', 'OR_ASSIGN', 'PACKAGE', 'PLUSPLUS', 'PLUS_ASSIGN', 'PRIVATE', 'PROTECTED', 'PUBLIC', 'REMAINDER_ASSIGN', 'RETURN', 'RRSHIFT', 'RRSHIFT_ASSIGN', 'RSHIFT', 'RSHIFT_ASSIGN', 'SHORT', 'STATIC', 'STRICTFP', 'STRING_LITERAL', 'SUPER', 'SWITCH', 'SYNCHRONIZED', 'THIS', 'THROW', 'THROWS', 'TIMES_ASSIGN', 'TRANSIENT', 'TRUE', 'TRY', 'VOID', 'VOLATILE', 'WHILE', 'XOR_ASSIGN'))
_lexreflags   = 64
_lexliterals  = '()+-*/=?:,.^|&~!=[]{};<>@%'
_lexstateinfo = {'INITIAL': 'inclusive'}
_lexstatere   = {'INITIAL': [('(?P<t_BLOCK_COMMENT>/\\*(.|\\n)*?\\*/)|(?P<t_NAME>[A-Za-z_$][A-Za-z0-9_$]*)|(?P<t_newline>\\n+)|(?P<t_newline2>(\\r\\n)+)|(?P<t_NUM>\\.?[0-9][0-9eE_lLdDa-fA-F.xXpP]*)|(?P<t_CHAR_LITERAL>\\\'([^\\\\\\n]|(\\\\.))*?\\\')|(?P<t_STRING_LITERAL>\\"([^\\\\\\n]|(\\\\.))*?\\")|(?P<t_ELLIPSIS>\\.\\.\\.)|(?P<t_MINUSMINUS>\\-\\-)|(?P<t_OR>\\|\\|)|(?P<t_PLUSPLUS>\\+\\+)|(?P<t_RRSHIFT_ASSIGN>>>>=)|(?P<t_ignore_LINE_COMMENT>//.*)|(?P<t_LSHIFT_ASSIGN><<=)|(?P<t_OR_ASSIGN>\\|=)|(?P<t_PLUS_ASSIGN>\\+=)|(?P<t_RRSHIFT>>>>)|(?P<t_RSHIFT_ASSIGN>>>=)|(?P<t_TIMES_ASSIGN>\\*=)|(?P<t_XOR_ASSIGN>\\^=)|(?P<t_AND>&&)|(?P<t_AND_ASSIGN>&=)|(?P<t_DIVIDE_ASSIGN>/=)|(?P<t_EQ>==)|(?P<t_GTEQ>>=)|(?P<t_LSHIFT><<)|(?P<t_LTEQ><=)|(?P<t_MINUS_ASSIGN>-=)|(?P<t_NEQ>!=)|(?P<t_REMAINDER_ASSIGN>%=)|(?P<t_RSHIFT>>>)', [None, ('t_BLOCK_COMMENT', 'BLOCK_COMMENT'), None, ('t_NAME', 'NAME'), ('t_newline', 'newline'), ('t_newline2', 'newline2'), None, (None, 'NUM'), (None, 'CHAR_LITERAL'), None, None, (None, 'STRING_LITERAL'), None, None, (None, 'ELLIPSIS'), (None, 'MINUSMINUS'), (None, 'OR'), (None, 'PLUSPLUS'), (None, 'RRSHIFT_ASSIGN'), (None, None), (None, 'LSHIFT_ASSIGN'), (None, 'OR_ASSIGN'), (None, 'PLUS_ASSIGN'), (None, 'RRSHIFT'), (None, 'RSHIFT_ASSIGN'), (None, 'TIMES_ASSIGN'), (None, 'XOR_ASSIGN'), (None, 'AND'), (None, 'AND_ASSIGN'), (None, 'DIVIDE_ASSIGN'), (None, 'EQ'), (None, 'GTEQ'), (None, 'LSHIFT'), (None, 'LTEQ'), (None, 'MINUS_ASSIGN'), (None, 'NEQ'), (None, 'REMAINDER_ASSIGN'), (None, 'RSHIFT')])]}
_lexstateignore = {'INITIAL': ' \t\x0c'}
_lexstateerrorf = {'INITIAL': 't_error'}
_lexstateeoff = {}