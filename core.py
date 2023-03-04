'''
This module contains all the necessary custom built functions required
'''
import File_handle
import pypdfium2 as pdfium
from PIL import Image
import shutil
from tkinter import Tk
from tkinter.filedialog import askopenfilename

pgs = 1

'''
This function extracts all the pages in a given pdf file and stores
them as images in subfolder 'images' in the parent directory
'''
def file_to_img(file_path):
    global pgs

    pdf = pdfium.PdfDocument(file_path)

    pgs = len(pdf)

    for i in range(0, pgs):
        page = pdf.get_page(i)
        page.render_topil().save(str(r"images\page_"+str(i)+".jpg"))

    pdf.close()

'''
This function merges all saved images into a new pdf file
'''
def imgs_to_file(outfile="output.pdf"):
    global pgs

    load = lambda x: Image.open(r"images\page_"+str(x)+".jpg")
    Image.open(r"images\page_0.jpg").save(outfile, save_all=True, append_images=[load(j) for j in range(1, pgs)])

'''
This function is used to clear the folder containing the 
individual image versions of all the pages
'''
def clean():
    shutil.rmtree("images")
    File_handle.create_path("images")

'''
This function makes it easier for the user to choose the
desired file using GUI
'''
def file_pick():
    Tk().withdraw()
    file_dat = askopenfilename()
    return file_dat
    
