import sys
import ftplib
import os
import get
from tkinter import filedialog
import time
my_ip = get.get_ip.get_current_ip('')
print(my_ip)

def get_DIR():
    try:
        q = ftplib.FTP()
        q.connect(my_ip,2121)
        q.login('user','12345')
        data = []
        q.dir(data.append)
        q.quit()

        for line in data:
            print("-", line)
    except:
        print("login Fail")
        print("Check FTP connection OR Server")

    print("\n")
    print("\n")
    print("\n")



def Upload_File(ftp):

    #print("* * * * Select File You Wish To Upload * * * *")
    #time.sleep(2)
    source = filedialog.askopenfilename()
    e = os.path.normpath(source)
    temp = ''
    #print(source)

    for x in range(len(source)):
        if source[-x] == '/':
            #print("got it")
            r = x - 1
            temp = source[-r:]
            #print(temp)
            break

    #print(temp)
    filename = temp
    #try:
        #ftp = ftplib.FTP()
        #ftp.connect(get_ip, int(get_port))
        #ftp.login(get_user, get_pass)
    #except:
        #print("login Fail")
        #print("Check FTP connection OR Server")

    try:
        # ftp.cwd(Self)
        my_file = open(e, 'rb')
        h = mode = open(e, mode='rb')
        if filename in (".txt", ".htm", ".html"):
           ftp.storlines('STOR ' + filename, h)
        else:
            ftp.storbinary('STOR ' + filename, h)
        #ftp.quit()
        print("done")
    except:
        print('! ! ! ! ! !     W A R N I N G  ! ! ! ! ! ! ')
        print("Find The Error")
    print("\n")
    print("\n")
    print("\n")

def Download_files(filename,ftp):
    #my_ip = get.get_ip.get_current_ip('')

    #get_File_name = input("Enter File Name With Extension: ")

    #try:
     #   filename = get_File_name
      #  ftp = ftplib.FTP()
       # ftp.connect(my_ip,2121)
        #ftp.login('user','12345')
    #except:
     #   print("login Fail")
      #  print("Check FTP connection OR Server")


    #print("You Can Select the folder Where You Wish to Download the item Otherwise default path would be F:/")
    #print("Do You Wish To Select Folder")
    #path_input = input("Enter Y / N: ")

    #if path_input == 'Y' or path_input == 'y':
     #   source = filedialog.askdirectory()
      #  e = os.path.normpath(source)
       # os.chdir(e)
    #else:
     #   n = os.path.normpath('F:/tem')
        #print(n)
      #  os.chdir(n)


    #print(os.getcwd())
    try:
        n = os.path.normpath('F:/Download')
        os.chdir(n)
        ftp.retrbinary("RETR %s" %filename ,open(filename,'wb').write)
        #ftp.quit()
        print("done")
    except:
        print('! ! ! ! ! !     W A R N I N G  ! ! ! ! ! ! ')
        print("Check The File Name OR May be File Does Not Exist")

    #print("\n")
    #print("\n")
    #print("\n")