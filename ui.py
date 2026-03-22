import tkinter as tk
from speech_to_text import get_voice
from normalizer import normalize

def handle_speech():
    raw = get_voice()
    text = normalize(raw)
    output_label.config(text=text)

root = tk.Tk()
root.title("Voice to Code")

btn = tk.Button(root, text="Speak", command=handle_speech)
btn.pack()

output_label = tk.Label(root, text="")
output_label.pack()

root.mainloop()