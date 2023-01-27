from PyPDF2 import PdfReader, PdfWriter
from os import path
class PDF:

    def __init__():
        pass

    def splitePDF(_path=None):
        #fname = path.splitext(_path)[0]
        fname = _path
        pdf = PdfReader(fname)
        paginas = len(pdf.pages)
        for page in range(paginas):
            pdf_writer = PdfWriter()
            pdf_writer.add_page(pdf.pages[page])
    
            output_filename = '{}_page_{}.pdf'.format(
                fname, page+1)
    
            with open(output_filename, 'wb') as out:
                pdf_writer.write(out)
    
            print('Created: {}'.format(output_filename))