from tkinter import*

janela = Tk()
janela.geometry('400x400+200+200')
  #Função para calcular o troco
def calculaTroco():
    troco = float(ent2.get()) - float(ent1.get())
    troco = troco*100
    moeda100 = int(troco / 100)
    troco = troco % 100
    moeda50= int(troco / 50)
    troco = troco % 50
    moeda25 = int(troco /25)
    troco = troco % 25
    moeda10 = int(troco /10)
    troco = troco % 10
    moeda5 = int(troco /5)
    troco = troco % 5
    moeda1 = int(troco)
    lb3['text'] = '%d moedas de 1 real' %moeda100
    lb4['text'] = '%d moedas de 0,50 centavos' %moeda50
    lb5['text'] = '%d moedas de 0,25 centavos' %moeda25
    lb6['text'] = '%d moedas de 0,10 centavos' %moeda10
    lb7['text'] = '%d moedas de 0,05 centavos' %moeda5
    lb8['text'] = '%d moedas de 0.01 centavos' %moeda1
   # Entrada de dados 1
lb1 = Label(janela, text='Entre com o valor do produto:')
lb1.place(x=110, y=10)
ent1 = Entry(janela)
ent1.place(x=110, y=30)
   # Entrada de dados 2
lb2= Label(janela, text='Entre com o valor pago:')
lb2.place(x=110, y=60)
ent2 = Entry(janela)
ent2.place(x=110, y=80)
   # Botão
bt1 = Button(janela, width=20, text='Calular', command=calculaTroco)
bt1.place(x=110, y=110)
  # Resultado
lb3 = Label(janela, text='Troco a ser dado.')
lb3.place(x=110, y=160)
lb4 = Label(janela, text='')
lb4.place(x=110, y=180)
lb5 = Label(janela, text='')
lb5.place(x=110, y=200)
lb6 = Label(janela, text='')
lb6.place(x=110, y=220)
lb7 = Label(janela, text='')
lb7.place(x=110, y=240)
lb8 = Label(janela, text='')
lb8.place(x=110, y=260)

janela.mainloop()


