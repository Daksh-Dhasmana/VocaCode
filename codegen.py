def generate_c(ir):
    lines = ir.strip().split('\n')
    c_lines = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        if line.startswith("print "):
            var = line.split(" ")[1]
            c_lines.append(f'printf("%d\\n", {var});')
        elif "=" in line:
            var, val = line.split('=', 1)
            c_lines.append(f"int {var.strip()} = {val.strip()};")
    return "\n".join(c_lines)
