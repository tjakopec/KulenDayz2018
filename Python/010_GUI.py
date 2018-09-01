from tkinter import Tk, Label, Button, Entry, StringVar
import KulenDayz as k
#KLASA
class Prozor:
    #KONSTRUKTOR
    def __init__(self, master):
        self.master = master
        master.title("Evo prozora")

        # UNOSNO POLJE
        self.unos = Entry(root)
        self.unos.pack()
        self.unos.focus_set()

        # GUMB
        self.btnPozdravi = Button(
            master,
            text="Prosti broj?",
            fg="#0000ff",
            command=self.btnPozdravi_click)
        self.btnPozdravi.pack()

        # LABELA ZA PRIKAZ REZULTATA
        self.labela_text = StringVar()
        self.labela_text.set("Ovako gradimo GUI")
        self.labela = Label(master, textvariable=self.labela_text)
        self.labela.pack()

    # EVENT funckija, malo šaram imenovanjem. Detalji o imenovanju https://www.python.org/dev/peps/pep-0008/
    def btnPozdravi_click(self):
        try:
            self.labela_text.set(
                "broj" +
                ( " je " if k.prostiBroj(int(self.unos.get())) else " nije ") +
                "prosti broj"
                )
        except ValueError:
            self.labela_text.set("Unesite cijeli broj veći od 0")
        
#nova instanca Thinkera
root = Tk()
prozor = Prozor(root)
root.mainloop()
