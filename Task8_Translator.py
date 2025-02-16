#Purpose: Translate from English to another language
#Used: Python lists, translator library, and GUI widget (label, text area, combo box, and button)
#Created By: Monique Priyan Dhanushkodi
#Created On: February 15, 2025

import tkinter as tk
from tkinter import ttk

from translate import Translator

window = tk.Tk()
window.title("Translator App")


window.geometry("800x500")
#window.config(bg="light grey")

def when_click():
    user_typed = user_text.get("1.0", tk.END)
    user_selected = combo_box.get()
    
    translate_client = Translator(to_lang=user_selected)
    result = translate_client.translate(user_typed)
    
    user_translation.delete("1.0", tk.END)
    user_translation.insert(tk.END, result)
    #user_translation.config(state=tk.DISABLED)

input_label = tk.Label(window, text="Enter text to be translated: ")
input_label.place(x=20, y=100)

user_text = tk.Text(window, width=50, height=5)
user_text.place(x=200, y=80)

select_label =  tk.Label(window, text="Select Language: ")
select_label.place(x=20, y=190)

languages = ["English", "Spanish", "French", "Chinese", "Tamil", "Japanese"]
combo_box = ttk.Combobox(window, values=languages)
combo_box.set(languages[0])
combo_box.place(x=200, y=190)

translate_button = tk.Button(window, text="Translate", command=when_click)
translate_button.place(x=450, y=190)

output_label = tk.Label(window, text="Translation: ")
output_label.place(x=20, y=280)

user_translation = tk.Text(window, width=50, height=5)
user_translation.place(x=200, y=260)

window.mainloop()
