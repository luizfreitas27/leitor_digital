from tkinter import *
import time
import os

fotoApp = os.path.dirname(__file__)


class Aplication():
    def __init__(self):
        self.root = Tk()
        self.config_tela()
        self.frames()
        self.root.mainloop()
        self.botao()
        
    def config_tela(self):
        self.root.geometry("900x700")
        self.root.title('Aplication')
        self.root.configure(background="black")
        self.root.minsize(width=500, height=500)

    def frames(self):

        ### Tela de imagem da pessoa
        self.frame_1 = Frame(self.root, bg="white")
        self.frame_1.place(relx= 0.65 ,rely= 0.05, width=250, height=300)
        

        ### Tela de imagem da digital
        self.frame_2 = Frame(self.root, bg="white")
        self.frame_2.place(relx= 0.65 ,rely= 0.5, width=250, height=300)

    def botao(self):
        self.button = Button(self.frame_2, text="balblabla",command=self.root.destroy)
        self.button.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.15)
    
        

    
        
