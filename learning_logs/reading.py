import pytesseract

pytesseract.pytesseract.tesseract_cmd = '/home/leo/.cache/pip/wheels/ed/8a/c6/40c7ec06c2dd3df636832537238128a1471bf9c1b6a3a9bf40'

print(pytesseract.image_to_string('/home/leo/Downloads/image123.jpeg'))