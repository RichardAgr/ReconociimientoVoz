from tkinter import *
from interfazProyecto import *

def centrarVentana(ventana):
    ventana.update_idletasks()
    ancho = ventana.winfo_width()
    alto = ventana.winfo_height()
    x = (ventana.winfo_screenwidth() // 2) - (ancho // 2)
    y = (ventana.winfo_screenheight() // 2) - (alto // 2)
    ventana.geometry('{}x{}+{}+{}'.format(ancho, alto, x, y))


def run():
    raiz = Tk()
    raiz.wm_title("Reconocimiento de voz")
    app = interfazProyecto(raiz);
    centrarVentana(raiz)
    raiz.mainloop()
    
run()