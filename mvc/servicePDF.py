from PyPDF2 import PdfFileReader, PdfFileWriter
from os import path
class PDF:

    def __init__():
        pass

    def splitePDF(_path=None):
        fname = path.splitext(path.basename(self._fileName))[0]
    
        pdf = PdfFileReader(_path)
        for page in range(pdf.getNumPages()):
            pdf_writer = PdfFileWriter()
            pdf_writer.addPage(pdf.getPage(page))
    
            output_filename = '{}_page_{}.pdf'.format(
                fname, page+1)
    
            with open(output_filename, 'wb') as out:
                pdf_writer.write(out)
    
            print('Created: {}'.format(output_filename))