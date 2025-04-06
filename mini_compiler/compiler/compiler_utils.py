def generate_tokens(a, b):
    # Tokens for the equation `z = a * a + b * b - 2 * a * b`
    tokens = [
        {"value": "a", "type": "variable"},
        {"value": "*", "type": "operator"},
        {"value": "a", "type": "variable"},
        {"value": "+", "type": "operator"},
        {"value": "b", "type": "variable"},
        {"value": "*", "type": "operator"},
        {"value": "b", "type": "variable"},
        {"value": "-", "type": "operator"},
        {"value": "2", "type": "constant"},
        {"value": "*", "type": "operator"},
        {"value": "a", "type": "variable"},
        {"value": "*", "type": "operator"},
        {"value": "b", "type": "variable"},
    ]
    return tokens

def generate_symbol_table(a, b):
    # The symbol table holds variable names, types, and values
    symbol_table = [
        {"name": "a", "type": "int", "value": a},
        {"name": "b", "type": "int", "value": b},
        {"name": "z", "type": "int", "value": 0},  # z is also an integer variable
    ]
    return symbol_table

def generate_three_address_code(a, b):
    # Three-address code (TAC) for `z = a * a + b * b - 2 * a * b`
    tac = [
        f"t1 = a * a",         # t1 stores a * a
        f"t2 = b * b",         # t2 stores b * b
        f"t3 = a * b",         # t3 stores a * b
        f"t4 = 2 * t3",        # t4 stores 2 * (a * b)
        f"t5 = t1 + t2",       # t5 stores t1 + t2 (a^2 + b^2)
        f"t6 = t5 - t4",       # t6 stores t5 - t4 (a^2 + b^2 - 2ab)
        f"z = t6",             # z stores the final result
    ]
    return tac
