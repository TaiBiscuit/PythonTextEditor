import tkinter as tk


def main():
    root = tk.Tk()
    root.title("Text Editor")
    root.rowconfigure(0)
    root.columnconfigure(1)
    root.config(bg="#242424")
    text_edit = tk.Text(root, font="Helvetica 18", fg="#f2f3eb", bg="#242424")
    text_edit.pack(expand=True, fill="both") 
    text_edit.grid(row=0, column=1)

    frame = tk.Frame(root, relief=tk.RAISED, bd=2)
    frame['relief'] = 'flat'
    frame.grid(row=0, column=0, sticky="ns")

    """ BUTTONS """

    save_btn = tk.Button(frame, text="Save", command=test)
    open_btn = tk.Button(frame, text="Open")

    save_btn.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
    open_btn.grid(row=1, column=0, padx=5, sticky="ew")

    root.mainloop()



def test():
    print("YES")

main()