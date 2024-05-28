import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

def main():
    root = tk.Tk()
    root.title("Text Editor")
    root.rowconfigure(0)
    root.columnconfigure(1)
    text_edit = tk.Text(root, font="Helvetica 18")
    text_edit.pack(expand=True, fill="both") 
    text_edit.grid(row=0, column=1)

    frame = tk.Frame(root, relief=tk.RAISED, bd=2)
    frame['relief'] = 'flat'
    frame.grid(row=0, column=0, sticky="ns")

    """ BUTTONS """

    save_btn = tk.Button(frame, text="Save", command= lambda: save_file(root, text_edit))
    open_btn = tk.Button(frame, text="Open", command= lambda: open_file(root, text_edit))

    save_btn.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
    open_btn.grid(row=1, column=0, padx=5, sticky="ew")

    """ SHORTKEYS """

    root.bind("<Control-s>", lambda i: save_file(root, text_edit))
    root.bind("<Control-o>", lambda i: open_file(root, text_edit))   

    root.mainloop()



def open_file(window, text_edit):
    filepath = askopenfilename(filetypes=[("Text Files", "*.txt")])
    if not filepath:
        return
    text_edit.delete(1.0, tk.END)
    with open(filepath, "r") as file:
        content = file.read()
        text_edit.insert(tk.END, content)
    window.title(f"Open File: {filepath}")

def save_file(window, text_edit):
    filepath = asksaveasfilename(filetypes=[("Text Files", "*.txt")])
    if not filepath:
        return
    with open(filepath, "w") as file:
        content = text_edit.get(1.0, tk.END)
        file.write(content)
    window.title(f"Open File: {filepath}")





main()