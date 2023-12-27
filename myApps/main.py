import tkinter as tk
from tkinter import ttk

class App():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('350x200')
        self.root.title('Text App')
        self.mainframe = tk.Frame(self.root, background='#fff')
        self.mainframe.pack(fill='both', expand=True)

        self.text = ttk.Label(self.mainframe, text='Hello World', background='#fff', font=('Poppins', 13))
        self.text.grid(row=0, column=0 )

        self.set_text_field = ttk.Entry(self.mainframe)
        self.set_text_field.grid(row=1, column=0, pady=10, sticky='NWES' )
        self_text_button = ttk.Button(self.mainframe, text='Set Text', command=self.set_text)
        self_text_button.grid(row=1, column=1, pady=10)

        color_option = ['red', 'blue', 'green', 'black']
        self.set_color_field = ttk.Combobox(self.mainframe, value=color_option)
        self.set_color_field.grid(row=2, column=0, sticky='NEWS', pady=10)
        self_color_button = ttk.Button(self.mainframe, text='Set Color', command=self.set_color)
        self_color_button.grid(row=2, column=1, pady=10)

        self.reverse_text = ttk.Button(self.mainframe, text="Reverse Text", command=self.reverse)
        self.reverse_text.grid(row=3, column=0, pady=10, sticky='NEWS')
        
        self.root.mainloop()
        return

    def set_text(self):
        newtext = self.set_text_field.get()
        self.text.config(text=newtext)

    def set_color(self):
        newcolor = self.set_color_field.get()
        self.text.config(foreground=newcolor)

    def reverse(self):
        newtext = self.text.cget('text')
        reversed = newtext[::-1]
        self.text.config(text=reversed)

if __name__ == '__main__':
    App()