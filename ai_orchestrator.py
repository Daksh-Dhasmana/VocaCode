import os
import json
import re
from google import genai
from google.genai import types

class AIVocaCode:
    """
    AI-powered integration using Google Gemini
    It translates natural speech to VocaScript DSL and provides explanations.
    """
    
    def __init__(self):
        print("🤖 Initializing Gemini AI...")
        self.api_key = os.getenv("GEMINI_API_KEY", "")
        if self.api_key:
            self.client = genai.Client(api_key=self.api_key)
        else:
            print("⚠️ No GEMINI_API_KEY found. AI features will be mocked unless initialized.")
            self.client = None

    def _preprocess(self, text):
        """Fix common input issues before sending to Gemini."""
        
        # Split on commas or 'and' to process each statement individually
        parts = [p.strip().rstrip('.') for p in re.split(r',| and ', text) if p.strip()]
        
        fixed = []
        declared_vars = set()
        
        for part in parts:
            part = part.lower().strip()
            
            # Already correct
            if part.startswith("declare integer"):
                var = part.split()[2] if len(part.split()) > 2 else None
                if var:
                    declared_vars.add(var)
                fixed.append(part)
            
            # Has 'declare' but missing 'integer'
            elif part.startswith("declare ") and "integer" not in part:
                part = part.replace("declare ", "declare integer ", 1)
                var = part.split()[2] if len(part.split()) > 2 else None
                if var:
                    declared_vars.add(var)
                fixed.append(part)
            
            # Looks like 'x equals 5' — new variable, add declare integer
            elif re.match(r'^[a-z_]\w*\s+equals\s+\d+$', part):
                var = part.split()[0]
                if var not in declared_vars:
                    part = "declare integer " + part
                    declared_vars.add(var)
                fixed.append(part)

            # Looks like 'x equals y plus z' — new variable, add declare integer
            elif re.match(r'^[a-z_]\w*\s+equals\s+[a-z_]\w*\s+plus\s+[a-z_]\w*$', part):
                var = part.split()[0]
                if var not in declared_vars:
                    part = "declare integer " + part
                    declared_vars.add(var)
                fixed.append(part)
            
            # print statement — leave as is
            elif part.startswith("print"):
                fixed.append(part)
            
            # Anything else — pass through
            else:
                fixed.append(part)
        
        return ", ".join(fixed)

    def enhance_speech_output(self, raw_text):
        """
        Translates raw speech into VocaScript DSL and generates JSON structural info.
        """
        print("🤖 AI: Interpreting user intent with Gemini...")
        
        if not self.client:
            return self._mock_fallback(raw_text)

        # Pre-process: normalize input before sending to Gemini
        raw_text = self._preprocess(raw_text)
        print(f"🔧 Preprocessed input: {raw_text}")
            
        prompt = f"""
        You are an advanced AI compiler assistant. The user provided this input: '{raw_text}'
        Translate this input into a strict domain specific language called VocaScript.
        
        VocaScript supports ONLY these EXACT formats (all lower case):
        - declare integer [var] equals [num]
        - declare integer [var] equals [var] plus [var]
        - print [var or num]
        - loop [var] from [num] to [num]
            ...
          endloop
        - if [var] [greater or less] [num] then
            ...
          endif
        - [var] equals [var] plus [var]
        - [var] equals [num or var]
        
        Important Rules: 
        1. Keep it strictly matching the DSL syntax.
        2. Put one statement per line. No extra punctuation.
        3. ALWAYS use 'declare integer' for every new variable, never just 'declare' alone.
        4. ALWAYS declare ALL variables mentioned before using them, even if the user did not explicitly say 'declare'.
        5. NEVER output bare assignments like 'x equals 5' for new variables — always use 'declare integer x equals 5'.
        6. The ONLY time you use '[var] equals [expr]' is when reassigning an already declared variable.

        Provide a structured JSON output with exactly this schema:
        {{
            "intent": "Short summary of what user wants to do",
            "voca_script": "The strictly formatted VocaScript string",
            "ast_json": {{"type": "preview_ast_object"}},
            "explanation": "Brief explanation of the translation and choices",
            "confidence": 0.95
        }}
        """

        try:
            response = self.client.models.generate_content(
                model='gemini-2.5-flash',
                contents=prompt,
                config=types.GenerateContentConfig(
                    response_mime_type="application/json",
                )
            )
            data = json.loads(response.text)
            
            return {
                "original": raw_text,
                "enhanced": data.get("voca_script", raw_text).strip(),
                "intent": data.get("intent", "Unknown"),
                "ast_json": data.get("ast_json", {}),
                "explanation": data.get("explanation", ""),
                "confidence": data.get("confidence", 0.9)
            }
        except Exception as e:
            print(f"⚠️ Gemini processing failed: {e}")
            return self._mock_fallback(raw_text)

    def _mock_fallback(self, text):
        return {
            "original": text,
            "enhanced": text,
            "intent": "Fallback Mode",
            "ast_json": {},
            "explanation": "API Key missing or error occurred. Returning verbatim.",
            "confidence": 0.0
        }

# Singleton instance
ai_orchestrator = AIVocaCode()