
from tkinter import *
  
# import filedialog module
from tkinter import filedialog
from PyPDF2 import PdfFileWriter, PdfFileReader
import os


def browseFiles():
    filename = filedialog.askopenfilename(initialdir = "/",title = "Select a File",filetypes = (("PDF files","*.pdf*"),("all files","*.*")))
    # Change label contents
    label_file_explorer.configure(text="File Opened: "+filename)
    

def encryptFiles():
  password = password_entry.get()
  filename = label_file_explorer.cget("text").split(':')[-1]
  print("Filename - "+filename)
  print("Password - "+password)
  password_entry.delete(0,END)
  if not os.path.exists(filename) or ".pdf" not in filename:
    label_file_explorer.configure(text = "Error : Incorrect File choosen. Choose correct file.")
    return

  outfilename = str(filename).replace('.pdf','')
  outfilename = outfilename+"_encrypted.pdf"

  out = PdfFileWriter()
  file = PdfFileReader(filename)

  num = file.numPages

  for idx in range(num):
    page = file.getPage(idx)
    out.addPage(page)

  out.encrypt(password)

  with open(outfilename, "wb") as f:  
    out.write(f)

  label_file_explorer.configure(text="File Excrypted and saved at : "+outfilename)
  print("Encrypted Filename - "+outfilename)
                                                                                     
# Create the root window
window = Tk()
# Set window title
window.title('PDF Encryption Tool')
# Set window size
window.geometry("800x400")
window.resizable(0,0)

#Set window background color
window.config(background = "#998CEB")
# Create a File Explorer label
label_file_explorer = Label(window,text = "Choose File to be encrypted",width = 90,height = 3,fg = "blue",font=('Arial 10'))
label1 = Label(window,text = "Enter Password",height = 2,width = 50,bg='#998CEB')
password_entry = Entry(window, text="Enter Password", bd=2, width = 28,font=('Arial 16'))
password_to_be_used = password_entry.get()
file_to_be_encrypted = label_file_explorer.cget("text").split(':')[-1]
button_explore = Button(window,text = "Browse Files",width = 100 ,command = browseFiles,bg='#BAE8AC')
button_encrypt = Button(window,text = "Encrypt", width = 100 , command = encryptFiles,bg='#BAE8AC')
  
# Grid method is chosen for placing
# the widgets at respective positions
# in a table like structure by
# specifying rows and columns

label_file_explorer.place(x=50,y=100)
#label_file_explorer.grid(column = 1, row = 1)
button_explore.place(x=50,y=200)
#button_explore.grid(column = 1, row = 2)
label1.place(x=50,y=250)
password_entry.place(x=405,y=250)
#label1.grid(column = 1,row = 3)
#password_entry.grid(column=2,row=3)
button_encrypt.place(x=50,y=300)
#button_encrypt.grid(column = 1,row = 4)
  
# Let the window wait for any events
window.mainloop()