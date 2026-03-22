def generate_ir(tree):
    if not tree:
        return ""
    if tree[0] == 'program':
        return "\n".join(generate_ir(stmt) for stmt in tree[1])
    elif tree[0] == 'assign':
        return f"{tree[1]} = {generate_ir(tree[2])}"
    elif tree[0] == 'print':
        return f"print {tree[1]}"
    elif tree[0] == 'binop':
        op_map = {'plus': '+', 'minus': '-', 'multiply': '*', 'divide': '/'}
        return f"{generate_ir(tree[2])} {op_map[tree[1]]} {generate_ir(tree[3])}"
    elif tree[0] == 'number':
        return str(tree[1])
    elif tree[0] == 'id':
        return str(tree[1])
    return ""
