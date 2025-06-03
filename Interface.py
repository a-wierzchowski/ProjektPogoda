import tkinter as tk
from tkinter import ttk


class Interface:
    def __init__(self):
        self.start()

    def pokaz_temp(temp):
        None
        #wynik_label.config(text=f"Aktualna temperatura: {connAPI.get_respone("Brodnica", "PL")}°C")

    def start(self):
        root = tk.Tk()
        root.title("Pogoda")
        root.geometry('600x400+50+50')
        root.resizable(False, False)
        root.iconbitmap('./assets/icon.ico')

        wynik_label = ttk.Label(root, text="Podaj API do OpenWeatherMap")
        wynik_label.pack()

        name_entry = ttk.Entry(root)
        name_entry.pack()

        pokaz_button = ttk.Button(root, text="Dalej", command=self.pokaz_temp)
        pokaz_button.pack()

        agreement_var = tk.BooleanVar()

        checkbox = ttk.Checkbutton(
            root,
            text='Zapamiętaj',
            variable=agreement_var
        )
        checkbox.pack()



        root.mainloop()
