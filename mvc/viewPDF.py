from sys import exit,argv
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QFileDialog
from PyQt5.QtCore import pyqtSlot
from servicePDF import PDF


class View(QWidget):
    
    def __init__(self):
        super().__init__()
        self.title = 'Dividir PDF'
        self.left = 100
        self.top = 100
        self.width = 300
        self.height = 60
        self.initUI()
        self._fileName=""

    def initUI(self):               
        
        
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        button = QPushButton('Buscar PDF', self)
        button.setToolTip('Aqui você vai buscar o pdf que será dividido')
        button.move(110,10)
        button.clicked.connect(self.openFileNameDialog)

        buttonSplit = QPushButton('Dividir', self)
        buttonSplit.setToolTip('Click aqui para dividir pdf')
        buttonSplit.move(110,30)
        buttonSplit.clicked.connect(self.pdf_splitter)
        
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
        PDF.splitePDF(self._fileName)
        # fname = path.splitext(path.basename(self._fileName))[0]
 
        # pdf = PdfFileReader(self._fileName)
        # for page in range(pdf.getNumPages()):
        #     pdf_writer = PdfFileWriter()
        #     pdf_writer.addPage(pdf.getPage(page))
    
        #     output_filename = '{}_page_{}.pdf'.format(
        #         fname, page+1)
    
        #     with open(output_filename, 'wb') as out:
        #         pdf_writer.write(out)
    
        #     print('Created: {}'.format(output_filename))