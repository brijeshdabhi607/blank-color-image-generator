from tkinter import *
from tkinter import colorchooser
from PIL import Image
from tkinter import filedialog

root = Tk()
root.title('dabhi brijesh project')
root.iconbitmap("logo.ico")
root.geometry('712x508+300+100')
root.resizable(width=False, height=False)
root.configure(bg='yellow')


def colorpicker():
    color_code = colorchooser.askcolor(title='choose color')
    colorentrybox.delete(0, END)
    colorentrybox.insert(END, "{},{},{}".format(
        color_code[0][0], color_code[0][1], color_code[0][2]))


def createimage():
    color = colorentrybox.get()
    extensions = extensionentrybox.get()
    width = int(widthentrybox.get())
    height = int(heightentrybox.get())
    imagenumber = int(imagenumberentrybox.get())
    name = imagenameentrybox.get()
    url = filedialog.askdirectory()
    convertstatuslabel.config(
        text='{}- images creating=*=*=*=*=*'.format(imagenumber))
    col = color.split(',')
    colorname = []
    try:
        for i in col:
            colorname.append(int(i))
        colorname = tuple(colorname)
    except:
        colorname = col[0]
    for i in range(imagenumber):
        path = url + '/{}{}{}'.format(name, i+1, extensions)
        img = Image.new('RGB', (width, height), color=colorname)
        img.save(path)
    convertstatuslabel.configure(
        text="{} - Images Created Sucessfully ------".format(imagenumber))


########### --------------------Labels--------------------###########
colorlabel = Label(root, text="Color    :", font=(
    "Helvetica", 20, 'bold'), bg='yellow')
colorlabel.place(x=50, y=10)

extensionlabel = Label(root, text='Extension   : ', font=(
    'Helvetica', 20, ' bold'), bg='yellow')
extensionlabel.place(x=50, y=80)

widthlabel = Label(root, text='Width       : ', font=(
    'Helvetica', 20, ' bold'), bg='yellow')
widthlabel.place(x=50, y=150)

heightlabel = Label(root, text='Height       : ', font=(
    'Helvetica', 20, ' bold'), bg='yellow')
heightlabel.place(x=50, y=220)

numberlabel = Label(root, text='Images No: ', font=(
    'Helvetica', 20, ' bold'), bg='yellow')
numberlabel.place(x=50, y=290)

imagenamelabel = Label(root, text='Name        : ', font=(
    'Helvetica', 20, ' bold'), bg='yellow')
imagenamelabel.place(x=50, y=360)

convertstatuslabel = Label(root, text='', font=(
    'Helvetica', 20, ' bold'), bg='yellow', width=40)
convertstatuslabel.place(x=10, y=465)
########### --------------------Entry-box--------------------###########
colorentrybox = Entry(root, font=(
    "white", 20, 'bold'), bg='blue', justify='center', relief=RIDGE, fg='white', selectbackground='white', selectforeground='black', )
colorentrybox.insert(END, '255,0,0')
colorentrybox.place(x=230, y=10, width=350, height=45)

extensionentrybox = Entry(root, font=('arial', 20, 'italic bold'), width=30, bg='blue', relief=RIDGE, bd=5,
                          justify='center', selectbackground='white', selectforeground='black', fg='yellow')
extensionentrybox.insert(END, ".png")
extensionentrybox.place(x=230, y=80)

widthentrybox = Entry(root, font=('arial', 14, 'italic bold'), bg='blue', relief=RIDGE, bd=5,
                      justify='center', selectbackground='white', selectforeground='black', fg='yellow')
widthentrybox.insert(END, "800")
widthentrybox.place(x=230, y=150, height=45, width=460)

heightentrybox = Entry(root, font=('arial', 14, 'italic bold'), bg='blue', relief=RIDGE, bd=5,
                       justify='center', selectbackground='white', selectforeground='black', fg='yellow')
heightentrybox.insert(END, "800")
heightentrybox.place(x=230, y=220, height=45, width=460)

imagenumberentrybox = Entry(root, font=('arial', 14, 'italic bold'), bg='blue', relief=RIDGE, bd=5,
                            justify='center', selectbackground='white', selectforeground='black', fg='yellow')
imagenumberentrybox.insert(END, "5")
imagenumberentrybox.place(x=230, y=290, height=45, width=460)

imagenameentrybox = Entry(root, font=('arial', 14, 'italic bold'), bg='blue', relief=RIDGE, bd=5,
                          justify='center', selectbackground='white', selectforeground='black', fg='yellow')
imagenameentrybox.insert(END, "RedImages")
imagenameentrybox.place(x=230, y=360, height=45, width=460)

########### --------------------Buttons--------------------###########


colorbutton = Button(root, text='select color', command=colorpicker,
                     activebackground='blue', activeforeground='white', background='red', font=("white", 10, 'bold'))
colorbutton.place(x=600, y=10, width=89, height=45)

Convertsinglebtn = Button(root, text='Create Coloured Images', font=('arial', 15, ' bold'), width=52, bd=5,
                          relief=RIDGE, bg='red', activebackground='blue', activeforeground='white',
                          command=createimage)
Convertsinglebtn.place(x=50, y=415, height=45)
root.mainloop()
