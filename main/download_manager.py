import requests
import imghdr as tester
import os
import image_converter

png = 0
svg = 0

#Getting The Image
def imgDownloader(imgs):
    global png
    global svg
    index = 0

    for i in imgs:

        response = requests.get(i)

        image = f"image_{index}"

        file = open(f"./conversion/{image}", "wb")
        file.write(response.content)
        file.close()

        type  = tester.what(f"./conversion/{image}")
        if type == "png":
            png = 1
            os.rename(f"./conversion/{image}", f"./conversion/{image}.png")
            image_converter.PngFix(f"./conversion/{image}.png")
        else:
            svg = 1
            os.rename(f"./conversion/{image}", f"./conversion/{image}.svg")
            image_converter.svgToPdfs(f"./conversion/{image}.svg")

        index += 1

    if png == 1:
        image_converter.PngToPdf()
    if svg == 1:
        image_converter.svgToPdf()