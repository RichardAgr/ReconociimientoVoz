import tkinter as tk
import customtkinter as ctk
import tkinter as tk
from PIL import ImageTk, Image
g1=468;
def obtener_coordenadas(event):
    global g1
    x = event.x
    y = event.y
    print(f"g.addVertex(Vertexx('e{g1}', {x}, {y}))")
    g1 += 1

ven = ctk.CTk()
can = ctk.CTkCanvas(ven, width="1300",height="750")
can.pack()
ima = Image.open("imagenes/mapaCocha2.png")
nuevaima = ima.resize((1275, 800))

gf = ImageTk.PhotoImage(nuevaima)

imagen = tk.PhotoImage("imagenes/mapaCocha2.png")
can.create_image(10,10, anchor=tk.NW, image = gf)
can.bind("<Button-1>", obtener_coordenadas)
ven.mainloop()

if __name__ == "__main__":
    print("holis")