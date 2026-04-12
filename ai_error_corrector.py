"""
AI Error Corrector - Fixes errors before teacher sees them
"""
import re
from difflib import get_close_matches

class AIErrorCorrector:
    """
    Silently fixes common errors in the pipeline
    """
    
    def __init__(self):
        self.common_mistakes = {
            "declar": "declare",
            "declarea": "declare",  # Fix for 'declaree' issue
            "declaree": "declare",  # Fix for double 'e'
            "interger": "integer",
            "equel": "equals",
            "assigne": "assign",
            "varible": "variable"
        }
        
        self.speech_corrections = {
            "int b equal 10": "declare integer b equals 10",
            "b equal 10": "declare integer b equals 10",
            "set b to 10": "declare integer b equals 10"
        }
    
    def fix_speech_text(self, text):
        """Auto-correct common speech recognition errors"""
        corrected = text.lower()
        
        # Fix typos (multiple passes to catch cascading issues)
        for wrong, correct in self.common_mistakes.items():
            if wrong in corrected:
                corrected = corrected.replace(wrong, correct)
        
        # Handle missing "declare" keyword
        if "declare" not in corrected and "integer" in corrected:
            corrected = "declare " + corrected
        
        # Handle missing type (if numbers present but no integer/string)
        if "declare" in corrected and "integer" not in corrected and "string" not in corrected:
            # Check if there's a number in the command
            if any(char.isdigit() for char in corrected):
                # Insert 'integer' after 'declare'
                corrected = corrected.replace("declare", "declare integer", 1)
        
        # Remove any double spaces
        corrected = ' '.join(corrected.split())
        
        print(f"🔧 AI Correction: '{text}' → '{corrected}'")
        return corrected
    
    def fix_parse_error(self, error_message, tokens):
        """Suggest fixes for parse errors"""
        suggestions = []
        
        if "Unexpected token" in error_message:
            # Extract unexpected token
            match = re.search(r"Unexpected token '(\w+)'", error_message)
            if match:
                wrong_token = match.group(1)
                valid_tokens = ['DECL', 'TYPE', 'ID', 'ASSIGN', 'NUMBER']
                suggestions = get_close_matches(wrong_token, valid_tokens)
        
        return {
            "error_type": "parse_error",
            "suggestions": suggestions,
            "auto_fix_possible": len(suggestions) > 0
        }


ai_error_corrector = AIErrorCorrector()