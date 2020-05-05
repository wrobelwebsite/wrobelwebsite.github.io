#!/usr/bin/env python3
import tempfile, os
from pdf2image import convert_from_path
from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)

print("When inputing pages, please use the number that is listed on the page itself.")
chapter = input("Chapter Number: ")
first = input("First Page: ")
last = input("Last Page: ")



offset = 49
first = int(first) + offset
last = int(last) + offset
images = convert_from_path("/home/invisa/Documents/Wrobel/bio2Book.pdf", first_page=first, last_page=last)
path = "/home/invisa/Documents/github/wrobelwebsite.github.io/src/Ch%s" % chapter

if not os.path.isdir(path):
	os.mkdir(path)

count = 1
for image in images:
	if count > 10 : image.save(path+"/Chapter{}BIO-{}.png".format(chapter,count), "PNG")
	else : image.save(path+"/Chapter{}BIO-0{}.png".format(chapter,count), "PNG")
	count += 1
print("Converted pages to images")