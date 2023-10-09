from tkinter import *
import sqlite3


class Funcs():

    def limpa_tudo(self):
        self.input_nome.delete(0, END)

    def conect_db(self):
        self.conn = sqlite3.connect("clientes.db")
        self.cursor = self.conn.cursor()

    def desconect_db(self):
        self.conn.close()

    def create_table(self):
        self.conect_db
        print("Conecting to database...")

        self.cursor.execute("CREATE TABLE if NOT EXISTS user")