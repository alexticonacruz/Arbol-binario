import tkinter as tk

from tkinter import *
class inter():
    def __init__(self):
        self.root = Tk()
        self.frame1 = Frame(self.root)
        
        self.btnGuardar = Button(self.frame1,text="guardar",command=self.guardar).grid(row=0,column=0)
        self.btnGuardar = Button(self.frame1,text="borrar",command=self.borrar).grid(row=0,column=1)
        self.canvas = Canvas(self.frame1, width=600, height=400, background="black")
        self.canvas.grid(row=1,column=0)
        
        self.frame1.pack()
        
        self.root.mainloop()
    def guardar(self):
        self.canvas.create_line(200,10,280,100, fill="white")
        self.canvas.create_oval(250,10,300,50, outline="white")
    def borrar (self):
        #self.canvas.create_line(200,10,280,100, fill="black")
        self.canvas = None
        self.canvas = Canvas(self.frame1, width=600, height=400, background="black")
        self.canvas.grid(row=1,column=0)
        
inte = inter()
        

# class Aplicacion:
#     def __init__(self):
#         self.ventana1=tk.Tk()
#         self.canvas1=tk.Canvas(self.ventana1, width=600, height=400, background="black")
#         self.canvas1.grid(column=0, row=0)
#         #self.canvas1.create_line(0, 0, 100,50, fill="white")
#         # self.canvas1.create_rectangle(150,10, 250,110, fill="white")
#         # self.canvas1.create_oval(300,10,400,150, fill="red")
#         # self.canvas1.create_arc(420,10,550,110, fill="yellow", start=180, extent=90)
#         # self.canvas1.create_rectangle(150,210, 250,310, outline="white")
#         self.canvas1.create_oval(150,10,300,150, outline="red") # A => 150 , B => 10 , C => 300, D => 150
#         self.canvas1.create_line(225,150,225,200, fill="white")
#         # self.canvas1.create_arc(420,210,550,310, outline="yellow", start=180, extent=90)        
#         self.ventana1.mainloop()
#         btn = tk.Button(self.ventana1,text="mostrar",command=self.creacion).grid(column=0, row=1)
#     def creacion (self) :
#         self.canvas1.create_line(0,10,50,100, fill="white")

# aplicacion1=Aplicacion()
# aplicacion1.creacion()