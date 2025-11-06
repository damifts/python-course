"""
demo/main.py

Esempio minimale di GUI con Tkinter: una finestra con un contatore
e un bottone per incrementarlo.
"""
import tkinter as tk


class CounterApp:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        root.title("Demo Tkinter - Contatore")
        self.count = 0

        self.label = tk.Label(root, text="Contatore: 0", font=("Arial", 16))
        self.label.pack(padx=20, pady=10)

        self.button = tk.Button(root, text="Incrementa", command=self.increment)
        self.button.pack(pady=10)

    def increment(self) -> None:
        self.count += 1
        self.label.config(text=f"Contatore: {self.count}")


def main() -> None:
    root = tk.Tk()
    app = CounterApp(root)
    root.mainloop()


# Avvio automatico: quando VS Code esegue il file viene lanciata la GUI.
# (rimosso il guard `if __name__ == "__main__"` su richiesta didattica)
main()
