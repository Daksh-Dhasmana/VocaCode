def generate_ir(tree):
    if tree[0]=='assign':
        return f"{tree[1]} = {tree[2]}"
