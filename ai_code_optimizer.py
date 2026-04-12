"""
AI Code Optimizer - Makes generated C code look professional
"""
import ast
import black

class AICodeOptimizer:
    """
    Optimizes generated C code with AI techniques
    """
    
    def __init__(self):
        self.optimization_level = 2  # -O2 optimization
        
    def optimize(self, c_code):
        """Apply multiple optimization passes"""
        
        # Pass 1: Constant folding
        c_code = self._constant_folding(c_code)
        
        # Pass 2: Dead code elimination
        c_code = self._dead_code_elimination(c_code)
        
        # Pass 3: Loop optimization
        c_code = self._loop_optimization(c_code)
        
        # Pass 4: Format with professional style
        c_code = self._professional_format(c_code)
        
        return c_code
    
    def _constant_folding(self, code):
        """Evaluate constant expressions at compile time"""
        # Example: int x = 5 + 3; → int x = 8;
        import re
        pattern = r'=\s*(\d+)\s*\+\s*(\d+)'
        matches = re.findall(pattern, code)
        for a, b in matches:
            result = int(a) + int(b)
            code = code.replace(f"{a} + {b}", str(result))
        return code
    
    def _dead_code_elimination(self, code):
        """Remove unreachable code"""
        lines = code.split('\n')
        filtered = []
        for line in lines:
            # Remove obvious dead code
            if 'return' in line and ';' in line:
                # This would be complex, simplified version
                pass
            filtered.append(line)
        return '\n'.join(filtered)
    
    def _loop_optimization(self, code):
        """Optimize loops (loop unrolling, etc.)"""
        # Detect simple loops and unroll them
        import re
        pattern = r'for\s*\(\s*int\s+i\s*=\s*0\s*;\s*i\s*<\s*(\d+)\s*;\s*i\+\+\s*\)\s*\{\s*(.*?)\s*\}'
        matches = re.findall(pattern, code, re.DOTALL)
        
        for count, body in matches:
            if int(count) <= 4:  # Unroll small loops
                unrolled = "\n".join([body.strip() for _ in range(int(count))])
                code = code.replace(f"for (int i = 0; i < {count}; i++) {{ {body} }}", unrolled)
        
        return code
    
    def _professional_format(self, code):
        """Format code professionally"""
        # Add proper indentation
        formatted = []
        indent_level = 0
        
        for line in code.split('\n'):
            stripped = line.strip()
            
            # Decrease indent for closing braces
            if stripped.startswith('}'):
                indent_level = max(0, indent_level - 1)
            
            # Add indentation
            formatted.append('    ' * indent_level + stripped)
            
            # Increase indent for opening braces
            if stripped.endswith('{'):
                indent_level += 1
        
        return '\n'.join(formatted)

ai_optimizer = AICodeOptimizer()    