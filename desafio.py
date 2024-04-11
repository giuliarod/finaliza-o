# calculo do imc

import tkinter as tk

def imc():
    peso = float(entry1.get())
    altura = float(entry2.get())
    calculo = peso // (altura ** altura)
    label4.config(text = f'Seu IMC é: {calculo}')
    if calculo < 18.5:
        print('Classificação: Baixo peso')
        label5.config(text = 'Classificação: Baixo peso.', fg = '#b8aa14')

    elif calculo > 18.5 and calculo < 24.99:
        print('Classificação: Normal')
        label6.config(text = 'Classificação: Normal.', fg = 'green')

    elif calculo > 25 and calculo < 29.99:
        print('Classificação: Sobrepeso')
        label7.config(text = 'Classificação: Sobrepeso.', fg = 'orange')

    elif calculo > 30:
        print('Classificação: Obesidade')
        label8.config(text = 'Classificação: Obesidade.', fg = 'red')

root = tk.Tk()
root.title('IMC')
root.geometry('300x250')

label1 = tk.Label(root, text = 'Calcule o seu IMC e veja a sua classificação: ', fg = 'green')
label1.pack()
# ---------------------------------------------------------

label2 = tk.Label(root, text = 'Peso (kg): ', fg = 'blue')
label2.pack()

entry1 = tk.Entry(root)
entry1.pack()

# ---------------------------------------------------------

label3 = tk.Label(root, text = 'Altura (m): ', fg = 'blue')
label3.pack()

entry2 = tk.Entry(root)
entry2.pack()

# ----------------------------------------------------------

label4 = tk.Label(root, text = ' ')
label4.pack()

label5 = tk.Label(root, text = ' ')
label5.pack()

label6 = tk.Label(root, text = ' ')
label6.pack()

label7 = tk.Label(root, text = ' ')
label7.pack()

label8 = tk.Label(root, text = ' ')
label8.pack()

btn = tk.Button(root, text = 'Calcular', bg = 'white', command = imc)
btn.pack()

root.mainloop()
