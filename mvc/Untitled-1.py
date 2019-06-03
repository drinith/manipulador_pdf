from os import path
from sys import exit,argv
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QFileDialog
from PyQt5.QtCore import pyqtSlot
from PyPDF2 import PdfFileReader, PdfFileWriter
class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        self.title = 'Dividir PDF'
        self.left = 100
        self.top = 100
        self.width = 300
        self.height = 80
        self.initUI()
        self._fileName=""

    def initUI(self):               
        
        
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        button = QPushButton('Buscar PDF', self)
        button.setToolTip('Aqui você vai buscar o pdf que será dividido')
        button.move(110,10)
        button.clicked.connect(self.openFileNamesDialog)

        buttonSplit = QPushButton('Dividir', self)
        buttonSplit.setToolTip('Click aqui para dividir pdf')
        buttonSplit.move(110,30)
        buttonSplit.clicked.connect(self.pdf_splitter)

        buttonMerger = QPushButton('Juntar', self)
        buttonMerger.setToolTip('Click aqui para juntar pdf')
        buttonMerger.move(110,50)
        buttonMerger.clicked.connect(self.pdf_merger)
        
        self.show()

    @pyqtSlot()
    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"Buscar", "","All Files (*);;PDFs (*.pdf)", options=options)
        if fileName:
            self._fileName=fileName
            print(fileName)
    @pyqtSlot()
    def openFileNamesDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        files, _ = QFileDialog.getOpenFileNames(self,"Buscar", "","All Files (*);;PDFs (*.pdf", options=options)
        if files:
            self._fileName=files
            print(files)
    @pyqtSlot()
    def pdf_splitter(self):
        fname = path.splitext(path.basename(self._fileName[0]))[0]
 
        pdf = PdfFileReader(self._fileName[0])
        for page in range(pdf.getNumPages()):
            pdf_writer = PdfFileWriter()
            pdf_writer.addPage(pdf.getPage(page))
    
            output_filename = '{}_page_{}.pdf'.format(
                fname, page+1)
    
            with open(output_filename, 'wb') as out:
                pdf_writer.write(out)
    
            print('Created: {}'.format(output_filename))

    @pyqtSlot()
    def pdf_merger(self,saida="merger.pdf"):
        input_streams = []
        writer = PdfFileWriter()
        # First open all the files, then produce the output file, and
        # finally close the input files. This is necessary because
        # the data isn't read from the input files until the write
        # operation. Thanks to
        # https://stackoverflow.com/questions/6773631/problem-with-closing-python-pypdf-writing-getting-a-valueerror-i-o-operation/6773733#6773733
        for input_file in self._fileName:
            
            print ("pdf carregado " +input_file)
                
            
            print("fname "+input_file)
            pdf =  PdfFileReader(input_file)
            for n in range(pdf.getNumPages()):
                writer.addPage(pdf.getPage(n))
        
        with open(saida, 'wb') as out:
            writer.write(out)
    
        for f in input_streams:
            f.close()    
        
if __name__ == '__main__':
    
    app = QApplication(argv)
    ex = Example()
    exit(app.exec_())