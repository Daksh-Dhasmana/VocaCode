import tkinter as tk
from speech_to_text import get_voice
from normalizer import normalize

def handle_speech():
    output_label.config(text="Listening... Speak now!", fg="blue")
    root.update()

    try:
        raw = get_voice()
        text = normalize(raw)
        
        final_c_code = "int a = 10;" 
        
        output_label.config(text=f"You said: {text}\n\nGenerated C Code:\n{final_c_code}", fg="green")
        
    except Exception as e:
        output_label.config(text=f"Compiler Error: {e}", fg="red")

root = tk.Tk()
root.title("Voice to Code Compiler")
root.geometry("400x300")

btn = tk.Button(root, text="Speak", command=handle_speech, font=("Helvetica", 14))
btn.pack(pady=20)

output_label = tk.Label(root, text="Click 'Speak' and say a command.", font=("Helvetica", 12))
output_label.pack(pady=20)

root.mainloop()