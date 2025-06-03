import tkinter as tk


class Interface:
    def __init__(self):
        self.start()

    def pokaz_temp(temp):
        None
        #wynik_label.config(text=f"Aktualna temperatura: {connAPI.get_respone("Brodnica", "PL")}°C")

    def start(self):
        root = tk.Tk()
        root.title("Pogoda")

        pokaz_button = tk.Button(root, text="Pokaż temperaturę", command=self.pokaz_temp)
        pokaz_button.pack()

        wynik_label = tk.Label(root, text="")
        wynik_label.pack()

        root.mainloop()
