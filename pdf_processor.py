from PyQt5 import QtWidgets, uic , QtGui
import sys
from PyPDF2 import PdfFileWriter, PdfFileReader, PdfMerger
import os 

class Ui(QtWidgets.QMainWindow):


    def resource_path(self,relative_path):
        base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(base_path, relative_path)

    def __init__(self):
        super(Ui, self).__init__()
        
        ui_file_path = self.resource_path('pdf_tool.ui')
        icon_file_path = self.resource_path('gui_icon.png')

        uic.loadUi(ui_file_path, self)
        self.setFixedSize(686,440)
        
        self.setWindowTitle("PDF PROCESSING TOOL")
        self.setWindowIcon(QtGui.QIcon(icon_file_path))

        self.label_14.setText("Idle Mode.")

        for lab in [self.label_2,self.label_5,self.label_8,self.label_9,self.label]:
            lab.setStyleSheet("color:blue;")

        self.label.setStyleSheet("color:brown;")

        #self.all_labels = [self.label,self.label_2,self.label_3,self.label_4,self.label_5,self.label_6,self.label_7,self.label_8]
        #self.all_labels = self.all_labels + [self.label_9,self.label_10,self.label_11,self.label_12,self.label_13]

        #for lab in self.all_labels:
            #lab.setStyleSheet("color:green;")

        self.label_14.setStyleSheet("color:red;border:2px solid;")

        #self.lineEdit.setStyleSheet("color:white")
        #self.lineEdit_3.setStyleSheet("color:white")
        #self.lineEdit_2.setStyleSheet("color:white")

        #self.all_buttons = [self.pushButton,self.pushButton_2,self.pushButton_3,self.pushButton_4,self.pushButton_5]
        #self.all_buttons = self.all_buttons + [self.pushButton_6,self.pushButton_7,self.pushButton_8,self.pushButton_9]

        #for button in self.all_buttons:
            #button.setStyleSheet("color:green;border:5px solid white;")

        self.pushButton.clicked.connect(self.browse_merge_file1)
        self.pushButton_2.clicked.connect(self.browse_merge_file2)
        self.pushButton_4.clicked.connect(self.browse_split_file)
        self.pushButton_6.clicked.connect(self.browse_encrypt_file)
        self.pushButton_8.clicked.connect(self.browse_decrypt_file)
        self.pushButton_7.clicked.connect(self.pdf_encrypt)
        self.pushButton_9.clicked.connect(self.pdf_decrypt)
        self.pushButton_3.clicked.connect(self.pdf_merge)
        self.pushButton_5.clicked.connect(self.pdf_split)

        self.merge_file1 = ""
        self.merge_file2 = ""
        self.split_file = ""
        self.encrypt_file = ""
        self.decrypt_file = ""

        self.line.setVisible(False)
        self.line_2.setVisible(False)

    def browse_merge_file1(self):
        filename = QtWidgets.QFileDialog.getOpenFileName(self,'Choose File','/')
        file_node = filename[0].split('/')[-1]
        file_path = filename[0]
        self.label_3.setText(file_node)
        self.label_14.setText("File selected for merge : "+file_path)
        self.merge_file1 = file_path

    def browse_merge_file2(self):
        filename = QtWidgets.QFileDialog.getOpenFileName(self,'Choose File','/')
        file_node = filename[0].split('/')[-1]
        file_path = filename[0]
        self.label_4.setText(file_node)
        self.label_14.setText("File selected for merge : "+file_path)
        self.merge_file2 = file_path

    def browse_split_file(self):
        filename = QtWidgets.QFileDialog.getOpenFileName(self,'Choose File','/')
        file_node = filename[0].split('/')[-1]
        file_path = filename[0]
        self.label_6.setText(file_node)
        self.label_14.setText("File selected for split : "+file_path)
        self.split_file = file_path

    def browse_encrypt_file(self):
        filename = QtWidgets.QFileDialog.getOpenFileName(self,'Choose File','/')
        file_node = filename[0].split('/')[-1]
        file_path = filename[0]
        self.label_10.setText(file_node)
        self.label_14.setText("File selected for encryption : "+file_path)
        self.encrypt_file = file_path

    def browse_decrypt_file(self):
        filename = QtWidgets.QFileDialog.getOpenFileName(self,'Choose File','/')
        file_node = filename[0].split('/')[-1]
        file_path = filename[0]
        self.label_12.setText(file_node)
        self.label_14.setText("File selected for decryption : "+file_path)
        self.decrypt_file = file_path

    def pdf_encrypt(self):
        input_file = self.encrypt_file
        if not os.path.exists(input_file):
            self.label_14.setText("Incorrect File loaded. File does not exists.")
            self.lineEdit_2.clear()
            return
        try:
            input_pdf_file = PdfFileReader(input_file)
        except:
            self.label_14.setText("Incorrect PDF File loaded.")
            return

        input_password = self.lineEdit_2.text()

        if input_password == "":
            self.label_14.setText("Password field empty. Enter valid password.")
            return

        try:

            out = PdfFileWriter()
            num = input_pdf_file.numPages

            for idx in range(num):
                page = input_pdf_file.getPage(idx)
                out.addPage(page)

            out.encrypt(input_password)

            out_pdf_file_node = input_file.split('/')[-1].split('.')[0]+"_encrypted.pdf"
            out_pdf_file_path = "/".join(input_file.split('/')[0:-1])+"/"+out_pdf_file_node

            with open(out_pdf_file_path, "wb") as f:
                out.write(f)

            self.label_14.setText("File encrypted successfully : "+out_pdf_file_path)
            self.lineEdit_2.clear()
            self.label_10.setText("No file loaded.")
            self.encrypt_file = ""

        except:
            self.label_14.setText("Unexpected error occured. Make sure no under process file is opened. Try Again !")

    def pdf_decrypt(self):
        input_file = self.decrypt_file
        if not os.path.exists(input_file):
            self.label_14.setText("Incorrect File loaded. File does not exists.")
            self.lineEdit_3.clear()
            return
        try:
            input_pdf_file = PdfFileReader(input_file)
        except:
            self.label_14.setText("Incorrect PDF File loaded.")
            return

        input_password = self.lineEdit_3.text()

        if input_password == "":
            self.label_14.setText("Password field empty. Enter valid password.")
            return

        if input_pdf_file.isEncrypted:
            
            try:
                input_pdf_file.decrypt(input_password)
            except:
                self.label_14.setText("Password is incorrect. Cannot decrypt file.")
                self.lineEdit_3.clear()
                return

            try:
                out = PdfFileWriter()
                num = input_pdf_file.numPages

                for idx in range(num):
                    page = input_pdf_file.getPage(idx)
                    out.addPage(page)

                out_pdf_file_node = input_file.split('/')[-1].split('.')[0]+"_decrypted.pdf"
                out_pdf_file_path = "/".join(input_file.split('/')[0:-1])+"/"+out_pdf_file_node

                with open(out_pdf_file_path, "wb") as f:
                    out.write(f)

                self.label_14.setText("File decrypted successfully : "+out_pdf_file_path)
                self.lineEdit_3.clear()
                self.decrypt_file = ""
                self.label_12.setText("No file loaded.")
            
            except:
                self.label_14.setText("Unexpected error occured. Make sure no under process file is opened or incorrect password. Try Again !")

        else:
            self.label_14.setText("File is not encrypted. Can't decrypt un-encrypted files. Unloading file.")
            self.label12.setText("No file loaded.")
            self.decrypt_file = ""
            self.lineEdit_3.clear()

    def pdf_merge(self):
        pdf_file_1 = self.merge_file1
        pdf_file_2 = self.merge_file2

        if not os.path.exists(pdf_file_1) or not os.path.exists(pdf_file_2):
            self.label_14.setText("Either of input file does not exists.")
            self.label_3.setText("No file loaded.")
            self.label_4.setText("No file loaded.")
            self.merge_file1 = ""
            self.merge_file2 = ""
            return

        try:

            merger = PdfMerger()
            merger.append(pdf_file_1)
            merger.append(pdf_file_2)

            output_file_path = '/'.join(pdf_file_2.split('/')[0:-1])+'/final_merged_file.pdf'

            merger.write(output_file_path)
            merger.close()

            self.label_14.setText("Files merged successfully. Merged file : "+output_file_path)
            self.label_3.setText("No file loaded.")
            self.label_4.setText("No file loaded.")
            self.merge_file1 = ""
            self.merge_file2 = ""

        except:
            self.label_14.setText("Files merging failed. Correct Inputs and try again.")

    def pdf_split(self):
        filename = self.split_file
        
        if not os.path.exists(filename):
            self.label_14.setText("Input file does not exists.")
            self.label_6.setText("No file loaded.")
            self.split_file = ""
            return

        indexes_to_grep = []
        page_range = self.lineEdit.text()
        pages = page_range.split(',')
        for page in pages:
            if "-" not in page and page.isdigit():
                indexes_to_grep.append(int(page)-1)
            if "-" in page:
                if len(page.split('-')) != 2:
                    self.label_14.setText("Invalid page range mentioned. Split will happen only on valid pages.")
                    break
                page_start = page.split('-')[0]
                page_end = page.split('-')[1]
                if page_start.isdigit() and page_end.isdigit():
                    for p in range(int(page_start)-1,int(page_end),1):
                        indexes_to_grep.append(p)
                else:
                    self.label_14.setText("Invalid page range mentioned. Split will happen only on valid pages.")

        number_of_pages_to_grep = len(indexes_to_grep)
        if number_of_pages_to_grep == 0:
            self.label_14.setText("No valid page range mentioned.")

        try:
            input_pdf_file = PdfFileReader(filename)
        except:
            self.label_14.setText("Incorrect PDF File loaded.")
            self.label_6.setText("No file loaded.")
            self.split_file = ""
            return

        try:

            out = PdfFileWriter()
            num = input_pdf_file.numPages

            for idx in range(num):
                if idx in indexes_to_grep:
                    page = input_pdf_file.getPage(idx)
                    out.addPage(page)

            out_pdf_file_node = filename.split('/')[-1].split('.')[0]+"_split.pdf"
            out_pdf_file_path = "/".join(filename.split('/')[0:-1])+"/"+out_pdf_file_node

            with open(out_pdf_file_path, "wb") as f:
                out.write(f)


            self.label_14.setText("File splited successfully : "+out_pdf_file_path)
            self.lineEdit.clear()
            self.split_file = ""
            self.label_6.setText("No file loaded.")

        except:
            self.label_14.setText("Unexpected error occured. Make sure no under process file is opened. Try Again !")





app = QtWidgets.QApplication(sys.argv)
window = Ui()
window.show()
app.exec_()