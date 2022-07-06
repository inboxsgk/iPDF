import File_handle
import pypdfium2 as pdfium
from PIL import Image
import shutil

pgs = 1


def file_to_img(file_path):
    global pgs

    pdf = pdfium.PdfDocument(file_path)

    pgs = len(pdf)

    for i in range(0, pgs):
        page = pdf.get_page(i)
        page.render_topil().save(str(r"images\page_"+str(i)+".jpg"))

    pdf.close()


def imgs_to_file():
    global pgs

    load = lambda x: Image.open(r"images\page_"+str(x)+".jpg")
    Image.open(r"images\page_0.jpg").save("output.pdf", save_all=True, append_images=[load(j) for j in range(1, pgs)])


def clean():
    shutil.rmtree("images")
    File_handle.create_path("images")
