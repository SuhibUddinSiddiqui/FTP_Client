import tkinter
from tkinter import BOTH, END, LEFT
import ftplib
import Client

get_ip = ''
get_user=''
get_pass=''

get_port=''

ftp = ftplib.FTP()

def connectServer():
    ip = ent_ip.get()
    port = int(ent_port.get())
    get_ip = ip
    get_port = port
    try:
        msg = ftp.connect(ip, port)
        text_servermsg.insert(END, "\n")
        text_servermsg.insert(END, msg)
        lbl_login.place(x=150, y=20)
        ent_login.place(x=150, y=40)
        lbl_pass.place(x=150, y=60)
        ent_pass.place(x=150, y=80)
        btn_login.place(x=182, y=110)
    except:
        text_servermsg.insert(END, "\n")
        text_servermsg.insert(END, "Ohh ! Bhai ip or Port Wrong hai ")


def loginServer():
    user = ent_login.get()
    password = ent_pass.get()
    get_user = user
    get_pass = password

    try:
        msg = ftp.login(user, password)
        text_servermsg.insert(END, "\n")
        text_servermsg.insert(END, msg+" show kaam hogaya")
        displayDir()
        lbl_login.place_forget()
        ent_login.place_forget()
        lbl_pass.place_forget()
        ent_pass.place_forget()
        btn_login.place_forget()
    except:
        text_servermsg.insert(END, "\n")
        text_servermsg.insert(END, "Bhai Id Pass Check Karo")


def displayDir():
    libox_serverdir.insert(0, "--------------------------------------------")
    dirlist = []
    dirlist = ftp.nlst()
    for item in dirlist:
        libox_serverdir.insert(0, item)


# FTP commands
def changeDirectory():
    directory = ent_input.get()
    try:
        msg = ftp.cwd(directory)
        text_servermsg.insert(END, "\n")
        text_servermsg.insert(END, msg + " new dir check kro")
    except:
        text_servermsg.insert(END, "\n")
        text_servermsg.insert(END, "directory Nahe ho sakti :P")
    displayDir()


def createDirectory():
    directory = ent_input.get()
    try:
        msg = ftp.mkd(directory)
        text_servermsg.insert(END, "\n")
        text_servermsg.insert(END, msg)
    except:
        text_servermsg.insert(END, "\n")
        text_servermsg.insert(END, "directory Nahe ban Sakti bhago yaha syy")
    displayDir()


def deleteDirectory():
    directory = ent_input.get()
    try:
        msg = ftp.rmd(directory)
        text_servermsg.insert(END, "\n")
        text_servermsg.insert(END, msg+" krdi delete")
    except:
        text_servermsg.insert(END, "\n")
        text_servermsg.insert(END, "Nahe kr raha Delete !  directory Delete kr k Dekhao :P ")
    displayDir()


def deleteFile():
    file = ent_input.get()
    try:
        msg = ftp.delete(file)
        text_servermsg.insert(END, "\n")
        text_servermsg.insert(END, msg)
    except:
        text_servermsg.insert(END, "\n")
        text_servermsg.insert(END, "Nahe ho rahe delete file")
    displayDir()


def downloadFile():
    file = ent_input.get()
    #down = open(file, "wb")
    try:
        Client.Download_files(file,ftp)

        text_servermsg.insert(END, "\n")
        text_servermsg.insert(END)
    except:
        text_servermsg.insert(END, "\n")
        text_servermsg.insert(END)
    displayDir()


def uploadFile():
    file = ent_input.get()
    try:

        Client.Upload_File(ftp)
    except:
         text_servermsg.insert(END, "Bhai upload Nahe kr sakta ! please Tang nahe Karo")
    displayDir()


def closeConnection():
    try:
        text_servermsg.insert(END, "\n")
        text_servermsg.insert(END, "Closing connection... Shukkar jan shurdi tum ny")
        text_servermsg.insert(END, "\n")
        text_servermsg.insert(END, ftp.quit())
    except:
        text_servermsg.insert(END, "\n")
        text_servermsg.insert(END, "nahe kr raha disconnect 8-)")


window = tkinter.Tk()
window.title("FTP Client")
#window.wm_iconbitmap("favicon.ico")
window.geometry("1000x600")

# Connect
lbl_ip = tkinter.Label(window, text="IP Address")
ent_ip = tkinter.Entry(window)
lbl_port = tkinter.Label(window, text="Port")
ent_port = tkinter.Entry(window)
btn_connect = tkinter.Button(window, text="Connect", command=connectServer)

# Server response text box
text_servermsg = tkinter.Text(window)

# Login
lbl_login = tkinter.Label(window, text="Username")
ent_login = tkinter.Entry(window)
lbl_pass = tkinter.Label(window, text="Password")
ent_pass = tkinter.Entry(window)
btn_login = tkinter.Button(window, text="Login", command=loginServer)

# Directory listing
lbl_dir = tkinter.Label(window, text="Directory listing:")
libox_serverdir = tkinter.Listbox(window, width=40, height=14)

# Options
lbl_input = tkinter.Label(window, text="Input")
ent_input = tkinter.Entry(window)
btn_chdir = tkinter.Button(window, text="Change Directory", command=changeDirectory, width=15)
btn_crdir = tkinter.Button(window, text="Create Directory", command=createDirectory, width=15)
btn_deldir = tkinter.Button(window, text="Delete Directory", command=deleteDirectory, width=15)
btn_delfile = tkinter.Button(window, text="Delete File", command=deleteFile, width=15)
btn_downfile = tkinter.Button(window, text="Download File", command=downloadFile, width=15)
btn_upfile = tkinter.Button(window, text="Upload File", command=uploadFile, width=15)
btn_quit = tkinter.Button(window, text="Disconnect", command=closeConnection, width=15)

# Place widgits
lbl_ip.place(x=20, y=20)
ent_ip.place(x=20, y=40)
lbl_port.place(x=20, y=60)
ent_port.place(x=20, y=80)
btn_connect.place(x=52, y=110)
text_servermsg.place(x=20, y=150)

lbl_dir.place(x=700, y=143)
libox_serverdir.place(x=700, y=165)

lbl_input.place(x=700, y=400)
ent_input.place(x=700, y=420)
btn_chdir.place(x=700, y=450)
btn_crdir.place(x=700, y=480)
btn_deldir.place(x=700, y=510)
btn_delfile.place(x=700, y=540)

btn_downfile.place(x=850, y=450)
btn_upfile.place(x=850, y=480)
btn_quit.place(x=850, y=510)

# Create
window.mainloop()