def generate_c(ir):
    lines = ir.strip().split('\n')
    c_lines = []
    declared = set()

    c_lines.append("#include <stdio.h>")
    c_lines.append("int main() {")

    for line in lines:
        line = line.strip()
        if not line:
            continue

        if line.startswith("print "):
            var = line.split()[1]
            c_lines.append(f'    printf("%d\\n", {var});')

        elif "=" in line:
            var, val = line.split('=', 1)
            var = var.strip()
            val = val.strip()

            if var not in declared:
                c_lines.append(f"    int {var} = {val};")
                declared.add(var)
            else:
                c_lines.append(f"    {var} = {val};")

    c_lines.append("    return 0;")
    c_lines.append("}")

    return "\n".join(c_lines)