from PIL import Image
import pytesseract
from google_trans_new import google_translator

def ocr_core(filename,targetlang):
# Sets up the googletranslator api
    translator = google_translator()
# Edit this path to tesseract.exe on your system. On windows its by default in the following:
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    # Opens image

    im = Image.open(filename)
    # Gets the image and translates it to Czech. You can specify own lang if you want.
    text = pytesseract.image_to_string(im)

    text_translated = translator.translate(text, lang_tgt=targetlang)
    return text_translated