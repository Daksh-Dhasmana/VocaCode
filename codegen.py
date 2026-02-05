def generate_c(ir):
    var,val = ir.split('=')
    return f"int {var.strip()} = {val.strip()};"
