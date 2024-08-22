from enum import Enum
import sys
S = sys.stdin.read()

ParserState = Enum('ParserState', ['STATEMENT', 'CONDITION'])

checkpoints = []
conditions = []
parser_state = ParserState.STATEMENT

for token in filter(lambda x: x!='', S.strip().split()):
    if parser_state == ParserState.STATEMENT:
        if token == "if":
            parser_state = ParserState.CONDITION
        elif token == "checkpoint":
            checkpoints.append(tuple(conditions))
