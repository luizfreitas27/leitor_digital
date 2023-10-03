from tkinter import *


import os

fotoApp = os.path.dirname(__file__)


class Aplication():
    def __init__(self):
        self.root = Tk()
        self.config_tela()
        self.frames()
        self.imagem_logo()


        self.root.mainloop()
        
    def config_tela(self):
        self.root.geometry("900x700")
        self.root.title('Aplication')
        self.root.configure(background="black")
        self.root.minsize(width=500, height=500)

    def frames(self):

        ### Tela de imagem da pessoa
        self.frame_foto = Frame(self.root, bg="white")
        self.frame_foto.place(relx= 0.44 ,rely= 0.3, width=250, height=300)

        self.frame_logo = Frame(self.root, bg="#c0c0c0")
        self.frame_logo.place(relx= 0.41,rely= 0.01, width= 500, height= 500)
        

    def imagem_logo(self):
        self.my_image = PhotoImage(file="/home/projexln01/Desktop/leitor_digital/assets/images/Logo_projex_Branca.png")
        self.imagemFinal = Label(self.frame_logo, image=self.my_image)
        self.imagemFinal.place(relx=0.01, rely=0.01, width=1000, height=1000)

    # def inputs(self):
    #     self.input_1 = 
        
    
    
        
