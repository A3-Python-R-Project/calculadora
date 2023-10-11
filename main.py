from tkinter import *
from tkinter import ttk

#Cores
brown = "#964b00"
bege = "#f5f5dc"
blue = "#0000FF"
green = "#008000"
loyalBlue = "#4169e1"
white = "#FFFFFF"
black = "#0F0F0F"
orange = "#FFA500"
yellow = "#FFFF00"

#Janela
janela = Tk()
janela.title("Calculadora")
janela.geometry("235x310")
janela.config(bg=blue)

frame_tela = Frame(janela, width=235, height=50, bg=black)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=235, height=268)
frame_corpo.grid(row=1, column=0)

#Label
app_label = Label(frame_tela, text='123456789', width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=('Ivy 18'), bg=black, fg=white)
app_label.place(x=0, y=0)

#Botões
#Primeira coluna
clean = Button(frame_corpo, text="C", width=11, height=2, font=('Ivy 13 bold'), fg=yellow, relief=RAISED, overrelief=RIDGE, bg=loyalBlue)
clean.place(x=0, y=0)

percentage = Button(frame_corpo, text="%", width=5, height=2, font=('Ivy 13 bold'), fg=yellow, relief=RAISED, overrelief=RIDGE, bg=loyalBlue)
percentage.place(x=118, y=0)

division = Button(frame_corpo, text="/", width=5, height=2, font=('Ivy 13 bold'), fg=loyalBlue, relief=RAISED, overrelief=RIDGE, bg=yellow)
division.place(x=177, y=0)

#Segunda coluna
seven = Button(frame_corpo, text="7", width=5, height=2, font=('Ivy 13 bold'), fg=yellow, relief=RAISED, overrelief=RIDGE, bg=loyalBlue)
seven.place(x=0, y=52)

eight = Button(frame_corpo, text="8", width=5, height=2, font=('Ivy 13 bold'), fg=yellow, relief=RAISED, overrelief=RIDGE, bg=loyalBlue)
eight.place(x=59, y=52)

nine = Button(frame_corpo, text="9", width=5, height=2, font=('Ivy 13 bold'), fg=yellow, relief=RAISED, overrelief=RIDGE, bg=loyalBlue)
nine.place(x=118, y=52)

multiplication = Button(frame_corpo, text="X", width=5, font=('Ivy 13 bold'), height=2, fg=loyalBlue, relief=RAISED, overrelief=RIDGE, bg=yellow)
multiplication.place(x=177, y=52)

#Terceira coluna
four = Button(frame_corpo, text="4", width=5, height=2, font=('Ivy 13 bold'), fg=yellow, relief=RAISED, overrelief=RIDGE, bg=loyalBlue)
four.place(x=0, y=104)

five = Button(frame_corpo, text="5", width=5, height=2, font=('Ivy 13 bold'), fg=yellow, relief=RAISED, overrelief=RIDGE, bg=loyalBlue)
five.place(x=59, y=104)

six = Button(frame_corpo, text="6", width=5, height=2, font=('Ivy 13 bold'), fg=yellow, relief=RAISED, overrelief=RIDGE, bg=loyalBlue)
six.place(x=118, y=104)

subtraction = Button(frame_corpo, text="-", width=5, font=('Ivy 13 bold'), height=2, fg=loyalBlue, relief=RAISED, overrelief=RIDGE, bg=yellow)
subtraction.place(x=177, y=104)

#Quarta coluna
one = Button(frame_corpo, text="1", width=5, height=2, font=('Ivy 13 bold'), fg=yellow, relief=RAISED, overrelief=RIDGE, bg=loyalBlue)
one.place(x=0, y=156)

two = Button(frame_corpo, text="2", width=5, height=2, font=('Ivy 13 bold'), fg=yellow, relief=RAISED, overrelief=RIDGE, bg=loyalBlue)
two.place(x=59, y=156)

three = Button(frame_corpo, text="3", width=5, height=2, font=('Ivy 13 bold'), fg=yellow, relief=RAISED, overrelief=RIDGE, bg=loyalBlue)
three.place(x=118, y=156)

addition = Button(frame_corpo, text="+", width=5, font=('Ivy 13 bold'), height=2, fg=loyalBlue, relief=RAISED, overrelief=RIDGE, bg=yellow)
addition.place(x=177, y=156)

#Última coluna
zero = Button(frame_corpo, text="0", width=11, height=2, font=('Ivy 13 bold'), fg=yellow, relief=RAISED, overrelief=RIDGE, bg=loyalBlue)
zero.place(x=0, y=208)

point = Button(frame_corpo, text=".", width=5, height=2, font=('Ivy 13 bold'), fg=yellow, relief=RAISED, overrelief=RIDGE, bg=loyalBlue)
point.place(x=118, y=208)

equal = Button(frame_corpo, text="=", width=5, height=2, font=('Ivy 13 bold'), fg=loyalBlue, relief=RAISED, overrelief=RIDGE, bg=yellow)
equal.place(x=177, y=208)

janela.mainloop()
