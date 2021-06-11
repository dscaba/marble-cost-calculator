from tkinter import *

# Menú principal
def calculate():
    global screen2
    screen2 = Toplevel(screen)
    screen2.geometry("500x300")
    screen2.title("Calculadora")

    marble = Label(screen2, text="Seleccione tipo de mármol")
    marble.pack()
    marble_list = ["Negro Brasil", "Calacata", "Carrara" "Portoro"]
    clicked = StringVar()
    clicked.set(marble_list[0])

    drop = OptionMenu(screen2, clicked, *marble_list)
    drop.pack()
    qty = Label(screen2, text="M²")
    qty.pack()
    qty_input = Entry(screen2)
    qty_input.pack()


def admin():
    global screen1
    screen1 = Toplevel(screen)
    screen1.geometry("350x250")
    screen1.title("Panel de Control")


def main_menu():
    global screen
    screen = Tk()
    screen.geometry("300x250")
    screen.title("Calculador de costos")
    Label(text="Bienvendio").pack()
    Label().pack()
    Button(
        text="Calcular",
        height="2",
        width="30",
        bg="lightgreen",
        justify="center",
        command=calculate,
    ).pack()
    Label().pack()

    Button(
        text="Panel de Control", height="2", width="30", bg="lightblue", command=admin
    ).pack()
    screen.mainloop()


main_menu()