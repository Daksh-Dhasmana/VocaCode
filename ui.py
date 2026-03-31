import tkinter as tk
from speech_to_text import get_voice
from normalizer import normalize
from parser import parser
from intermediate import generate_ir
from codegen import generate_c

def handle_speech():
    output_label.config(text="Listening... Speak now!", fg="blue")
    root.update()

    try:
        raw = get_voice()
        if not raw:
            output_label.config(text="Didn't catch that. Please try again.", fg="orange")
            return
            
        text = normalize(raw)
        
        # This is the actual engine!
        tree = parser.parse(text)
        if tree is None:
            output_label.config(text=f"You said: {text}\n\nError: Syntax not recognized.", fg="red")
            return
            
        ir = generate_ir(tree)
        final_c_code = generate_c(ir)
        
        output_label.config(text=f"You said: {text}\n\nGenerated C Code:\n{final_c_code}", fg="green", justify="left")
        
    except Exception as e:
        output_label.config(text=f"Compiler Error: {e}", fg="red")

root = tk.Tk()
root.title("Voice to Code Compiler")
root.geometry("500x400")

btn = tk.Button(root, text="Speak", command=handle_speech, font=("Helvetica", 14))
btn.pack(pady=20)

output_label = tk.Label(root, text="Click 'Speak' and say a command.", font=("Courier", 12))
output_label.pack(pady=20)

root.mainloop()