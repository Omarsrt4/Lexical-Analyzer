import ply.lex as lex
from colorama import Fore, Style

while True:
    Contador = 0
    tokens = (
        'NUMBER', 'OPER', 'STR', 'RESERVED', 'COM', 'VAR', 'LDEL', 'RDEL', 'EQUAL', 'TYPE'
    )

    t_NUMBER = r'\d+(\.\d+)?'
    t_OPER = r'[-+*/<>]'
    t_STR = r'("[^"]*"|\'[^\']*\')'
    t_COM = r'\#.*\#'
    t_LDEL = r'[({\[]'
    t_RDEL = r'[)}\]]'
    t_EQUAL = r'(=|\+=|-=)'

    def t_RESERVED(t):
        r'(print|scan|if|else|while|do)'
        return t

    def t_TYPE(t):
        r'(INT|int|FLO|flo|BOL|bol)'
        return t

    def t_VAR(t):
        r'[a-zA-Z]\w*'
        return t

    t_ignore = ' \t'

    def t_error(t):
        global Contador
        print(f"{Fore.RED}Error léxico{Style.RESET_ALL} Carácter inesperado: '{t.value[0]}'")
        Contador += 1
        t.lexer.skip(1)

    lexer = lex.lex()

    def count_lines(text):
        return text.count('\n') + 1

    data = input("Ingrese la cadena a escanear: ")
    lexer.input(data)

    token_list = [tok.type for tok in iter(lexer.token, None)]

    # Contador de tokens
    num_tokens = len(token_list)

    print("Seleccione los resultados deseados:\n1: Resultados simples\n2: Resultados detallados.\n3: Salir")
    op = input()   

    if op == "1":
        print("Tokens detectados:")
        print(" ".join(token_list))
        print("Errores detectados:", Contador)
        print("Total de tokens:", num_tokens)
    elif op == "2":
        lexer.lexpos = 0
        for tok in iter(lexer.token, None):
            print(f"Tipo de token: {tok.type}\nCaracteres: {tok.value}\nNúmero de línea: {tok.lineno}\n")
        print("Errores detectados:", Contador)
        print("Total de tokens:", num_tokens)
    elif op == "3":
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")