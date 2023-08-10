import tkinter as tk
from tkinter.filedialog import asksaveasfilename, askopenfilename

current_file = None

#Button functionality
def open_file(txt_edit, window):
    global current_file
    filepath = askopenfilename(filetypes=[('Text files','*.txt'), ('All file', '*.*')])
    if not filepath:
        return
    txt_edit.delete(1.0, tk.END)
    with open(filepath, 'r') as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    window.title(f'Text Editor - {filepath}')
    current_file = filepath
    

def create_new_file(txt_edit, window):
    txt_edit.delete(1.0, tk.END)
    global current_file
    current_file = None
    window.title(f'Text Editor - New File')

def save_file(txt_edit, window):
    global current_file
    filepath = asksaveasfilename(filetypes=[('Text files','*.txt'), ('All file', '*.*')])
    if not filepath:
        return
    with open(filepath, 'w') as output_file:
        text = txt_edit.get(1.0, tk.END)
        output_file.write(text)
    window.title(f'Text Editor - {filepath}')
    current_file = filepath

def text_editor():
    # Window Settings
    window = tk.Tk()
    window.title('Text Editor')
    window.rowconfigure(0, minsize=800, weight=1)
    window.columnconfigure(1, minsize=800, weight=1)

    # Create Window Features
    txt_edit = tk.Text(window) # Text field on window
    fr_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)

    # Making buttons
    btn_open = tk.Button(fr_buttons, text='Open', command=lambda:open_file(txt_edit,window))
    btn_new = tk.Button(fr_buttons, text='New', command=lambda:create_new_file(txt_edit,window))
    btn_save = tk.Button(fr_buttons, text='Save', command=lambda:save_file(txt_edit, window))


    # Adding to the screen
    btn_open.grid(row=0,column=0,sticky='ew', padx=5, pady=5)
    btn_new.grid(row=1,column=0,sticky='ew', padx=5, pady=5)
    btn_save.grid(row=2, column=0, sticky='ew', padx=5, pady=5)

    fr_buttons.grid(row=0, column=0, sticky='ns')
    txt_edit.grid(row=0, column=1, sticky='nsew')

    window.mainloop()

if __name__ == '__main__':
    text_editor()