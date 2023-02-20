from email.mime import image
from platform import java_ver
from struct import pack
from tkinter import *
import random
from tkinter import font
from turtle import width

#cores
cinza = "#3b3b3b"
branco = "#FFFFFF"
amarelo = "#fff873"
verde = "#34eb3d"
marrom = "#8B4513"
roxo = '#8A2BE2'
#janela
janela = Tk()
janela.title('JOGO DA FORCA')
janela.geometry('700x500')
janela.configure(bg=roxo)
#tela inicial
nome_jogo = Label(janela,text='JOGO DA FORCA',width=35,height=6,font=('ivy 25'),bg=roxo,fg=branco)
nome_jogo.place(x=20,y=90)
botao_jogar  = Button(janela,command=lambda:(iniciar(),botao_jogar.destroy()),text='JOGAR',font=('ivy 17'),width=10,height=2,bg=branco,fg=cinza)
botao_jogar.place(x=280,y=260)
def iniciar():
    global label_repetidas
    nome_jogo.destroy()
    #frames
    frame_cima = Frame(janela,width=700,height=250,bg=roxo)
    frame_cima.grid(row=0,column=0)
    frame_baixo = Frame(janela,width=700,height=250,bg=roxo)
    frame_baixo.grid(row=1,column=0)
    #botões letras
    b_a = Button(frame_baixo,text='A',command=lambda:letras('a'),width=5,height=2,relief=RAISED,font=('ivy 13'),fg=branco,bg=cinza)
    b_a.place(x=150,y=20)
    b_b = Button(frame_baixo,text='B',command=lambda:letras('b'),width=5,height=2,relief=RAISED,font=('ivy 13'),fg=branco,bg=cinza)
    b_b.place(x=210,y=20)
    b_c = Button(frame_baixo,text='C',command=lambda:letras('c'),width=5,height=2,relief=RAISED,font=('ivy 13'),fg=branco,bg=cinza)
    b_c.place(x=270,y=20)
    b_d = Button(frame_baixo,text='D',command=lambda:letras('d'),width=5,height=2,relief=RAISED,font=('ivy 13'),fg=branco,bg=cinza)
    b_d.place(x=330,y=20)
    b_e = Button(frame_baixo,text='E',command=lambda:letras('e'),width=5,height=2,relief=RAISED,font=('ivy 13'),fg=branco,bg=cinza)
    b_e.place(x=390,y=20)
    b_f = Button(frame_baixo,text='F',command=lambda:letras('f'),width=5,height=2,relief=RAISED,font=('ivy 13'),fg=branco,bg=cinza)
    b_f.place(x=450,y=20)
    b_g = Button(frame_baixo,text='G',command=lambda:letras('g'),width=5,height=2,relief=RAISED,font=('ivy 13'),fg=branco,bg=cinza)
    b_g.place(x=510,y=20)
    b_h = Button(frame_baixo,text='H',command=lambda:letras('h'),width=5,height=2,relief=RAISED,font=('ivy 13'),fg=branco,bg=cinza)
    b_h.place(x=150,y=70)
    b_i = Button(frame_baixo,text='I',command=lambda:letras('i'),width=5,height=2,relief=RAISED,font=('ivy 13'),fg=branco,bg=cinza)
    b_i.place(x=210,y=70)
    b_j = Button(frame_baixo,text='J',command=lambda:letras('j'),width=5,height=2,relief=RAISED,font=('ivy 13'),fg=branco,bg=cinza)
    b_j.place(x=270,y=70)
    b_k = Button(frame_baixo,text='K',command=lambda:letras('k'),width=5,height=2,relief=RAISED,font=('ivy 13'),fg=branco,bg=cinza)
    b_k.place(x=330,y=70)
    b_l = Button(frame_baixo,text='L',command=lambda:letras('l'),width=5,height=2,relief=RAISED,font=('ivy 13'),fg=branco,bg=cinza)
    b_l.place(x=390,y=70)
    b_m = Button(frame_baixo,text='M',command=lambda:letras('m'),width=5,height=2,relief=RAISED,font=('ivy 13'),fg=branco,bg=cinza)
    b_m.place(x=450,y=70)
    b_n = Button(frame_baixo,text='N',command=lambda:letras('n'),width=5,height=2,relief=RAISED,font=('ivy 13'),fg=branco,bg=cinza)
    b_n.place(x=510,y=70)
    b_o = Button(frame_baixo,text='O',command=lambda:letras('o'),width=5,height=2,relief=RAISED,font=('ivy 13'),fg=branco,bg=cinza)
    b_o.place(x=150,y=120)
    b_p = Button(frame_baixo,text='P',command=lambda:letras('p'),width=5,height=2,relief=RAISED,font=('ivy 13'),fg=branco,bg=cinza)
    b_p.place(x=210,y=120)
    b_q = Button(frame_baixo,text='Q',command=lambda:letras('q'),width=5,height=2,relief=RAISED,font=('ivy 13'),fg=branco,bg=cinza)
    b_q.place(x=270,y=120)
    b_r = Button(frame_baixo,text='R',command=lambda:letras('r'),width=5,height=2,relief=RAISED,font=('ivy 13'),fg=branco,bg=cinza)
    b_r.place(x=330,y=120)
    b_s = Button(frame_baixo,text='S',command=lambda:letras('s'),width=5,height=2,relief=RAISED,font=('ivy 13'),fg=branco,bg=cinza)
    b_s.place(x=390,y=120)
    b_t = Button(frame_baixo,text='T',command=lambda:letras('t'),width=5,height=2,relief=RAISED,font=('ivy 13'),fg=branco,bg=cinza)
    b_t.place(x=450,y=120)
    b_u = Button(frame_baixo,text='U',command=lambda:letras('u'),width=5,height=2,relief=RAISED,font=('ivy 13'),fg=branco,bg=cinza)
    b_u.place(x=510,y=120)
    b_v = Button(frame_baixo,text='V',command=lambda:letras('v'),width=5,height=2,relief=RAISED,font=('ivy 13'),fg=branco,bg=cinza)
    b_v.place(x=210,y=170)
    b_w = Button(frame_baixo,text='W',command=lambda:letras('w'),width=5,height=2,relief=RAISED,font=('ivy 13'),fg=branco,bg=cinza)
    b_w.place(x=270,y=170)
    b_x = Button(frame_baixo,text='X',command=lambda:letras('x'),width=5,height=2,relief=RAISED,font=('ivy 13'),fg=branco,bg=cinza)
    b_x.place(x=330,y=170)
    b_y = Button(frame_baixo,text='Y',command=lambda:letras('y'),width=5,height=2,relief=RAISED,font=('ivy 13'),fg=branco,bg=cinza)
    b_y.place(x=390,y=170)
    b_z = Button(frame_baixo,text='Z',command=lambda:letras('z'),width=5,height=2,relief=RAISED,font=('ivy 13'),fg=branco,bg=cinza)
    b_z.place(x=450,y=170)
    #imagens
    imagem1 = PhotoImage(file='img/forca1.png')
    label_foto = Label(frame_cima,image=imagem1,bg=roxo)
    label_foto.photo = imagem1
    label_foto.place(x=0,y=0)
    #palavras
    lista_de_plavras =  ['abajur','abrir', 'amar', 'amor','andar',
    'azar', 'cair', 'cantar','caviar', 'colar',
    'compor', 'condor', 'dispor', 'dividir',
    'dormir', 'estar', 'expor', 'falar', 'fazer',
    'hangar', 'horror', 'melhor', 'mexer','motor', 'prazer',
    'roedor', 'saber', 'sair',
    'senhor', 'tremor', 'abril', '', 'anel', 'animal', 'anzol',
    'avental', 'azul', 'barril', 'brasil', 'cachecol', 'cantil', 'civil',
    'coronel', 'cristal', 'cruel', 'dedal', 'final','funil', 'futebol',
    'padaria','cidade','lago']
    palavra = random.choice(lista_de_plavras)
    global casas
    casas = '_ '*len(palavra)
    casas_novas = ''
    label_casas = Label(frame_cima,text=casas,width=10,height=1,fg=marrom,bg=roxo,font=('ivy 35'),relief=FLAT,)   
    label_casas.place(x=290,y=170)
    casas = '_'*len(palavra)
    casas = list(casas)
    global contador_tentativas
    contador_tentativas = 1
    global lista_letras_repetidas
    lista_letras_repetidas = []
    def letras(letra):
        global contador_tentativas, label_repetidas
        global casas
        casas_novas = ''
        contador  = -1
        letra_jogador = letra
        if letra_jogador in palavra:
            for v in palavra:
                contador = contador+1
                if v == letra_jogador:
                    casas[contador] = v
                    casas_novas = ''.join(casas)
                    casas_final = ''
                    for l in casas_novas:
                        casas_final = casas_final+l+' '

                    label_casas['text']= casas_final
                    if '_' not in label_casas['text']:
                        label_foto.destroy()
                        frame_baixo.destroy()
                        frame_cima.destroy()
                        
                        label_vitoria = Label(janela,text='VOCÊ GANHOU',font=('ivy 25 '),bg=roxo,fg=branco,width=25)
                        label_vitoria.place(x=120,y=200)
                        b_recomecar = Button(janela,command=lambda: (iniciar(),b_recomecar.destroy(),label_vitoria.destroy()),text='CONTINUAR',bg=branco,fg=cinza,width=10,height=2,font=('ivy 17'),relief=RAISED)
                        b_recomecar.place(x=290,y=270)
        
        else:
            if letra_jogador in lista_letras_repetidas:
                return
            if letra_jogador not in lista_letras_repetidas:
                lista_letras_repetidas.append(letra_jogador,)
                label_repetidas = Label(frame_cima,text=f'repetidas: {lista_letras_repetidas}',font=('ivy 20'),bg=roxo,fg=marrom)
                label_repetidas.place(x=250,y=50)
            contador_tentativas =contador_tentativas+1
            if contador_tentativas == 2:
                imagem1['file']='img/forca2.png'
            if contador_tentativas == 3:
                imagem1['file']='img/forca3.png'
            if contador_tentativas == 4:
                imagem1['file']='img/forca4.png'
            if contador_tentativas == 5:
                imagem1['file']='img/forca5.png'
            if contador_tentativas == 6:
                imagem1['file']='img/forca6.png'
            if contador_tentativas == 7:
                imagem1['file']='img/forca7.png'
            if contador_tentativas == 8:
                frame_baixo.destroy()
                frame_cima.destroy()
                label_foto.destroy()
                label_derrota = Label(janela,text=f'A PALAVRA ERA: {palavra}',font=('ivy 25 '),bg=roxo,fg=branco,width=25)
                label_derrota.place(x=120,y=180)
                b_recomecar = Button(janela,command=lambda: (iniciar(),b_recomecar.destroy(),label_derrota.destroy()),text='CONTINUAR',bg=branco,fg=cinza,width=10,height=2,font=('ivy 17'),relief=RAISED)
                b_recomecar.place(x=300,y=270)
janela.mainloop()