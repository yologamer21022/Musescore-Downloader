from PIL import Image
import os
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF
from PyPDF2 import PdfFileMerger

list = []
images_RGB = []
images_RGB2 = []
count = 0
pdfs = []

#Cache Clearing
def clearCache():
    for f in os.listdir("./conversion"):
        os.remove(os.path.join("./conversion", f))

#Converting The Transparent Background to White Color
def PngFix(content):
    global list
    img = Image.open(content)
    img = img.convert("RGBA")

    datas = img.getdata()

    newData = []

    for item in datas:
        if item[3] == 0:
            newData.append((255, 255, 255, 255))
        elif item[0] == 255 and item[1] == 0 and item[2] == 0:
            newData.append((0, 0, 0, 255))
        else:
            newData.append(item)

    img.putdata(newData)
    img.save(content, "PNG")

    list.append(content)

#PNG to PDF
def PngToPdf():
    global list
    for i in list:
        global images_RGB
        image = Image.open(i)
        images_RGB.append(image.convert("RGB"))


    images_RGB[0].save("./output/Music Sheet.pdf", "PDF", save_all = True, append_images = images_RGB[1:])

    clearCache()
    print("DONE")

#SVG to PDF
def svgToPdfs(content):
    drawing = svg2rlg(content)
    renderPDF.drawToFile(drawing, f"{content}.pdf")
    pdfs.append(f"{content}.pdf")

def svgToPdf():

    merger = PdfFileMerger()

    for i in pdfs:
        merger.append(i)

    merger.write("./output/Music Sheet.pdf")

    merger.close()
    clearCache()
    print("DONE")