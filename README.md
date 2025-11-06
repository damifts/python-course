# python-course
Repository con esercizi e appunti del corso di Python.

## Demo Tkinter

Esempio minimale di GUI usando Tkinter in `demo/main.py`.

Esecuzione (Windows PowerShell):

```powershell
python .\demo\main.py
```

Oppure:

```powershell
python -m demo.main
```

Requisiti: Python 3.8+ (Tkinter è incluso nella distribuzione standard di Python).

Nota di sicurezza: per evitare che la GUI parta involontariamente quando il
modulo viene importato, `demo/main.py` dispone della guardia standard
`if __name__ == "__main__"`. Se vuoi eseguire il file direttamente in
VS Code usa il pulsante "Run" o il terminale integrato (vedi sotto).
