from tkinter import *
from PIL import ImageTk,Image
from os import *
import csv

class interfazProyecto(Frame):
    def __init__(self, master=None):
        super().__init__(master, width=1300,height=700)
        self.master = master
        self.pack()
        self.crearMapa()
        self.coordenadas = []
        
    def crearMapa(self):
        carpetaImagen = path.dirname(__file__)
        rutaImagen = path.join(carpetaImagen,"imagen")

        self.mapaCocha = ImageTk.PhotoImage(Image.open(path.join(rutaImagen,"mapaCocha2.jpg")).resize((1000,700)))
        
        frameMapa = Frame(self)
        frameMapa.place(x=0,y=0,width=1000,height=700)
        
        mapa = Label(frameMapa,image=self.mapaCocha)
        mapa.place(x=0,y=0,width=1000,height=700)
        
        mapa.bind("<Button-1>", self.obtener_puntos)
        
    def obtener_puntos(self, event):
        print( f"{event.x},{event.y}")

