import tkinter as tk
from tkinter import filedialog
from translate_funtion import translate_mRNA

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[('Text files', '*.txt')])
    if file_path:
        with open(file_path, 'r') as file:
            file_content = file.readlines()
            cleaned_list = [item.replace("\n", "") for item in file_content]
            result_texts = []  

            for i, item in enumerate(cleaned_list):
                stringy = translate_mRNA(item)
                result_texts.append(f"{i+1}. {stringy}")

            result_text.set('\n'.join(result_texts))

def translate_input():
    input_text = input_entry.get()
    translated_input = translate_mRNA(input_text)
    if translated_input == '':
        translated_input = 'No AS sequence found'
    result_text.set(f"Translated input: {translated_input}")

app = tk.Tk()
app.title('mRNA Translator')

open_button = tk.Button(app, text='Open File', command=open_file)
open_button.pack(pady=10)

input_label = tk.Label(app, text="Enter mRNA sequence:")
input_label.pack()

input_entry = tk.Entry(app)
input_entry.pack(pady=10)

translate_button = tk.Button(app, text='Translate Input', command=translate_input)
translate_button.pack()

result_text = tk.StringVar()
result_label = tk.Label(app, textvariable=result_text, wraplength=500, justify=tk.LEFT)
result_label.pack(padx=10, pady=10)

app.mainloop()
