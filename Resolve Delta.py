from tkinter import *


class Main:

    def resultado(self):

        dtb = int(self.B.get())
        dta = int(self.A.get())
        dtc = int(self.C.get())

        #CONTA





        p = dtb * dtb
        v = (4 * dta * dtc)
        
        if dtc < 0:

            v = (4 * dta * (-dtc))

        elif dta < 0:
            v = (4 * (-dta) * dtc)

        elif dta and dtc < 0:

            v = (4 * (-dta) * (-dtc))
            v = (4 * dta * dtc)


        resultado = int((p - v))



        self.result['text'] = int(resultado)







    def __init__(self):
        self.janela = Tk()
        self.janela.title('Resolve Delta')
        self.janela.geometry('210x300')

        Label(self.janela, text='RESOLVA SEU DELTA', bg='#31D976', fg='black', width=30, height=2).grid(row=0, column=0, columnspan=2,pady=5, )
        Label(self.janela, text='DIGITE O VALOR DE B', bg='black', fg='white', width=30).grid(row=1, column=0)

        self.B = Entry(self.janela, bg='#31D976', fg='black', width=20)
        self.B.grid(row=2, column=0, pady=5)

        Label(self.janela, text='DIGITE O VALOR DE A', bg='black', fg='white', width=30).grid(row=3, column=0)

        self.A = Entry(self.janela, bg='#31D976', fg='black', width=20)
        self.A.grid(row=4, column=0, pady=5)

        Label(self.janela, text='DIGITE O VALOR DE C', bg='black', fg='white', width=30).grid(row=5, column=0)

        self.C = Entry(self.janela, bg='#31D976', fg='black', width=20)
        self.C.grid(row=6, column=0, pady=5)

        Label(self.janela, text='RESULTADO', bg='#1CB9D2', fg='Black', width=30).grid(row=7, column=0)
        self.result = Label(self.janela, text='1', width=30)
        self.result.grid(row=8, column=0)

        self.Calcular = Button(self.janela, text='CALCULAR', bg='#E39018', command=self.resultado).grid(row=9, column=0, pady=10)








        self.janela.mainloop()






Main()
