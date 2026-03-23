temp_count = 0

def new_temp():
    global temp_count
    temp_count += 1
    return f"t{temp_count}"

def generate_ir(tree):
    if not tree:
        return ""

 
    if tree[0] == 'program':
        return "\n".join(generate_ir(stmt) for stmt in tree[1])

    elif tree[0] == 'assign':
        expr_code, result = generate_ir(tree[2])
        return expr_code + f"\n{tree[1]} = {result}"

 
    elif tree[0] == 'print':
        return f"print {tree[1]}"

 
    elif tree[0] == 'binop':
        op_map = {
            'plus': '+',
            'minus': '-',
            'multiply': '*',
            'divide': '/'
        }

        left_code, left = generate_ir(tree[2])
        right_code, right = generate_ir(tree[3])

        temp = new_temp()
        op = op_map.get(tree[1], tree[1])  

        code = ""
        if left_code:
            code += left_code + "\n"
        if right_code:
            code += right_code + "\n"

        code += f"{temp} = {left} {op} {right}"

        return code, temp


    elif tree[0] == 'number':
        return "", str(tree[1])


    elif tree[0] == 'id':
        return "", str(tree[1])

    return ""