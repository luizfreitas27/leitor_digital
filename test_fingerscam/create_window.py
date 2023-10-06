from tkinter import *
from .fonts import *
import time


class Aplication():

    ### Initialization
    def __init__(self):
        self.root = Tk()
        self.config_tela()
        self.frames()
        self.input()
        self.imagem_logo()


        self.root.mainloop()
        
        

        
        
    def config_tela(self):

        ### Configs basicas da tela
        self.root.geometry("1920x1080")
        self.root.title('Aplication')
        self.root.configure(background="black")
        self.root.maxsize(width=1920, height=1080)
        self.root.minsize(width=900, height=700)
        

    def frames(self):

        ### Tela de imagem da pessoa
        self.frame_foto = Frame(self.root, bg="white")
        self.frame_foto.place(relx= 0.44 ,rely= 0.3, width=250, height=300)
        
        ### Caixa de input nome
        self.frame_input = Frame(self.root, bg="black")
        self.frame_input.place(relx= 0.44 ,rely= 0.65, width=400, height=200)
           

    def imagem_logo(self):

        ### Logo empresa
        self.my_image = PhotoImage(file="/home/projexln01/Desktop/leitor_digital/assets/images/Logo_Projex_71x66.5.png")
        self.imagemFinal = Label(self.root, image=self.my_image, bg="black")
        self.imagemFinal.place(relx=0.45, rely=0.00, width=200, height=200)

    
    def input(self):

        ### Input nome funcionario
        self.label_nome = Label(self.frame_input,text="User    ",font=fonte(), bg="black", fg="white")
        self.label_nome.grid(column=1, row=0)
        self.input_nome = Entry(self.frame_input, border=0)
        self.input_nome.grid(column=2, row=0)
        self.botao_nome = Button(self.frame_input, text="Validar", command=self.root.destroy, bg="white", font=fonte2(), bd=0)
        self.botao_nome.place(relx=0.20, rely=0.5, width=100, height=40)

        
    
            
    

        
    