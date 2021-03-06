from tkinter import Tk, ttk, scrolledtext, messagebox
from tkinter import *
from rsa.rsa import *


def save_to_file(file, value):
    file = open("../output/" + file, 'w')
    file.write(value)
    file.close()


def bt1_command(p, q, e):
    p = int(p.get())
    q = int(q.get())
    e = int(e.get())

    public, _ = generate_keys(int(p), int(q), int(e))
    save_to_file("chave_publica.txt", "cahves: " + str(public[0]) + " " + str(public[1]))
    messagebox.showinfo("Chave: ", str(public))


def bt2_command(e, n, text):
    e = int(e.get())
    n = int(n.get())

    try:
        message = text.get("1.0", "end-1c")
        message = encrypt(message, (e, n))

        text.delete('1.0', END)
        text.insert(INSERT, message)

        message = text.get("1.0", "end-1c")
        save_to_file("mensagem_criptografada.txt", message)

    except KeyError as e:
        print(e)
        text.delete('1.0', END)
        text.insert(INSERT, "VOCE DIGITOU CARATERES INVALIDOS\nDIGITE LETRAS DE A ATE Z MAIUSCULAS")


def bt3_command(p, q, e, text):
    p = int(p.get())
    q = int(q.get())
    e = int(e.get())

    message = text.get("1.0", "end-1c")

    _, private = generate_keys(int(p), int(q), int(e))

    message = [int(x) for x in message.split()]
    message = decrypt(message, private)
    text.delete('1.0', END)
    text.insert(INSERT, message)


"""
public key = e, n
"""

window = Tk()
window.title("RSA - Criptografia")
window.geometry('650x400')
tab_control = ttk.Notebook(window)

tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)

tab_control.add(tab1, text='Gerar chave')
tab_control.add(tab2, text='Criptografar')
tab_control.add(tab3, text='Descriptografar')

lbl1_0 = Label(tab1, text='', padx=100, pady=50)
lbl1_0.grid(column=0, row=0)

lbl1_1 = Label(tab1, text='P', padx=10, pady=7)
lbl1_1.grid(column=1, row=1)
txt1_1 = Entry(tab1, width=10)
txt1_1.grid(column=1, row=2)

lbl1_2 = Label(tab1, text='Q', padx=10, pady=7)
lbl1_2.grid(column=3, row=1)
txt1_2 = Entry(tab1, width=10)
txt1_2.grid(column=3, row=2)

lbl1_4 = Label(tab1, text='E', padx=10, pady=7)
lbl1_4.grid(column=3, row=3)
txt1_4 = Entry(tab1, width=10)
txt1_4.grid(column=3, row=4)

lbl1_0 = Label(tab1, text='', padx=10, pady=7)
lbl1_0.grid(column=2, row=3)
lbl1_0 = Label(tab1, text='', padx=10, pady=7)
lbl1_0.grid(column=2, row=4)
lbl1_0 = Label(tab1, text='', padx=10, pady=7)
lbl1_0.grid(column=2, row=5)

btn_1 = Button(tab1, text="gerar chaves", command=lambda: bt1_command(txt1_1, txt1_2, txt1_4))
btn_1.grid(column=3, row=6)

lbl2 = Label(tab2, text='Digite a mensagem, \n ou o nome do arquivo:', padx=5, pady=5)
lbl2.grid(column=0, row=1)

txt2_1 = scrolledtext.ScrolledText(tab2, width=40, height=10)
txt2_1.grid(column=1, row=1)

lbl2_2 = Label(tab2, text="E:")
lbl2_2.grid(column=0, row=2)
txt2_2 = Entry(tab2, width=10)
txt2_2.grid(column=0, row=3)

lbl2_3 = Label(tab2, text="N:")
lbl2_3.grid(column=0, row=5)
txt2_3 = Entry(tab2, width=10)
txt2_3.grid(column=0, row=6)

btn_2 = Button(tab2, text="encriptar", command=lambda: bt2_command(txt2_2, txt2_3, txt2_1))
btn_2.grid(column=1, row=2)

rad2_1 = Radiobutton(tab2, text='Arquivo', value=0)
rad2_2 = Radiobutton(tab2, text='Texto', value=1)
rad2_1.grid(column=3, row=2)
rad2_2.grid(column=3, row=3)

lbl3 = Label(tab3, text='Digite a mensagem criptografada,\n ou o nome do arquivo:', padx=5, pady=5)
lbl3.grid(column=0, row=1)

txt3 = scrolledtext.ScrolledText(tab3, width=40, height=10)
txt3.grid(column=1, row=1)

lbl3_1 = Label(tab3, text='P', padx=10, pady=7)
lbl3_1.grid(column=0, row=2)
txt3_1 = Entry(tab3, width=10)
txt3_1.grid(column=0, row=3)

lbl3_2 = Label(tab3, text='Q', padx=10, pady=7)
lbl3_2.grid(column=0, row=4)
txt3_2 = Entry(tab3, width=10)
txt3_2.grid(column=0, row=5)

lbl3_3 = Label(tab3, text='Expoente', padx=10, pady=7)
lbl3_3.grid(column=0, row=6)
txt3_3 = Entry(tab3, width=10)
txt3_3.grid(column=0, row=7)

btn3 = Button(tab3, text="desencriptar", command=lambda: bt3_command(txt3_1, txt3_2, txt3_3, txt3))
btn3.grid(column=1, row=4)

tab_control.pack(expand=1, fill='both')

window.mainloop()
