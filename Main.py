import tkinter as Tkinter
from tkinter import Tk, ttk, StringVar, Label, PhotoImage, Canvas
import math
import struct


def ao_redimencionar(): # realoca todos os itens da janela
    novo_width = janela.winfo_width()
    novo_height = janela.winfo_height()
    
    entrada_de_imagem.delete("all")
    imagem = entrada_de_imagem.create_image((novo_width/2, novo_height/3), image=arquivo_de_imagem)


def check_window_size():
    current_size = (janela.winfo_width(), janela.winfo_height())
    if getattr(check_window_size, 'last_size', None) != current_size:
        ao_redimencionar()  # Chamada da função de redimensionamento
        check_window_size.last_size = current_size
    janela.after(200, check_window_size)  # Verificar a cada 200 milissegundos

def calcular(): #faz o logaritmo de fato
    campos_de_entrada = {
        base: float(ttk.Entry.get(base_entrada))
        logaritmando: float(ttk.Entry.get(logaritmando_entrada))
        precisao: int(ttk.Entry.get(precisao_spin))
    }

    Escolhas = [0,1,0.1,0.01,0.001,0.0001,0.00001]
    campos_de_entrada[precisao] = Escolhas[campos_de_entrada[precisao]]

    log = logaritmo(
        campos_de_entrada[precisao],
        campos_de_entrada[logaritmando],
        campos_de_entrada[base])
    
    log = round(log[0], int(campos_de_entrada[precisao] - 1))
    saida_de_resultados(log)

def saida_de_resultados(bagagem):
    logaritmo_saida.config(state="enable")
    logaritmo_saida.delete(0, Tkinter.END)
    logaritmo_saida.insert(0, bagagem)
    logaritmo_saida.config(state="disable")

def logaritmo(p, a, b):
    temp = []  # Saída local
    x = 1
    i = 0
    # b^x = a => log_b(a) = x
    if b**x == a:
        temp.append(x)  
    if b**x > a:
        while b**x > a: # diminui
            x -= p
            print(x)
        temp.append(x)  
    if b**1 < a:
        while b**x < a: # aumenta
            x += p
            print(x)
        temp.append(x)  
    return temp

def validar(valor): #impede inserçao de letras nos campos
    try:
        float(valor)
        return True
    except ValueError:
        return False
    
    


#Configurações da janela
janela = Tk()
janela.title("Calculadora de Logaritmos")
janela.geometry("600x450")
janela.minsize(124, 91)
janela.maxsize(4096, 2160)
janela.resizable(1, 1)
validacao = janela.register(validar)


#checagem da imagem
caminho_imagem_log = 'Log.png'
const_larg = 0

#Imagem
arquivo_de_imagem = PhotoImage(file = caminho_imagem_log)
entrada_de_imagem = Tkinter.Canvas(janela, width=600, height=400)
entrada_de_imagem.pack(expand=True)
imagem = entrada_de_imagem.create_image(((600)/2, 450/3), image=arquivo_de_imagem)

xis = 600
ipsilon = 450

#Vars/campos
LOGARITMANDO = StringVar()
BASE = StringVar()
LOGARITMO = StringVar()
PRECISAO = StringVar()

#Configuração de Botões
logaritmando_entrada = ttk.Entry(janela, textvariable = "LOGARITMANDO", validate="key", validatecommand=(validacao, "%P"))
logaritmando_entrada.place(x=373,y=142,height=50,width=60)
logaritmando_entrada.config(font=25)

base_entrada = ttk.Entry(janela, textvariable = "BASE", validate="key", validatecommand=(validacao, "%P"))
base_entrada.place(x=335,y=205,height=50,width=50)
base_entrada.config(font=25)

logaritmo_saida = ttk.Entry(janela, textvariable = 'LOGARITMO', state= "disable")
logaritmo_saida.place(x=250,y=300,height=35,width=120)
logaritmo_saida.config(font=15)

texto_log = ttk.Label(janela,text="Resultado:")
texto_log.place(x=190, y=310)

precisao_spin = Tkinter.Spinbox(janela, from_=1, to=5)
precisao_spin.place(x=139, y=80, width=26)

texto_ps = ttk.Label(janela,text="Precisão(casas decimais)")
texto_ps.place(x=4, y=80)

calcular_botao = ttk.Button(janela, text="calcular", command=calcular)
calcular_botao.place(x=272, y=260)





#fim do progama

janela.after(200, check_window_size)
janela.mainloop()


